        # print("create new joke")

        # # call the add_joke api
        # response = call_add_joke_api(content)

        # # turning the response object to a dictionary
        # pythonified_response = response.json()
        # # status_code = response.status_code

        # new_response_dict = {
        #     "action": "insert" ,
        #     "updated_joke_data": pythonified_response
        # }

        # if response.ok:
        #     # Return the JSON from the response if it is successful
        #     return (
        #         json.dumps(new_response_dict), 
        #         response.status_code, 
        #         {'Content-Type': 'application/json'}
        #         )
        
        # else:
        #     # Handle the case where adding the joke failed

        #     error_response = {
        #         "success": False, 
        #         "message": "Failed to create new joke."
        #         }

        #     return (
        #         json.dumps(error_response), 
        #         response.status_code, 
        #         {'Content-Type': 'application/json'}
        #         )