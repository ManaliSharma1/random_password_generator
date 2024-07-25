# Python program to create a Password Generator application

import random   # For generating random choices
import string   # For easy access to sets of characters

print("***** Random Password Generator *****\n")
def main():
    # Specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    if length < 4 and length != 0:
        print("Password length must be at least 4 characters\n")

    elif length == 0:
        return

    else:
        # Define the combination of characters
        lower_chars = string.ascii_lowercase
        upper_chars = string.ascii_uppercase
        digit_chars = string.digits
        symbols_chars = string.punctuation

        # Combination of random characters to generate a password
        combine = lower_chars + upper_chars + digit_chars + symbols_chars
        x = random.sample(combine, length)
        password = "".join(x)

        # Display the generated password
        print("The Generated Password is: ", password, "\n")
    main()
main()
