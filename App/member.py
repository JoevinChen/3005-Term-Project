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