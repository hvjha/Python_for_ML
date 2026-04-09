def username(name = "Guest"):
    return f"Hello, {name}! Welcome to the Python programming world."

user_name = input("Please enter your name: ")
if user_name.strip():
    print(username(user_name))
else:
    print(username())
    