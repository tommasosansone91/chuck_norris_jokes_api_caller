

    # http://127.0.0.1:5000/api/jokes/2

    # conn = sqlite3.connect(sqlite_db_path)
    # curs = conn.cursor()

    # # print(joke_id)
    # # print(content)

    # curs.execute(GET_JOKE_BY_JOKE_ID, (joke_id,))
    # query_results = curs.fetchall()

    # conn.close()

    # listofdicts_query_results = [
    #     {
    #         "id": item[0],
    #         "is_active": item[1],
    #         "joke_version_id": item[2],
    #         "creation_timestamp": 
    #             datetime.
    #             fromtimestamp(item[3]).
    #             strftime('%Y-%m-%d %H:%M:%S'),
    #         "content": item[4],
    #     }
    #     for item in query_results
    # ]

    # caller_app_jokes = listofdicts_query_results