import string
import secrets

def generate_secure_password(length):
    """
    Generate a secure password using printable characters.

    Parameters:
    - length (int): Length of the password.

    Returns:
    - str: Generated secure password.
    """
    all_characters = string.printable
    return ''.join(secrets.choice(all_characters) for _ in range(length))

def get_password_length():
    """
    Get the desired password length from user input.

    Returns:
    - int: Desired password length.
    """
    while True:
        password_length_input = input('Enter your password length (type "exit" to stop): ')
        if password_length_input.lower() == "exit":
            print("Exiting the program.")
            exit()
        try:
            return int(password_length_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

def main():
    """
    Main function to interact with the user and generate passwords.
    """
    print("Secure Password Generator")
    print("=========================")

    while True:
        password_length = get_password_length()

        # Generate a secure password
        password = generate_secure_password(password_length)

        # Print the generated password
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
