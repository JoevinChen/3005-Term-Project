from db_connect import db

class Member:
    @staticmethod
    def registerMember(username, password, email, f_name, l_name, age):
        try:
            conn = db.get_conn()
            cursor = conn.cursor()
            #Query
            cursor.execute('INSERT INTO Members (email, username, password, f_name, l_name, age) VALUES (%s, %s, %s, %s, %s, %s)', (email, username, password, f_name, l_name, age))
            conn.commit()
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