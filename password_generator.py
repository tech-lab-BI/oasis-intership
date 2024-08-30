import random
import string

def password_generator(length, use_letters, use_numbers, use_symbols):
    """
    Generates a random password based on user-defined criteria.

    Args:
        length (int): The length of the password.
        use_letters (bool): Whether to include letters in the password.
        use_numbers (bool): Whether to include numbers in the password.
        use_symbols (bool): Whether to include symbols in the password.

    Returns:
        str: The generated password.
    """
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type should be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    password = password_generator(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Generated Password : ", password)

if __name__ == "__main__":
    main()