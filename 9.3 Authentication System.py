import json

FILE = "students.json"

# Load registered users
try:
    with open(FILE, "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []

print("===== Login System =====")

email = input("Enter your email: ")
password = input("Enter your password: ")

login_success = False

for student in students:
    if student["email"] == email and student["password"] == password:
        login_success = True
        print("Login successful!")
        print("Welcome,", student["name"])
        break

if not login_success:
    print("Login failed!")
    print("Invalid email or password.")