def login_user(username, password):
    if username == "admin" and password == "admin123":
        return "Login successful"
    return "Invalid credentials"