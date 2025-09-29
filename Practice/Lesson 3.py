import re

# i is a variable that counts the 'for' loop
# for i in range(0,101,10):
#     if i > 70:
#         break
#     print(i)

# i=0
# while i < 3:
#     print (i)
#     i += 1
#
# print("Loop ended")


# num= int(input("Enter a number: "))
# print(f"The number is {num}")
# for i in range (0, num+1):
#     print(i)
# print("Loop ended")

# num= int(input("Enter a number: "))
# print(f"The number is {num}")
# while num <= 0:
#     print("Please enter a positive number")
#     num= int(input("Enter a number: "))
# for i in range (0, num+1):
#     print(i)
# print("Loop ended")

# counter = 0
# sum = 0
# for i in range(1,51):
#     sum += i
#     counter += 1
#     if i % 2 == 0:
#         print("even")
#     else:
#         print(i)
# print("Loop ended")
# print(f"The sum is {sum}")
# print(f"The average is {sum/counter}")

# for i in range(-5,9):
#     print(i)
# print("Loop ended")

# for i in range(2,17,2):
#     print(i)
# print("Loop ended")



def is_valid_email(email_str: str) -> bool:
    """
    Validate if string matches email regex pattern.

    Args:
        email_str: String to validate

    Returns:
        True if valid email format, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'

    if re.match(pattern, email_str):
        return True
    else:
        return False

# str = input("Enter your email: ")
# print(f"Is the email valid? {is_valid_email(str)}")

emails = ["dor20000@gmail.com", "invalid-email@", "Moshe@gmail", "Guldroy@walla.co.il", "user@domain..com", "user@google.com", "user@domain.c", "user@yahoo.com"]
# for email in emails:
#     print(f"Email: {email}, Valid: {is_valid_email(email)}")

