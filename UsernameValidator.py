username = input("Enter your username: ")

try:
    if len(username) < 5 or len(username) > 10 or not username.isalnum():
        raise ValueError("Invalid username")
    print("Username accepted!")
except ValueError:
    print("username too short or wrong format(no special characters allowed)")
