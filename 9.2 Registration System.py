import json
import re

FILE = "students.json"

# Load existing data
try:
    with open(FILE, "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []

print("===== Registration System =====")

name = input("Enter your name: ")

# Email validation
while True:
    email = input("Enter your email: ")

    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        break
    else:
        print("Invalid email! Please enter a valid email.")

# Password validation
while True:
    password = input("Enter your password: ")

    if len(password) >= 6:
        break
    else:
        print("Password must be at least 6 characters long.")

# Store data
student = {
    "name": name,
    "email": email,
    "password": password
}

students.append(student)

# Save to JSON
with open(FILE, "w") as file:
    json.dump(students, file, indent=4)

print("\nRegistration successful!")
print("Data saved in", FILE)