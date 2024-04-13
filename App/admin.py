from db_connect import db

class Admin:
    @staticmethod
    def login():
        try:
            conn = db.get_conn()
            cur = conn.cursor()

            username = input("Enter username: ")
            password = input("Enter password: ")

            cur.execute('SELECT * FROM Admins WHERE username = %s AND password = %s', (username, password))
            rows = cur.fetchall()

            if len(rows) != 0:
                print("Welcome " + username)

                cur.execute('SELECT admin_id FROM Admins WHERE username = %s', (username,))
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
            print("1. Login \n2. Back\n")
            adminOption = input("Enter choice: ")
            if adminOption == "1":
                print("\nChose login")
                values = Admin.login()

                #if login is successful, then return
                if values[0] is True:
                    return values
            elif adminOption == "2":
                print("\nBack")

                #if back is chosen, return false
                return (False, 0)

    #display all classes
    @staticmethod
    def displayAllClasses():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            query = 'SELECT * FROM grouptraining JOIN room ON grouptraining.room_id = room.room_id'
            cur.execute(query)
            classes = cur.fetchall()

            print("Here are all the group training classes:")
            if classes:
                for i in classes:
                    # print(i)
                    print(f"ID: {i[0]}")
                    print(f"    Group training name: {i[1]}")
                    print(f"    Max capacity: {i[2]}")
                    print(f"    Members registered: {i[3]}")
                    print(f"    Room number: {i[10]}")
                    print(f"    Date and time: {i[4]}: {i[5]} -> {i[6]}")
        except:
            print("Error fetching all classes")

    #monitor fitness equipment maintenance
    @staticmethod
    def displayAllEquipment():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            query = 'SELECT * FROM equipment'
            cur.execute(query)
            equipment = cur.fetchall()

            print("Here is all the equipment:")
            if equipment:
                for i in equipment:
                    # print(i)
                    print(f"ID: {i[0]}")
                    print(f"Equipment: {i[1]}\n"
                          f"    Maintenance condition: {i[2]}\n"
                          f"    Maintenance date: {i[3]}\n")
        except:
            print("Error fetching data")

    #checks if the group training date and time frame are available
    @staticmethod
    def checkClassBookingAvailability(room_id, date, start_time, end_time):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            query = '''
                        SELECT *
                        FROM grouptraining as g
                        INNER JOIN room as r ON g.room_id = r.room_id 
                        WHERE r.room_id = %s 
                        AND g.date = %s 
                        AND g.start_time >= %s
                        AND g.end_time <= %s
                    '''
            cur.execute(query, (room_id, date, start_time, end_time))
            result = cur.fetchone()
            print(result)
            if result:
                return result[0] == 0
        except:
            print("Error for class availability. Try again.")
    
    # #create personal training class
    # @staticmethod
    # def createPersonalTraining():
    #     while(True):
    #         try:
    #             trainer_fname = input("Enter first name: ")
    #             trainer_lname = input("Enter last name: ")

    @staticmethod
    def trainerExist(trainer_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            query = f"SELECT * FROM trainer WHERE trainer_id = %s"
            cur.execute(query, trainer_id)
            result = cur.fetchone()
            return bool(result)
        except:
            print("Error for trainerExist(). Try again.")