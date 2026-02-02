import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'
    if re.match(pattern, phone):
        return True
    return False

def validate_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&]).{8,}$'
    if re.match(pattern, password):
        return True
    return False


email = input("Enter your email: ")
phone = input("Enter your mobile number: ")
password = input("Enter your password: ")

if validate_email(email):
    print("Email is valid")
else:
    print("Email is invalid")

if validate_phone(phone):
    print("Phone number is valid")
else:
    print("Phone number is invalid")

if validate_password(password):
    print("Password is Strong")
else:
    print("Password is Weak")
