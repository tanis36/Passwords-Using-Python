# Ask the user to create a password
user_password = input("Please create a password: ")

while True:
    password_confirmation = input("Enter password again to ensure they match: ")

    # Write the password to a file if they match
    if password_confirmation == user_password:
        with open("user_password.txt", "w") as the_file:
            the_file.write(user_password)
        print("Password created successfully.")
        break

    # If they do not match, ask user to enter password again
    else:
        print("\nThe password you entered does not match.")