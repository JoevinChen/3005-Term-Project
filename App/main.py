from db_connect import db
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

def memberMenu():
    print("/////////////////////////////////////////")
    print("How can we help you?")
    print("1. Login \n2. Register \n3. A \n4. Back\n")

# might want to work on a sign in function in the Member class
# use global variable to track the signed in member/trainer/admin?
# def memberSignIn():

#frequently get "Error with adding member" with regular input (BUG)
def registerMember(username, password, email, f_name, l_name, age):
    conn = db.get_conn()
    cursor = conn.cursor()
    try:
        #Query
        cursor.execute('INSERT INTO Members (email, username, password, f_name, l_name, age) VALUES (%s, %s, %s, %s, %s, %s)', (email, username, password, f_name, l_name, age))
        conn.commit()
    except:
        print("Error with adding member")
    

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
    registerMember(email, username, password, f_name, l_name, age)
    print(username + " has been added to the database")

    return 




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
    initMenu()
    # getTest()

    #add stuffs here
    while(True):
        chosenOption = input("Enter choice: ")
        if chosenOption == "1":
            memberMenu()
            memberOption = input("Enter choice: ")
            if memberOption == "1":
                print("\nChose login")
            elif memberOption == "2":
                print("\nChose register")
                memberRegistration()

        elif chosenOption == "2":
            print("hi2")
        elif chosenOption == "3":
            print("hi3")
        elif chosenOption == "4":
            break


    # while(True):
    #     chosenOption = input("1. Get all students \n2. Add a student \n3. Update a student's email \n4. Delete a student \n5. Exit\n")
        
    #     if chosenOption == "1":
    #         getAllStudents()
    #     elif chosenOption == "2":
    #         first_name = input("Enter first name: ")
    #         last_name = input("Enter last name: ")
    #         email = input("Enter email: ")
    #         enrollment_date = input("Enter enrollment date: ")
    #         addStudent(first_name, last_name, email, enrollment_date)
    #     elif chosenOption == "3":
    #         student_id = input("Enter student id: ")
    #         new_email = input("Enter new email: ")
    #         updateStudentEmail(student_id, new_email)
    #     elif chosenOption == "4":
    #         student_id = input("Enter student id: ")
    #         deleteStudent(student_id)
    #     elif chosenOption == "5":
    #         break
    
    # #Closed when user exits
    # cursor.close()
    # connection.close()


main()