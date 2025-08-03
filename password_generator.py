# Python Programming 
# Task 3: Create a Password Generator

import random 
import string

print("----Welcome to Password Generator----")
length = int(input("Password length: "))
chars = ""

if input("Include uppercase? (y/n): ").lower() == 'y':
    chars += string.ascii_uppercase
if input("Include lowercase? (y/n): ").lower() == 'y':
    chars += string.ascii_lowercase
if input("Include digits? (y/n): ").lower() == 'y':
    chars += string.digits
if input("Include symbols? (y/n): ").lower() == 'y':
    chars += string.punctuation

# Check for empty selection
if not chars:
    print("Error: No character types selected.")
else:
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)
