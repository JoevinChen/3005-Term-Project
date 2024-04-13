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
                Member.registerMember()

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
    
    # menuOptions = 
    #loop once logged in
    while(True):
        pass

main()