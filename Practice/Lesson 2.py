def is_email(str_mail_check:str)->bool:
    if "@" in str_mail_check and len(str_mail_check)>3:
        return True
    else:
        return False
print("type your email")
my_str = input()
print(f"is mail?: {is_email(my_str)}")

def is_positive(number: int)->bool:
    return number>=0

print(f"is positive? {is_positive(-1)}")
print("type a number")
number = int(input())
print(f"is positive? {is_positive(number)}")

def is_school(number: int)->str:
    if 6 <= number <= 14:
        return "elementary school"
    elif 15 <= number <= 18:
        return "high school"
    else:
        return "not in school"

print(f"is in school: {is_school(6)}")
print(f"is in school: {is_school(14)}")
print(f"is in school: {is_school(15)}")
print(f"is in school: {is_school(18)}")
print(f"is in school: {is_school(5)}")
print(f"is in school: {is_school(19)}")

def is_a(number:int):
    if number == 1:
        print("a")
    else:
        print("b")

print ("type a number")
num = input()
is_a(int(num))

def is_even(number:int)-> bool:
    return number % 2 == 0
print(f"is even? {is_even(4)}")
print(f"is even? {is_even(3)}")
print("type a number")
num = int(input())
print(f"is even? {is_even(num)}")

def is_long_string(text:str) -> str:
    if len(text) < 4:
        return "too short"
    elif 4 <= len(text) <= 9:
        return "Ok"
    elif len(text) > 9:
        return "too long"
print(f"is long string? {is_long_string('Hello World')}")
print(f"is long string? {is_long_string('Hi')}")
print(f"is long string? {is_long_string('Python')}")

def age_category(age:int)->str:
    if age < 0:
        age = 0
    elif age > 120:
        age = 120
    if 0 <= age <= 18:
        return "teenager"
    elif 19 <= age <= 120:
        return "adult"

print("Type your age:")
user_age = int(input())
print(f"Category: {age_category(user_age)}")

def check_password(password: str) -> None:
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return
    if password[0] not in ('Z', 'C'):
        print("Password must start with 'Z' or 'C'.")
        return
    if not password.endswith('$'):
        print("Password must end with '$'.")
        return
    print("STRONG PASSWORD")

print("Type your password:")
user_password = input()
check_password(user_password)