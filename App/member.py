from db_connect import db

class Member:
    @staticmethod
    def registerMember():
        try:
            conn = db.get_conn()
            cur = conn.cursor()

            username = input("Enter a username: ")
            password = input("Enter a password: ")
            email = input("Enter a email: ")
            f_name = input("Enter your first name: ")
            l_name = input("Enter your last name: ")
            age = input("Enter your age: ")

            #Query
            cur.execute('INSERT INTO Members (email, username, password, f_name, l_name, age) VALUES (%s, %s, %s, %s, %s, %s)', (email, username, password, f_name, l_name, age))
            conn.commit()
            print(username + " has been added to the database")

            cur.execute('SELECT member_id FROM Members WHERE username = %s', (username,))
            user_id_tuple = cur.fetchone()
            user_id = user_id_tuple[0]
            return (True, user_id)
        except:
            print("Error with adding member")
            return (False, 0)

    @staticmethod
    def login():
        try:
            conn = db.get_conn()
            cur = conn.cursor()

            username = input("Enter username: ")
            password = input("Enter password: ")

            cur.execute('SELECT * FROM Members WHERE username = %s AND password = %s', (username, password))
            rows = cur.fetchall()

            if len(rows) != 0:
                print("Welcome " + username)

                cur.execute('SELECT member_id FROM Members WHERE username = %s', (username,))
                user_id_tuple = cur.fetchone()
                user_id = user_id_tuple[0]
                return (True, user_id)
            else: 
                print("Username or password is incorrect")
                return (False, 0)
        except:
            print("Error has occurred. Try again.")
            return (False, 0)
    
    @staticmethod
    def signInMenu():
        print("/////////////////////////////////////////")
        print("How can we help you?")
        while(True): 
            print("1. Login \n2. Register \n3. Back\n")
            memberOption = input("Enter choice: ")
            if memberOption == "1":
                print("\nChose login")
                values = Member.login()

                #if login is successful, then return
                if values[0] is True:
                    return values
            elif memberOption == "2":
                print("\nChose register")
                values = Member.registerMember()

                #if register is successful, then return
                if values[0] is True:
                    return values
            elif memberOption == "3":
                print("\nBack")

                #if back is chosen, return false
                return (False, 0)

    def displayHealthMetric(member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM HealthMetric WHERE member_id = %s", (member_id))
            rows = cur.fetchall()
                
            print("\nHere are all your current health metrics: ")
            for member in rows:
                print(f"Member ID#:  {member[0]}")
                print(f"user weight:  {member[1]}")
                print(f"Height:  {member[2]}")
                print(f"bmi:  {member[3]}")
        except:
            print("Error has occured")
    
    def modifyHealthMetric (member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            user_weight = int(input("Enter your modifed or new weight (lbs): "))
            height = int(input("Enter your modifed or new height (cm): "))
            bmi = float(input("Enter your modifed or new bmi: "))

            cur.execute("UPDATE HealthMetric SET user_weight = %s, height = %s, bmi = %s WHERE member_id = %s", (user_weight, height, bmi, member_id))
            conn.commit()
            print("Updated")

        except:
            print("Error has occured")

    def displayPersonalInfo (member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Members WHERE member_id = %s", (member_id))
            rows = cur.fetchall()
                
            print("\nHere is your personal info: ")
            for member in rows:
                print(f"Email:  {member[1]}")
                print(f"Username:  {member[2]}")
                print(f"First Name:  {member[4]}")
                print(f"Last Name:  {member[5]}")
                print(f"Age:  {member[6]}")
        except:
            print("Error has occured")
    
    def modifyPersonalInfo(member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            email = (input("Enter your new email: "))
            f_name = input("Enter your new first name: ")
            l_name = input("Enter your new last name: ")
            age = int(input("Enter your new age: "))

            cur.execute("UPDATE Members SET email = %s, f_name = %s, l_name = %s, age = %s WHERE member_id = %s", (email, f_name, l_name, age, member_id))
            conn.commit()
            print("User info Updated")

        except:
            print("Error has occured")

