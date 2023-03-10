import os
from cryptography.fernet import Fernet

personal_files = []

# Add text files in list directory to personal_files list
for file in os.listdir():
    if file == "sign_out.py" or file == "key.key" or file == "sign_in.py" or file == "create_account.py" or file == "user_password.txt":
        continue
    if os.path.isfile(file):
        personal_files.append(file)

# Create a key and write it to .key file
key = Fernet.generate_key()

with open("key.key", "wb") as the_key:
    the_key.write(key)


# Ask the user if they want to sign out
ask_sign_out = input("Are you sure you want to sign out? (y/n): ")

# If yes, encrypt their files and sign them out
if ask_sign_out == "y":
    for file in personal_files:
        with open(file, "rb") as the_file:
            contents = the_file.read()
        encrypted_contents = Fernet(key).encrypt(contents)
        with open(file, "wb") as the_file:
            the_file.write(encrypted_contents)
    print("\nSign out successful.")

# If no, let them know they are still signed in
elif ask_sign_out == "n":
    print("\nOk. You are still signed in.")    