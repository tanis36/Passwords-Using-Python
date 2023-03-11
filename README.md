# Passwords-Using-Python

This is a project that walks through different scenarios such as creating a password and signing out and signing in to an account using the creatd password.
The files in this project are not necessarily used all together to accomplish one goal, rather each file goes through the separate processes. So, while the files 
"work with each other", they are more so just steps, which could be used in a larger project that truly creates an account, signs out and in, etc.



Run the following files in this order:
  
    create_account.py
  
    sign_out.py
  
    sign_in.py
  


create_account.py:

    In this file, the user will be creating a password that will be stored in a text file. This password will be used for signing in to an account.
  
  
sign_out.py:

    When this file is run, the user will be asked if they want to sign out. If they do want to sign out ('y'), then a .key file storing a key will be generated and 
    the text files will be encrypted.
  
  
sign_in.py:
  
    When running this file, the user will be asked to provide their password to sign in and decrypt their files. If the password is correct, then the user will be 
    successfully signed in and their files will be decrypted. If the password is incorrect, the user will be asked to try again. If there are three total incorrect 
    password entries, the user will be asked if they want to change their password. If no, the file run quits and the files remain encrypted. If yes, the user will 
    be asked to create a new password, then sign in with the new password. After this successful sign in, the files will be decrypted and the new password will 
    overwrite the old password in the existing text file.
