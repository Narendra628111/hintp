def microsoft_sso_login(token):
    if validate_token(token):
        return "SSO Login successful"
    return "SSO Login failed"

def validate_token(token):
    # Dummy validation
    return token == "valid_token"