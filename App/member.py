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
                print("\nWelcome " + username + "\n")

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
        try:
            print("/////////////////////////////////////////")
            print("How can we help you?")
            while(True):
                print("/////////////////////////////////////////")
                print("- Member Menu -")
                print("1. Login \n2. Register \n3. Back\n")
                memberOption = input("Enter choice: ")
                if memberOption == "1":
                    values = Member.login()

                    #if login is successful, then return
                    if values[0] is True:
                        return values
                elif memberOption == "2":
                    values = Member.registerMember()

                    #if register is successful, then return
                    if values[0] is True:
                        return values
                elif memberOption == "3":
                    print("\nBack")

                    #if back is chosen, return false
                    return (False, 0)
        except:
            print("Error has occurred. Try again.")
            return (False, 0)

    @staticmethod
    def displayHealthMetric(member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM HealthMetric WHERE member_id = %s", (member_id,))
            rows = cur.fetchall()
                
            print("\nHere are all your current health metrics: ")
            for member in rows:
                print(f"Member ID#:  {member[0]}")
                print(f"user weight:  {member[1]}")
                print(f"Height:  {member[2]}")
                print(f"bmi:  {member[3]}")
        except:
            print("Error has occured")
    
    @staticmethod
    def modifyHealthMetric(member_id):
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

    @staticmethod
    def displayPersonalInfo (member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Members WHERE member_id = %s", (member_id,))
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
    
    @staticmethod
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

    @staticmethod
    def modifyFitnessGoal(member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            weightGoal = int(input("Enter a new weight goal: "))
            newDate = input("Enter the date you will start this goal (ie. yyyy-mm-dd): ")

            cur.execute("UPDATE FitnessGoals SET weight_goal = %s, date_started = %s WHERE member_id = %s", (weightGoal, newDate, member_id))
            conn.commit()
            print("Goal Updated")

        except:
            print("Error has occured")
    
    @staticmethod
    def displayFitnessGoal(member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM FitnessGoals WHERE member_id = %s", (member_id,))
            rows = cur.fetchall()
                
            print("\nHere is your Fitness Goal: ")
            for member in rows:
                print(f"Target Weight:  {member[1]}")
                print(f"Date Started This Goal:  {member[2]}")
        except:
            print("Error has occured")

    @staticmethod
    def dashboardDisplay(member_id):
        conn = db.get_conn()
        cur = conn.cursor()

        Member.displayPersonalInfo(member_id)

        cur.execute("SELECT * FROM ExerciseRoutine WHERE member_id = %s", (member_id,))
        rows = cur.fetchall()
        print("\nHere are all your current exercise routines: ")
        for row in rows:
            print(row)

        print("\nHere are all your current achievements: ")
        cur.execute("SELECT * FROM Achievements WHERE member_id = %s", (member_id,))
        rows = cur.fetchall()
        for row in rows:
            print(row)

        Member.displayHealthMetric(member_id)

    @staticmethod
    def showOpenTimes():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Availability")
            rows = cur.fetchall()
                
            print("\nHere are all the available times ")
            for member in rows:
                print(f"Trainer's ID:  {member[0]}")
                print(f"Date Available:  {member[1]}")
                print(f"Start Time:  {member[2]}")
                print(f"End Time:  {member[3]}")
                print()
        except:
            print("Error has occured")

    @staticmethod
    def bookSession(member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            trainerID = input("Select which trainer's ID you would like to train with: ")
            startTime = input("Enter a starting time (make sure it is between the trainer's availbility (ie. 16:00:00) )")
            endTime = input("Enter a end time (make sure it is between the trainer's availbility (ie. 18:00:00) )")
            date = input("Enter The Date (make sure it is on a day a trainer is available) (ie. YYYY-MM-DD)")

            cur.execute(f'''SELECT trainer_id FROM Availability WHERE trainer_id = %s 
                        AND date_available = %s 
                        AND start_time <= %s 
                        AND end_time >= %s''', (trainerID, date, startTime, endTime))
            availability = cur.fetchone()
            
            if availability:
                cur.execute("INSERT INTO Trains (member_id, trainer_id, booking_start_time, booking_end_time, booking_date) VALUES (%s, %s, %s, %s, %s)", (member_id, trainerID, startTime, endTime, date))
                conn.commit()
                print("Training session booked")

                cur.execute("DELETE FROM Availability where trainer_id = %s", (trainerID))
                conn.commit()
                print("Trainer's availability been removed")                
            else:
                print("Not a valid time.")
        
        except:
            print("Error has occured")

    @staticmethod
    def showBookedSessions(member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Trains WHERE member_id = %s", (member_id,))
            rows = cur.fetchall()
                
            print("\nHere is your booked session: ")
            for member in rows:
                print(f"Trainer's ID:  {member[1]}")
                print(f"Booking Start Time:  {member[2]}")
                print(f"Booking end Time:  {member[3]}")
                print(f"Booking Date:  {member[4]}")
                print()

        except:
            print("Error has occured")

    def cancelBookedSession(member_id):
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            trainerID = int(input("Select which trainer's ID you would like to cancel: "))
            cur.execute("SELECT * FROM Trains where trainer_id = %s", (trainerID,))
            info = cur.fetchone()


            if info:
                startTime = info[2]
                endTime = info[3]
                date = info[4]
                cur.execute("INSERT INTO Availability (trainer_id, date_available, start_time, end_time) VALUES (%s, %s, %s, %s)", (trainerID, date, startTime, endTime))
                conn.commit()
                print("Trainer Availability back")
                cur.execute("DELETE FROM Trains WHERE member_id = %s AND trainer_id = %s", (member_id, trainerID))
                conn.commit()
                print("Session Cancelled")
            else:
                print("Not a valid session.")

        except:
            print("error")