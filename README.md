# Chuck Norris jokes API caller

## What is this

A minimalistic flask API application that let the user search, create, delete and update jokes from [Chuck Norris jokes](https://api.chucknorris.io/), that works through for example Postman. To simplify the description, we will call [Chuck Norris jokes](https://api.chucknorris.io/) as remote and application implemented in this assignment as local.

Please read this file and follow its instructions to install, setup, run and operate the application.


![Chuck Norris Jokes app cover](/static/img/chuck_norris_jokes_app_cover_v2.png?raw=true "Chuck Norris Jokes app cover")


## Install

    virtualenv venv

    source venv/bin/activate

    cat requirements.txt | xargs -n 1 pip install

> [!WARNING]
> Do not change the project name after the virtual environment was created, otherwise the environment will not be recognized and will have to be deleted and regenerated.

### apply migrations

export the app script path as bash variable

    export FLASK_APP=chuck_norris_jokes_caller/app.py

Initialize the db migration gear: it will create a folder at path `migrations`.<br>

> [!TIP]
> You should ignore the error in case a folder `migrations` is already present/versioned in the project.

> [!NOTE]
> In case you deleted migrations and you want to init the db again:
> 
>     sqlite3 chuck_norris_jokes_caller/chuck_norris_jokes_caller.sqlite
>     
>         delete from alembic_version;  

create migration required files

    flask db init

save the changes to DB structure

    flask db migrate -m "< migration message here>"

apply the changes to DB structure

    flask db upgrade 

> [!NOTE]
> Every time the DB structure is changed, you have to run
> 
>     flask db migrate -m "< migration message here>"
> 
>     flask db upgrade

> [!NOTE]
> Every time you open a bash session or terminal and want to operate the migrations, you have to run
> 
>     export FLASK_APP=chuck_norris_jokes_caller/app.py


### Populate the database with test data

    python chuck_norris_jokes_caller/populate_database.py

In case you need to manipulate db data via SQL

    sqlite3 chuck_norris_jokes_caller/chuck_norris_jokes_caller.sqlite


### Run the app

activate the virtual environment

    source venv/bin/activate

run the server 

    flask --app chuck_norris_jokes_caller/app run --debug

>[!WARNING]
> do not add `--debug` in production!


## Usage

Import in your Postman application the json collections stored in folder `dev_utils/postman_collections` and have fun with the app.


### Available APIs


### `GET /jokes/?query={query}`
Free text search endpoint. You should take local and remote search results into consideration.

### `POST /api/jokes/`
Endpoint to create joke locally.

### `GET /api/jokes/{id}`
Endpoint to retrieve a joke by unique id. You should take local and remote results into consideration.

### `PUT /api/jokes/{id}`
Endpoint to update a joke by unique id. If the joke does not exist, return 404 not found. But if it does, store a updated version locally. Any subsequent reads should only see this updated version.

### `DELETE /api/jokes/{id}`
Endpoint to delete a joke by unique id. If the joke does not exist, return 404 not found. But if it does, mark the joke locally as deleted. Any subsequent reads should *NOT* see this joke.



