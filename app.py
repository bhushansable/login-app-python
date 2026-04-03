
import sqlite3

con = sqlite3.connect('database.db')
cursor = con.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
               id INTEGER PRIMARY KEY ,
               name TEXT UNIQUE NOT NULL,
               pass TEXT NOT NULL
               )
''')


con.commit


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
        print("Username not Available")


def forget(user_name ,new_pass):
    cursor.execute("UPDATE data SET pass = ? WHERE name =?",(new_pass,user_name))
    print("\n")
    print("------------------------------------")
    print("Password Forget ")
    print("\n")
    print("------------------------------------")
    con.commit


def main():
    while True:
        print("Wlecome To App")
        print("\n1 Login")
        print("2 Sing-Up")
        print("3 Forget Password")
        print("4 Exit app")
        print("\n")
        user =input("Enter Your Option --> ")

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
            new_pass =input("Enter Your Password --> ")
            forget(user_name,new_pass)
        
        elif user == "4":
            print("Thanks For Comeing")
            break

        else:
            print("Invalide Try Again ")

    con.close()
if __name__ == '__main__':
    main()



    


