
## `DELETE /api/jokes/{id}`
# Endpoint to delete a joke by unique id. If the joke does not exist, return 404 not found. 
# But if it does, mark the joke locally as deleted. Any subsequent reads should *NOT* see this joke.
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

        #@TODO 
        # display in response the joke that has been cancelled

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