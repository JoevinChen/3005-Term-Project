#import psycopg2
from db_connect import db

# #Connect to database
# connection = psycopg2.connect(database="ASS3", user="postgres", password="postgres")
# cursor = connection.cursor()

# Test method (BUG!!!)
def getTest(): 
    try:
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute('SELECT * FROM trainer')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except:
        print("Error fetching data")

#def memberRegistration():




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

# Code for user to interact with the database
def main():
    print("===================================\nWelcome to the Dawg's Fitness Club!\n===================================\n")
    getTest()

    #add stuffs here
    while(True):
        chosenOption = input("1. Member Functions \n2. Trainer Functions \n3. Admin/Staff Functions \n4. Exit\n")
        if chosenOption == "1":
            print("hi")
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