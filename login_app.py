import getpass

correct_username = "admin"
correct_password = "123456"
max_attempts = 3

for attempt in range(max_attempts):
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        remaining = max_attempts - attempt - 1
        if remaining > 0:
            print("Invalid username or password.")
            print(f"Attempts remaining: {remaining}")
        else:
            print("Too many failed attempts. Access denied.")