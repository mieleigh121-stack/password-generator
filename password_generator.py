import random
import string


# ---------------------------------------------------------
# FUNCTION: generate_password
# ---------------------------------------------------------
# This function creates a random password based on user
# preferences.
#
# Parameters:
#   length (int) - desired password length
#   use_upper (bool) - include uppercase letters
#   use_lower (bool) - include lowercase letters
#   use_digits (bool) - include numbers
#   use_symbols (bool) - include special characters
#
# Returns:
#   A randomly generated password string
#   OR
#   None if no character types were selected
# ---------------------------------------------------------
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """"
    Generate a random password based on selected character types.

    Parameters:
        lenght (int): Desired password length
        use_upper (bool): Include uppercase letters
        use_lower (bool): Include lowercase letters
        use_digits (bool): Include digits
        use_symbols (bool): Include symbols

        Returns:
            str of None: Generated password, or None if no character types selected
        """

    # This variable will store all possible characters
    # the password can use based on user selection


    characters = ""

     # If user selected uppercase letters,
    # add all uppercase letters to the character pool


    if use_upper:
        characters += string.ascii_uppercase

         # If user selected lowercase letters,
    # add all lowercase letters to the character pool


    if use_lower:
        characters += string.ascii_lowercase

        # If user selected digits,
    # add numbers 0–9 to the character pool


    if use_digits:
        characters += string.digits

         # If user selected symbols,
    # add punctuation symbols to the character pool


    if use_symbols:
        characters += string.punctuation

        # SAFETY CHECK:
    # If the character pool is empty,
    # it means the user selected no character types.
    # In this case, return None to avoid runtime errors.

    # Safety check
    if characters == "":
        return None
    
        # Create an empty string to build the password


    password = ""

    # Loop 'length' times and randomly select
    # one character from the pool each time


    for _ in range(length):
        password += random.choice(characters)
    
    return password

    # Return the completed password

# ---------------------------------------------------------
# FUNCTION: get_user_preferences
# ---------------------------------------------------------
# This function handles all user input and validates
# the password length.
#
# Returns:
#   length (int)
#   use_upper (bool)
#   use_lower (bool)
#   use_digits (bool)
#   use_symbols (bool)
# ---------------------------------------------------------


def get_user_preference():
    """
    Collects and validates user imput for password settings.
    """

        # Keep asking for length until user enters valid input


    while True:
        try:
            length = int(input("Enter desired password length: "))

                        # Check that the length is positive

            if length <= 0:
                print("Password length must be greater than 0.")
                continue
            break # Exit loop if valid input
            # If user enters non-number input,
        # this catches the error and prevents crash
        except ValueError:
            print("Please enter a valid number.")
                # Ask user which character types to include
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    return length, use_upper, use_lower, use_digits, use_symbols

# ---------------------------------------------------------
# FUNCTION: main
# ---------------------------------------------------------
# This is the main control function of the program.
# It calls other functions and controls the overall flow.
# ---------------------------------------------------------

def main():
    print("=== Password Generator ===")
    # Collect user preferences

    length, use_upper, use_lower, use_digits, use_symbols = get_user_preferences()
    # Generate the password

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        # If password is None, no character types were selected

    if password is None:
        print("Error: You must select at least one character type.")
    else:
        print("Generated Password:", password)
# This ensures the program only runs
# when executed directly (not when imported as a module)
if __name__ == "__main__":
    main()