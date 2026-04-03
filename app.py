# This is a simple login, signup, and password reset application using SQLite as the database. The application allows users to create an account, log in with their credentials, and reset their password if they forget it. The user data is stored in a SQLite database called 'database.db'.

import sqlite3 # Importing the sqlite3 module to interact with the SQLite database.

con = sqlite3.connect('database.db')
cursor = con.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
               id INTEGER PRIMARY KEY ,
               name TEXT UNIQUE NOT NULL,
               pass TEXT NOT NULL
               )
''')

# this code creates a table named 'data' in the database if it does not already exist. The table has three columns: 'id' (an integer primary key), 'name' (a unique text field that cannot be null), and 'pass' (a text field that cannot be null).

con.commit

# This line commits the changes made to the database, ensuring that the table creation is saved.
def login(name , password):
    cursor.execute("SELECT * FROM data WHERE name =? AND pass =?",(name,password))
    result =cursor.fetchone()
    if result:
         print("\n")
         print("------------------------------------")
         print("Login Successful")
         print("\n")
         print("------------------------------------")
    else:
         print("\n")
         print("------------------------------------")
         print("Invalid Username and Passwrod Try Again")
         print("\n")
         print("------------------------------------")
# The login function takes a username and password as input, queries the database to find a matching record, and prints a success message if the credentials are correct or an error message if they are not.
def singup(new_name,new_pass):
    try:
        cursor.execute("INSERT INTO data (name ,pass) VALUES (?,?)",(new_name,new_pass))
        print("\n")
        print("------------------------------------")
        print("Account Created")
        print("\n")
        print("------------------------------------")
        con.commit()
    except:
        print("\n")
        print("------------------------------------")
        print("Username not Available")
        print("\n")
        print("------------------------------------")

# The singup function takes a new username and password as input, attempts to insert a new record into the database, and prints a success message if the account is created. If the username is already taken (due to the UNIQUE constraint), it catches the exception and prints an error message.
def forget(user_name ,new_pass):
    cursor.execute("UPDATE data SET pass = ? WHERE name =?",(new_pass,user_name))
    print("\n")
    print("------------------------------------")
    print("Password Forget ")
    print("\n")
    print("------------------------------------")
    con.commit

# The forget function takes a username and a new password as input, updates the password for the specified username in the database, and prints a message indicating that the password has been reset. It then commits the changes to the database.
def main():
    while True:# This is the main function that runs an infinite loop to display the menu and handle user input for login, signup, password reset, and exiting the application.
        print("Wlecome To App")
        print("\n1 Login")
        print("2 Sing-Up")
        print("3 Forget Password")
        print("4 Exit app")
        print("\n")
        user =input("Enter Your Option --> ")
# The user is prompted to enter an option (1 for login, 2 for signup, 3 for password reset, and 4 for exit). Based on the user's input, the corresponding function is called to handle the requested action. If the user chooses to exit, the loop breaks and the application ends.
        if user == "1":
            name = input("Enter Your Username --> ")
            password = input("Enter Your Password --> ")
            login(name ,password)
        
        elif user == "2":
            newName = input("Enter Your New User Name -->  ")
            newPassword = input("Enter Your New Password -->  ")
            singup(newName,newPassword)
        
        elif user == "3":
            user_name = input("Enter Your User Name --> ")
            new_pass =input("Enter Your newPassword --> ")
            forget(user_name,new_pass)
        
        elif user == "4":
            print("Thanks For Comeing")
            break

        else:
            print("Invalide Try Again ")

    con.close()
# The main function displays a menu to the user, allowing them to choose between logging in, signing up, resetting their password, or exiting the application. It handles user input and calls the appropriate functions based on the user's choice. The loop continues until the user chooses to exit, at which point it prints a goodbye message and breaks the loop. Finally, it closes the database connection.
if __name__ == '__main__':
    main()



    


