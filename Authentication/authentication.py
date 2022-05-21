import msal

def get_token_with_client_secret(client_id, client_secret, tenant_id):
    # This function is to obtain a bearer token using the client credentials flow, with a client secret instead of a certificate
    # https://docs.microsoft.com/en-us/graph/sdks/choose-authentication-providers?tabs=CS#client-credentials-provider
    
    app = msal.ConfidentialClientApplication(
        client_id         = client_id,
        client_credential = client_secret,
        authority         = f"https://login.microsoftonline.com/{tenant_id}")

    scopes = ["https://graph.microsoft.com/.default"]

    token = app.acquire_token_for_client(scopes = scopes)

    return(token)
