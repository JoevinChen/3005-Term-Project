from db_connect import db

class Trainer:
    @staticmethod
    def login():
        try:
            conn = db.get_conn()
            cur = conn.cursor()

            username = input("Enter username: ")
            password = input("Enter password: ")

            cur.execute('SELECT * FROM Trainer WHERE username = %s AND password = %s', (username, password))
            rows = cur.fetchall()

            if len(rows) != 0:
                print("Welcome " + username)
                return True
            else: 
                print("Username or password is incorrect")
                return False
        except:
            print("Error has occurred. Try again.")
            return False
    
    @staticmethod
    def signInMenu():
        print("/////////////////////////////////////////")
        print("How can we help you?")
        while(True): 
            print("1. Login \n2. Back\n")
            trainerOption = input("Enter choice: ")
            if trainerOption == "1":
                print("\nChose login")
                if Trainer.login() is True:
                    return True
            elif trainerOption == "2":
                print("\nBack")
                return False

    @staticmethod
    def memberProfileView():
        try:
            conn = db.get_conn()
            cur = conn.cursor()

            fname = input("Enter first name: ")
            lname = input("Enter last name: ")

            cur.execute('SELECT * FROM members WHERE f_name = %s AND l_name = %s', (fname, lname))
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except:
            print("Error fetching data")