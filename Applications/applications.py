import requests

def add_client_secret(access_token, app_object_id, secret_description = None, secret_start_date_time = None, secret_end_date_time = None):
    # This function adds a client secret to an application
    # https://docs.microsoft.com/en-us/graph/api/application-addpassword
    
    request_url = f"https://graph.microsoft.com/v1.0/applications/{app_object_id}/addPassword"

    request_headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    request_body = (
        {
            "passwordCredential": {
                "displayName": secret_description,
                "startDateTime": secret_start_date_time,
                "endDateTime": secret_end_date_time,
            }
        }
    )

    result = requests.post(url = request_url, headers = request_headers, json = request_body)

    return(result)
