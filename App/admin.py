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
                print("\nWelcome " + username + "\n")

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
        try:
            print("/////////////////////////////////////////")
            print("How can we help you?")
            while(True):
                print("/////////////////////////////////////////")
                print("- Admin Menu -")
                print("1. Login \n2. Back\n")
                adminOption = input("Enter choice: ")
                if adminOption == "1":
                    values = Admin.login()

                    #if login is successful, then return
                    if values[0] is True:
                        return values
                elif adminOption == "2":
                    print("\nBack")

                    #if back is chosen, return false
                    return (False, 0)
        except:
            print("Error has occurred. Try again.")
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

    @staticmethod
    def updateEquipmentMaintenance():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            equipment_id = input("Enter equipment ID: ")
            maintenance_status = input("Enter maintenance condition: ")
            maintenance_date = input("Enter maintenance date (YYYY-MM-DD): ")

            cur.execute('UPDATE equipment SET maintenance_status = %s, maintenance_date = %s WHERE equipment_id = %s', (maintenance_status, maintenance_date, equipment_id))
            conn.commit()
            print("Updated")
        except:
            print("Error fetching data")
    
    def addEquipment():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            equipment_name = input("Enter equipment name: ")
            maintenance_status = input("Enter maintenance condition: ")
            maintenance_date = input("Enter maintenance date (YYYY-MM-DD): ")

            cur.execute('INSERT INTO Equipment (equipment_name, maintenance_status, maintenance_date) VALUES (%s, %s, %s)', (equipment_name, maintenance_status, maintenance_date))
            conn.commit()
            print("Added")
        except:
            print("Error fetching data")

    def removeEquipment():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            equipment_id = input("Enter equipment ID: ")

            cur.execute('DELETE FROM Equipment WHERE equipment_id = %s', (equipment_id,))
            conn.commit()
            print("Removed")
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
            # print(result)
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
    
    @staticmethod
    def displayAllBills():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM payment")
            payments = cur.fetchall()

            for i in payments:
                print(f"Member ID: {i[0]}")
                print(f"    Bill reason: {i[1]}")
                print(f"    Billing fee: {i[2]}")
                print(f"    Amount paid: {i[3]}")

        except Exception as e:
            print("Error for updatePayment(). Try again.")

    @staticmethod
    def updatePayment():
        try:
            conn = db.get_conn()
            cur = conn.cursor()

            #validate inputted member ID
            memberID = input("Enter member's ID to update: ")
            cur.execute("SELECT COUNT(*) FROM members WHERE member_id = %s", memberID)
            member = cur.fetchone()
            # if member[0] == 0:
            #     print("Entered member ID is invalid!")
            # else:
            bill_reason = input("Reason for bill: ")
            
            try:
                billing_fee = int(input("Billing fee: "))
                amount_paid = int(input("Amount paid: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
            
            cur.execute(f'''INSERT INTO payment 
                        (member_id, bill_reason, billing_fee, amount_paid) VALUES (%s, %s, %s, %s)''', 
                        (memberID, bill_reason, billing_fee, amount_paid))
            conn.commit()
            print("Updated payment!")
                
        except Exception as e:
            print("Error for updatePayment(). Try again.")