from datetime import datetime

from flask import render_template
from flask import request

import sqlite3
import requests
import json

from app import app
from app import db
from app import sqlite_db_path

# import queries
from db_queries import \
    GET_JOKES_BY_FREE_TEXT, \
    GET_JOKE_BY_JOKE_ID, \
    SET_JOKE_AS_NOT_ACTIVE

# import models
from models import \
    Joke, \
    JokeVersion


from sqlalchemy.exc import IntegrityError


###########
# APIs
###########


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/helloname/')
def helloname():
    name = request.args.get('name', 'You')
    # http://127.0.0.1:5000/helloname/?name=mario
    return f'<h1>Welcome on Chuck Norris Jokes app, {name}!</h1>' 


### `GET /jokes/?query={query}`
# Free text search endpoint. You should take local and remote search results into consideration.
@app.route('/jokes/')
def get_jokes_by_free_text():

    # caller app jokes
    #-----------------

    # http://127.0.0.1:5000/jokes/?query=cigars

    free_text = request.args.get('query', 'NO_TEXT')

    free_text_lowered_and_wrapped_with_jollychars = f"%{free_text.lower()}%"

    conn = sqlite3.connect(sqlite_db_path)
    curs = conn.cursor()

    # print(free_text)

    curs.execute(GET_JOKES_BY_FREE_TEXT, (free_text_lowered_and_wrapped_with_jollychars,))
    query_results = curs.fetchall()

    conn.close()

    listofdicts_query_results = [
    {
        "id": item[0],
        "is_active": item[1],
        "joke_version_id": item[2],
        "creation_timestamp": 
            datetime.
            fromtimestamp(item[3]).
            strftime('%Y-%m-%d %H:%M:%S'),
        "content": item[4],
    }
    for item in query_results
]

    caller_app_jokes = listofdicts_query_results

    # remote app jokes
    #-----------------

    remote_app_api_url = "https://api.chucknorris.io/jokes/search?query={}".format(free_text)

    remote_app_response = requests.get(remote_app_api_url)
    remote_app_response_data = remote_app_response.json()

    remote_app_jokes = remote_app_response_data

    # unite jokes
    #-----------------

    jokes = {
        "caller_app_jokes": caller_app_jokes,
        "remote_app_jokes": remote_app_jokes
    }

    return jokes
    

# ### `GET /api/jokes/{id}`
# Endpoint to retrieve a joke by unique id. You should take local and remote results into consideration.
@app.route('/api/jokes/<string:joke_id>', methods=['GET'])
def get_joke_by_id(joke_id):

    # ascertain which are the target apps you want to launch the query on
    #----------------

    request_body = request.get_json()

    target_apps = request_body.get('target_apps', [])

    valid_targets = {'local', 'remote'}

    target_apps_set = set(target_apps)

    # Check for valid target_apps values
    if \
        not target_apps \
        or \
        not target_apps_set.issubset(valid_targets):

        # issubset(valid_targets): 
        # restituisce True se tutti gli elementi di target_apps_set sono presenti in valid_targets.

        error_response = {
            "success": False,
            "message": "The 'target_apps' field must contain a list with 'local', 'remote', or both."
        }

        status_code = 400

        return (
            json.dumps(error_response), 
            status_code, 
            {'Content-Type': 'application/json'}
            )
    
    jokes = dict()

    # caller app jokes
    #-----------------

    # Fetch jokes locally if 'local' is in target_apps
    if 'local' in target_apps:

        # http://127.0.0.1:5000/api/jokes/2

        conn = sqlite3.connect(sqlite_db_path)
        curs = conn.cursor()

        # print(joke_id)

        curs.execute(GET_JOKE_BY_JOKE_ID, (joke_id,))
        query_results = curs.fetchall()

        conn.close()

        listofdicts_query_results = [
            {
                "id": item[0],
                "is_active": item[1],
                "joke_version_id": item[2],
                "creation_timestamp": 
                    datetime.
                    fromtimestamp(item[3]).
                    strftime('%Y-%m-%d %H:%M:%S'),
                "content": item[4],
            }
            for item in query_results
        ]

        caller_app_jokes = listofdicts_query_results

        jokes["local_app_jokes"] = caller_app_jokes

    # remote app jokes
    #-----------------

    # Fetch jokes remotely if 'remote' is in target_apps
    if 'remote' in target_apps:

        remote_app_api_url = "https://api.chucknorris.io/jokes/{}".format(joke_id)

        remote_app_response = requests.get(remote_app_api_url)
        remote_app_response_data = remote_app_response.json()

        remote_app_jokes = remote_app_response_data

        jokes["remote_app_jokes"] = remote_app_jokes

    # unite jokes
    #-----------------



    return jokes


