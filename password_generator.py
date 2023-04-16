'''
Password generator!
'''
import string
import random


def generate_password(length=12):
    '''
    Generate a strong password with a given length (default is 12).

    Args:
        length (int): The desired length of the password. Must be at least 12 characters.

    Returns:
        str: A randomly generated strong password containing uppercase letters, 
        lowercase letters, digits, and special characters.

    Raises:
        ValueError: If the password length is less than 12 characters.
    '''
    if length < 12:
        raise ValueError(
            "A strong password length should be at least 12 characters.")

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_chars = uppercase_letters + lowercase_letters + digits + special_chars
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)
