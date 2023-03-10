import os
from cryptography.fernet import Fernet

personal_files = []

# Add text files in list directory to personal_files list
for file in os.listdir():
    if file == "sign_out.py" or file == "key.key" or file == "sign_in.py" or file == "create_account.py" or file == "user_password.txt":
        continue
    if os.path.isfile(file):
        personal_files.append(file)


# Read the contents of "key.key" to the key variable
with open("key.key", "rb") as the_key:
    key = the_key.read()

# Counter to limit incorrect password entries
counter = 0

while True:

    ask_for_password = input("Please enter your password: ")

    with open("user_password.txt", "r") as the_file:
        user_password = the_file.read()

    # If the passwords match, decrypt the files
    if ask_for_password == user_password:
        for file in personal_files:
            with open(file, "rb") as the_file:
                contents = the_file.read()
            decrypted_contents = Fernet(key).decrypt(contents)
            with open(file, "wb") as the_file:
                the_file.write(decrypted_contents)
        print("\nSign in successful.")
        break

    # If the passwords do not match, have the user try again
    else:
        counter += 1

        if counter < 3:
            print("\nIncorrect password. Please try again.")

        # If there are 3 incorrect password entries, ask the user if they would like to reset their password
        if counter == 3:
            response = input("\nThere were too many incorrect password entries. Would you like to reset your password? (y/n): ")

            # If the user answers yes, have them reset their password
            if response == "y":

                user_password = input("Please create a password: ")

                while True:
                    password_confirmation = input("Enter password again to ensure they match: ")

                    # Write the password to a file if they match
                    if password_confirmation == user_password:
                        with open("user_password.txt", "w") as the_file:
                            the_file.write(user_password)
                        new_password = input("\nPassword changed successfully. Please try signing in again with your new password: ")

                        with open("user_password.txt", "r") as the_file:
                            user_password = the_file.read()

                        # If the passwords match, decrypt the files
                        if new_password == user_password:
                            for file in personal_files:
                                with open(file, "rb") as the_file:
                                    contents = the_file.read()
                                decrypted_contents = Fernet(key).decrypt(contents)
                                with open(file, "wb") as the_file:
                                    the_file.write(decrypted_contents)
                            print("\nSign in successful.")
                            break

                        break

                    # If they do not match, ask user to enter password again
                    else:
                        print("\nThe password you entered does not match.")
                break

            else:
                print("Ok. Please try again later.")
                break