## `DELETE /api/jokes/{id}`
# Endpoint to delete a joke by unique id. If the joke does not exist, return 404 not found. But if it does, mark the joke locally as deleted. Any subsequent reads should *NOT* see this joke.
@app.route('/api/jokes/<string:joke_id>', methods=['DELETE'])
def delete_joke_by_id(joke_id):

    # caller app jokes
    #-----------------

    # http://127.0.0.1:5000/api/jokes/2

    conn = sqlite3.connect(sqlite_db_path)
    curs = conn.cursor()

    # print(joke_id)

    curs.execute(SET_JOKE_AS_NOT_ACTIVE, (joke_id,))

    if curs.rowcount == 0:
        # No update
        status_code = 404

        response = {
            "success": False,
            "msg": f"Cannot delete Joke. Joke with id {joke_id} not found or already deleted (TIP: deactivated).",
            "status_code": status_code

        }
        
    else:
        # success
        status_code = 200

        response = {
            "success": True,
            "msg": f"Joke with id {joke_id} has been set as not active.",
            "status_code": status_code
        }
        

    conn.commit()  # here I have to commit the change
    conn.close()

    return (
        json.dumps(response), 
        status_code, 
        {'Content-Type': 'application/json'}
        )


@app.route('/api/jokes/', methods=['POST'])
def add_joke():

    request_body = request.get_json()

    if 'content' not in request_body:
        response = {
            "success": False,
            "message": "The request body does not contain the field 'content'."
        }
        return (
            json.dumps(response), 
            400, 
            {'Content-Type': 'application/json'}
            )

    content = request_body['content']

    try:
        new_joke = Joke()
        db.session.add(new_joke)

        # Execute the query but don't do the commit
        # so I can get and give new_joke.id to the new joke_version object
        db.session.flush()  

        current_timestamp = datetime.now().timestamp()
        current_timestamp_in_seconds = int(current_timestamp)

        new_joke_version = JokeVersion(
            joke_id=new_joke.id,  # match the two objects
            content=content,
            creation_timestamp = current_timestamp_in_seconds
        )
        db.session.add(new_joke_version)

        db.session.commit()

        response = {
            "success": True,
            "message": "A new joke has been successfully created.",
            "new_joke": {
                "id": new_joke.id,
                "is_active": new_joke.is_active,
                "joke_version_id": new_joke_version.id,
                "creation_timestamp": current_timestamp,
                "content": new_joke_version.content
            }
        }
        status_code = 201  # Created

    except IntegrityError as e:
        # Gestisci l'IntegrityError specifico
        response = {
            "success": False,
            "error_type": "IntegrityError",
            "message": "The operation violated a database integrity constraint.",
            "details": str(e)
        }

        status_code = 500  # Internal Server Error

    except Exception as e:
        db.session.rollback()  # Annulla la transazione in caso di errore
        response = {
            "success": False,
            "message": str(e)
        }

        status_code = 500  # Internal Server Error

    return (
        json.dumps(response), 
        status_code, 
        {'Content-Type': 'application/json'}
        )



### `PUT /api/jokes/{id}`
# Endpoint to update a joke by unique id. 
# If the joke does not exist, return 404 not found. 
# But if it does, store a updated version locally. 
# Any subsequent reads should only see this updated version.
@app.route('/api/jokes/<int:joke_id>', methods=['PUT'])
def update_joke_by_id(joke_id):

    request_body = request.get_json()

    # check the request requirements
    #-----------------

    if ('content' not in request_body):
        response = {
            "success": False,
            "message": "The request body does not contain the field 'content'."
        }
        return (
            json.dumps(response), 
            400, 
            {'Content-Type': 'application/json'}
            )

    content = request_body['content']


    # check if there is already a joke stored with the given id (only in local app)
    #-----------------

    # @TODO: 
    # change the get joke by id with 
    # a body parameter that allows to specify if you want to retieve the joke 
    # from remote or local or both apps.
    # exploit that new api to retrieve the joke here and avoid to write more code

    # http://127.0.0.1:5000/api/jokes/2

    conn = sqlite3.connect(sqlite_db_path)
    curs = conn.cursor()

    # print(joke_id)
    # print(content)

    curs.execute(GET_JOKE_BY_JOKE_ID, (joke_id,))
    query_results = curs.fetchall()

    conn.close()

    listofdicts_query_results = [
        {
            "id": item[0],
            "is_active": item[1],
            "joke_version_id": item[2],
            "creation_timestamp": 
                datetime.
                fromtimestamp(item[3]).
                strftime('%Y-%m-%d %H:%M:%S'),
            "content": item[4],
        }
        for item in query_results
    ]

    caller_app_jokes = listofdicts_query_results


    # @TODO: 
    # define functions that run in case the joke with given id exists or not.

    def call_add_joke_api(content):
        url = "http://127.0.0.1:5000/api/jokes/"
        headers = {
            "Content-Type": "application/json"
        }
        body = {
            "content": content
        }
        response = requests.post(url, headers=headers, data=json.dumps(body))
        return(response)


    if len(caller_app_jokes) == 1:
        # update existing

        # new function
        pass

    elif len(caller_app_jokes) == 0:
        # create new one

        # call the add_joke api
        response = call_add_joke_api(content)

        return( response )

    else:
        raise ValueError("Code should never get here.")

