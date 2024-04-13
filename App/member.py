from db_connect import db

class Member:
    @staticmethod
    def registerMember():
        try:
            conn = db.get_conn()
            cursor = conn.cursor()

            username = input("Enter a username: ")
            password = input("Enter a password: ")
            email = input("Enter a email: ")
            f_name = input("Enter your first name: ")
            l_name = input("Enter your last name: ")
            age = input("Enter your age: ")

            #Query
            cursor.execute('INSERT INTO Members (email, username, password, f_name, l_name, age) VALUES (%s, %s, %s, %s, %s, %s)', (email, username, password, f_name, l_name, age))
            conn.commit()

            print(username + " has been added to the database")
        except:
            print("Error with adding member")

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
            else: 
                print("Username or password is incorrect")
        except:
            print("Error has occurred. Try again.")
        

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
