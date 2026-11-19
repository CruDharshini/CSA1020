def login(username, password):
    """Return a simple demonstration login result."""
    if username == "admin" and password == "1234":
        return "Login Successful"
    return "Invalid Credentials"

if __name__ == "__main__":
    print(login("admin", "1234"))
    print(login("student", "wrong"))
