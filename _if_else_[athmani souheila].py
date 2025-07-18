firstname=input("Enter your first name: ")
lastname=input("Enter your last name: ")

if firstname and lastname:
    print(f"Welcome, {firstname} {lastname}")
else:
    print("Error: Both first name and last name must be provided.")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "password123":
    print("Login successful.")
elif username != "admin":
    print("Error: Invalid username.")
else:
    print("Error: Invalid password.")