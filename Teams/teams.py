def send_chat_message(access_token, chat_id: str, msg_content: str = ""):
    # This function sends a Teams chat message, see Example 1
    # https://docs.microsoft.com/en-us/graph/api/chatmessage-post?view=graph-rest-1.0&tabs=http#example-1-send-a-hello-world-message-in-a-channel

    request_url = f"https://graph.microsoft.com/v1.0/chats/{chat_id}/messages"

    request_headers = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json"
        }

    request_body = {
        "body": {
            "content": msg_content
        }
    }

    result = requests.post(url = request_url, headers = request_headers, json = request_body)
    return(result)

def send_chat_message_attachment(access_token: str, chat_id: str, attachment_name: str, attachment_path: str, attachment_id: str, msg_content: str = ""):
    # This function sends a Teams chat message with an attachment, see Example 4
    # https://docs.microsoft.com/en-us/graph/api/chatmessage-post?view=graph-rest-1.0&tabs=http#example-4-send-a-message-with-file-attachment-in-it

    request_url = f"https://graph.microsoft.com/v1.0/chats/{chat_id}/messages"

    request_headers = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json"
        }

    request_body = {
        "body": {
            "contentType": "html",
            "content": f"{msg_content} <attachment id=\"{attachment_id}\"></attachment>"
        },
        "attachments": [
            {
                "id": attachment_id,
                "contentType": "reference",
                "contentUrl": f"{attachment_path}/{attachment_name}",
                "name": attachment_name
            }
        ]
    }

    result = requests.post(url = request_url, headers = request_headers, json = request_body)
    return(result)
