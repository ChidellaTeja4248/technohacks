import random
import string


def pas(length):
    special = "@!#$%^&*+_-"
    characters = string.ascii_letters + string.digits + special
    passwords = ''.join(random.choice(characters) for _ in range(length))
    return passwords


try:
    input_length = int(input("Enter the length of the password you want: "))
    # password = generate_password(lengthofinput)
    if input_length <= 0:
        raise ValueError("password length must be greater than 0")
    password = pas(input_length)
    print("Your generated password is :", password)
except ValueError as e:
    print(f"Invalid {e}")
except Exception as e:
    print(f"an error {e}")
