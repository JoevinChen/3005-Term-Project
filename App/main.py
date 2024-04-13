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
#         print("Error fetching data")\

user_id = 0

def initMenu():
    print("/////////////////////////////////////////")
    print("Please choose one of the following options:")
    print("1. Member Functions \n2. Trainer Functions \n3. Admin/Staff Functions \n4. Exit\n")

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
            values = Member.signInMenu()
            if values[0] is True:
                user_id = values[1]
                break

        elif chosenOption == "2":
            values = Trainer.signInMenu()
            if values[0] is True:
                user_id = values[1]
                break

        elif chosenOption == "3":
            values = Admin.signInMenu()
            if values[0] is True:
                user_id = values[1]
                break

        elif chosenOption == "4":
            break
    
    # menuOptions = 
    #loop once logged in
    while(True):
        if chosenOption == "1":
            print("Member functions")
            print(user_id)
            break
        elif chosenOption == "2":
            print("Trainer functions")
            print(user_id)
            break
        elif chosenOption == "3":
            print("Admin functions")
            print(user_id)
            break
        elif chosenOption == "4":
            print("Exiting program")
            break
main()