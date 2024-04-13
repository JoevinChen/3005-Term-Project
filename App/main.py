from db_connect import db
from member import Member
from trainer import Trainer
from admin import Admin

user_id = 0

def initMenu():
    print("/////////////////////////////////////////")
    print("Please choose one of the following options:")
    print("1. Member Functions \n2. Trainer Functions \n3. Admin/Staff Functions \n4. Exit\n")

#code for user to interact with the database
def main():
    #testing Admin class
    # Admin.displayAllClasses()
    # Admin.displayAllEquipment()
    
    print("=========================================\n   Welcome to the Dawg's Fitness Club!   \n=========================================")
    
    #testing
    # Admin.checkClassBookingAvailability('1', '2024-03-16', '10:00:00', '18:00:00')
    # print(Admin.trainerExist('1'))
    # Trainer.setTrainerAvailability('1')
    # Admin.updatePayment()

    #inital menu loop
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
            print("\nMember options:")
            while(True):
                print("\n1. Profile Management \n2. Dashboard Display \n3. Schedule Management \n4. Exit")
                memberOption = input("Enter choice: ")
                if memberOption == "1":
                    break
                elif memberOption == "2":
                    Member.dashboardDisplay(user_id)
                elif memberOption == "3":
                    break
                elif memberOption == "4":
                    break
            break
        elif chosenOption == "2":
            print("\nTrainer options:")
            while(True):
                print("\n1. Schedule Management \n2. Member Profile Viewing \n3. Exit")
                trainerOption = input("Enter choice: ")
                if trainerOption == "1":
                    Trainer.setTrainerAvailability()
                elif trainerOption == "2":
                    Trainer.memberProfileView()
                elif trainerOption == "3":
                    break
            break
        elif chosenOption == "3":
            print("\nAdmin options")
            while(True):
                print("\n1. Room Booking Management \n2. Equipment Maintenance Monitoring\n3. Class Schedule Updating \n4. Billing and Payment Management \n5. Exit")
                adminOption = input("Enter choice: ")
                if adminOption == "1":
                    break
                elif adminOption == "2":
                    while(True):
                        print("\n1. Display all equipment \n2. Update maintenance \n3. Add Equipment \n4. Remove Equipment \n5. Exit")
                        equipmentOption = input("Enter choice: ")
                        if equipmentOption == "1":
                            Admin.displayAllEquipment()
                        elif equipmentOption == "2":
                            Admin.updateEquipmentMaintenance()
                        elif equipmentOption == "3":
                            Admin.addEquipment()
                        elif equipmentOption == "4":
                            Admin.removeEquipment()
                        elif equipmentOption == "5":
                            break
                elif adminOption == "3":
                    while(True):
                        print("\n1. Display all bills \n2. Update payments \n3. Exit")
                elif adminOption == "4":
                    while(True):
                        print("\n1. Display all bills \n2. Update payments \n3. Exit")
                        billingOption = input("Enter choice: ")
                        if billingOption == "1":
                            Admin.displayAllBills()
                        elif billingOption == "2":
                            Admin.updatePayment()
                        elif billingOption == "3":
                            break
                elif adminOption == "5":
                    break
            break
        elif chosenOption == "4":
            print("Exiting program")
            break
main()