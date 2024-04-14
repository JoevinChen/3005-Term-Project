from db_connect import db
from datetime import datetime

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

    #display all rooms currently booked
    def roomsBooked():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute('SELECT * FROM grouptraining JOIN room ON grouptraining.room_id = room.room_id')
            rooms = cur.fetchall()
            for room in rooms:
                print(f"Room {room[10]} is booked for {room[1]} on {room[4]} from {room[5]} to {room[6]}")
        except:
            print("Error fetching all rooms")

    #change a room for a class
    def changeRoom():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            class_id = input("Enter class ID: ")
            room_id = input("Enter new room ID: ")
            cur.execute('UPDATE GroupTraining SET room_id = %s WHERE class_id = %s', (room_id, class_id))
            conn.commit()
            print("Room changed")
        except:
            print("Error changing room")

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
    
    @staticmethod
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
    
    @staticmethod
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
    
    @staticmethod
    def classExist(class_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM grouptraining WHERE class_id = %s", (class_id))
            result = cur.fetchone()
            return bool(result)
        except:
            print("Error for classExist(). Try again.")
    
    @staticmethod
    def checkClassOverlap(date, start_time, end_time, room_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute(f'''SELECT COUNT(*) FROM grouptraining AS g WHERE 
                        room_id = %s 
                        AND g.date = %s 
                        AND g.start_time <= %s 
                        AND g.end_time >= %s''', (room_id, date, start_time, end_time))
            result = cur.fetchone()
            if result:
                return result[0] == 0  # True = no overlap, False = overlap
        except Exception as e:
                print("Error! Try again.")

    @staticmethod
    def updateClass():
        while True:
            try:
                class_id = input("Enter the class ID to update: ")
                if not(Admin.classExist(class_id)):
                    print(f"Class of ID {class_id} does not exist!")
                    break
                
                #gather info to update the class
                name = input("Enter name: ")
                max_capacity = input("Enter the max capacity: ")
                members_registered = input("Enter # of members registered: ")
                date = input(f"Enter the date (YYYY-MM-DD): ")
                start_time = input(f"Enter the starting time (HH:MM:SS): ")
                end_time = input(f"Enter the ending time (HH:MM:SS): ")
                room_id = input(f"Enter the room ID: ")
                trainer_id = input(f"Enter the trainer ID: ")

                date = (datetime.strptime(date, "%Y-%m-%d")).date()
                start_time = (datetime.strptime(start_time, "%H:%M:%S")).time()
                end_time = (datetime.strptime(end_time, "%H:%M:%S")).time()

                # check if same room_id start and end time overlap
                if (Admin.checkClassOverlap(date, start_time, end_time, room_id)):
                    conn = db.get_conn()
                    cur = conn.cursor()
                    cur.execute("UPDATE grouptraining SET name = %s, max_capacity = %s, members_registered = %s, \
                                    date = %s, start_time = %s, end_time = %s, room_id = %s, \
                                    trainer_id = %s WHERE class_id = %s", (name, max_capacity, members_registered, date, start_time, end_time, room_id, trainer_id, class_id))
                    conn.commit()
                    print("Updated trainer availibilty!")
                    break
                else:
                    print("Invalid input! Try again.")
            except Exception as e:
                print("Invalid input! Try again.")

    @staticmethod
    def trainerExist(trainer_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM trainer WHERE trainer_id = %s", (trainer_id,))
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

            memberID = input("Enter member's ID to update: ")
            cur.execute("SELECT COUNT(*) FROM members WHERE member_id = %s", memberID)
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