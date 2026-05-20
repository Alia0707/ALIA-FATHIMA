# Password Strength Checker

import re

print("========== Password Strength Checker ==========\n")

# Taking password input
password = input("Enter your password: ")

# Special character pattern
special_characters = r"[!@#$%^&*(),.?\":{}|<>]"

# Checking password conditions
if len(password) >= 8 and re.search(special_characters, password):
    print("\n✅ Strong Password")
    print("Your password has good length and contains a special character.")
else:
    print("\n❌ Weak Password")
    print("Password must:")
    print("- Be at least 8 characters long")
    print("- Contain at least one special character")