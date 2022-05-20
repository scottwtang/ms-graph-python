def send_message_attachment(chat_id, attachment_name, attachment_path, attachment_id, access_token, chat_message = None):
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
            "content": f"{chat_message} <attachment id=\"{attachment_id}\"></attachment>"
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
