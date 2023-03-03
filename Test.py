import random
import string


def generate_password(length, uppercase, digits, special_chars):
    """
    Generates a random password with the specified length and character types.
    """
    chars = string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def main():
    """
    Main function that prompts the user for input and generates a password.
    """
    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, uppercase, digits, special_chars)
    print("Your password is:", password)


if __name__ == '__main__':
    main()
