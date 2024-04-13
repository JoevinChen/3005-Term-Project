from db_connect import db
from member import Member
from trainer import Trainer
from admin import Admin

#test method
# def getTest(): 
#     try:
#         conn = db.get_conn()
#         cur = conn.cursor()
#         cur.execute('SELECT * FROM members')
#         rows = cur.fetchall()
#         for row in rows:
#             print(row)
#     except:
#         print("Error fetching data")

def initMenu():
    print("/////////////////////////////////////////")
    print("Please choose one of the following options:")
    print("1. Member Functions \n2. Trainer Functions \n3. Admin/Staff Functions \n4. Exit\n")

def signInMemberMenu():
    print("/////////////////////////////////////////")
    print("How can we help you?")
    print("1. Login \n2. Register \n3. Back\n")

# for trainer and admin
def signInSecondaryMenu():
    print("/////////////////////////////////////////")
    print("How can we help you?")
    print("1. Login \n2. Back\n")

# use global variable to track the signed in member/trainer/admin?
# def memberSignIn():

# def trainerSignIn():
#     print("/////////////////////////////////////////")

# def adminSignIn():
#     print("/////////////////////////////////////////")

#Registering a member
def memberRegistration():
    #Grabs user info
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter a email: ")
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    
    #Calls helper function
    Member.registerMember(email, username, password, f_name, l_name, age)
    print(username + " has been added to the database")

# #Inserts a new student record into the students table.
# def addStudent(first_name, last_name, email, enrollment_date):
#     try:
#         cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
#         connection.commit()
#     except psycopg2.errors.UniqueViolation:
#         print("Email already exists")
#     except:
#         print("Other error with adding student")

# #Updates the email address for a student with the specified student_id.
# def updateStudentEmail(student_id, new_email):
#     try: 
#         cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
#         connection.commit()
#     except psycopg2.errors.UniqueViolation:
#         print("Email already exists")
#     except:
#         print("Other error with updating email")

# #Deletes the record of the student with the specified student_id.
# def deleteStudent(student_id):
#     try:
#         cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
#         connection.commit()
#     except:
#         print("Error deleting student")

#code for user to interact with the database
def main():
    #testing Admin class
    Admin.displayAllClasses()
    Admin.displayAllEquipment()
    
    print("=========================================\n   Welcome to the Dawg's Fitness Club!   \n=========================================")
    # getTest()

    #add stuffs here
    while(True):
        initMenu()
        chosenOption = input("Enter choice: ")
        if chosenOption == "1":
            signInMemberMenu()
            memberOption = input("Enter choice: ")
            if memberOption == "1":
                print("\nChose login")
                #call sign in method then break (use another while loop for logged in user)
                Member.login()
            elif memberOption == "2":
                print("\nChose register")
                memberRegistration()

        elif chosenOption == "2":
            print("hi2")
            signInSecondaryMenu()
            trainerOption = input("Enter choice: ")
            if trainerOption == "1":
                print("\nChose login")
                #call sign in method then break (use another while loop for logged in user)
                Trainer.login()
            elif trainerOption == "2":
                print("\nBack")
                
        elif chosenOption == "3":
            print("hi3")
            signInSecondaryMenu()
            adminOption = input("Enter choice: ")
            if adminOption == "1":
                print("\nChose login")
                #call sign in method then break (use another while loop for logged in user)
                Admin.login()
            elif adminOption == "2":
                print("\nBack")
        elif chosenOption == "4":
            break
    
    # while(True):

main()