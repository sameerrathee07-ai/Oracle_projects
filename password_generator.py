import secrets
import string
print("=== Simple Password Generator ===")
length = int(input("Enter password length: ")) # Enter the password length
# Ask which character sets to include
use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
use_digits = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"
# Build the character set
chars = ""
if use_lower:
    chars += string.ascii_lowercase
if use_upper:
    chars += string.ascii_uppercase
if use_digits:
    chars += string.digits
if use_symbols:
    chars += string.punctuation
# Make sure at least one set was chosen
if chars == "":
    print("You must select at least one character set.")
else:
    password = ""
    for _ in range(length):
        password += secrets.choice(chars)

    print("\nGenerated password:", password)