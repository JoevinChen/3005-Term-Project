from db_connect import db
from member import Member
from admin import Admin
from datetime import datetime

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
                print("\nWelcome " + username + "\n")

                cur.execute('SELECT trainer_id FROM Trainer WHERE username = %s', (username,))
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
                print("- Trainer Menu -")
                print("1. Login \n2. Back\n")
                trainerOption = input("Enter choice: ")
                if trainerOption == "1":
                    values = Trainer.login()

                    #if login is successful, then return
                    if values[0] is True:
                        return values
                elif trainerOption == "2":
                    print("\nBack")

                    #if back is chosen, return false
                    return (False, 0)
        except:
            print("Error has occurred. Try again.")
            return (False, 0)

    @staticmethod
    def memberProfileView():
        try:
            conn = db.get_conn()
            cur = conn.cursor()

            fname = input("Enter first name: ")
            lname = input("Enter last name: ")

            cur.execute('SELECT member_id FROM members WHERE f_name = %s AND l_name = %s', (fname, lname))
            rows = cur.fetchall()
            Member.dashboardDisplay(rows[0][0])
        except:
            print("Error fetching data")

    @staticmethod
    def checkTrainerTimeOverlap(date_available, start_time, end_time, trainer_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute(f'''SELECT COUNT(*) FROM availability as a WHERE 
                        trainer_id = %s
                        AND a.date_available = %s 
                        AND a.start_time >= %s
                        AND a.end_time <= %s''', (trainer_id, date_available, start_time, end_time))
            result = cur.fetchone()
            # print(result)
            if result:
                return result[0] == 0
        except Exception as e:
                print("Error! Try again.")

    @staticmethod
    def setTrainerAvailability(trainer_id):
        while True:
            try:
                if not(Admin.trainerExist(trainer_id)):
                    print(f"Trainer of ID {trainer_id} does not exist!")
                    break
       
                date = input(f"Enter your available date (YYYY-MM-DD): ")
                start_time = input(f"Enter your starting time (HH:MM:SS): ")
                end_time = input(f"Enter your ending time (HH:MM:SS): ")

                date = (datetime.strptime(date, "%Y-%m-%d")).date()
                start_time = (datetime.strptime(start_time, "%H:%M:%S")).time()
                end_time = (datetime.strptime(end_time, "%H:%M:%S")).time()

                if not(Trainer.checkTrainerTimeOverlap(date, start_time, end_time, trainer_id)):
                    conn = db.get_conn()
                    cur = conn.cursor()
                    cur.execute(f"UPDATE availability SET date_available = %s, start_time = %s, \
                                end_time = %s WHERE trainer_id = %s", (date, start_time, end_time, trainer_id))
                    conn.commit()
                    print("Updated trainer availibilty!")
                    break
                else:
                    print("Invalid input! Try again.")
            except Exception as e:
                print("Invalid input! Try again.")

    # @staticmethod
    # def checkTrainerAvailability():
    #     try:
    #         conn = db.get_conn()
    #         cur = conn.cursor()
    #         if Admin.trainerExist():

    #     except:
    #         pass