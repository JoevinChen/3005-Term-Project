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
    print("=========================================\n   Welcome to the Dawg's Fitness Club!   \n=========================================")

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
    
    #loop once logged in
    while(True):
        if chosenOption == "1":
            print("/////////////////////////////////////////")
            print("Member options:")
            while(True):
                print("1. Profile Management \n2. Dashboard Display \n3. Schedule Management \n4. Exit")
                memberOption = input("Enter choice: ")
                if memberOption == "1":
                    while(True):
                        print("/////////////////////////////////////////")
                        print("1. Update Personal Info \n2. Fitness Goals \n3. Health Metrics \n4. Back")
                        profileOption = input("Enter choice: ")
                        if profileOption == "1":
                            Member.modifyPersonalInfo(user_id)
                        elif profileOption == "2":
                            while(True):
                                print("/////////////////////////////////////////")
                                print("1. View Fitness Goal \n2. Update Fitness Goal \n3. Back")
                                fitnessOption = input("Enter choice: ")
                                if fitnessOption == "1":
                                    Member.displayFitnessGoal(user_id)
                                elif fitnessOption == "2":
                                    Member.modifyFitnessGoal(user_id)
                                elif fitnessOption == "3":
                                    break
                        elif profileOption == "3":
                            while(True):
                                print("/////////////////////////////////////////")
                                print("1. Add/Modify Health Metrics \n2. View Health Metrics \n3. Back")
                                healthOption = input("Enter choice: ")
                                if healthOption == "1":
                                    Member.modifyHealthMetric(user_id)
                                elif healthOption == "2":
                                    Member.displayHealthMetric(user_id)
                                elif healthOption == "3":
                                    break
                        elif profileOption == "4":
                            break
                elif memberOption == "2":
                    Member.dashboardDisplay(user_id)
                elif memberOption == "3":
                    while(True):
                        print("/////////////////////////////////////////")
                        print("1. View Available Sessions \n2. View Booked Sessions \n3. Book a New Session \n4. Cancel a Session \n5. Back")
                        scheduleOption = input("Enter choice: ")
                        if scheduleOption =="1":
                            Member.showOpenTimes()
                        elif scheduleOption == "2":
                            Member.showBookedSessions(user_id)
                        elif scheduleOption == "3":
                            Member.bookSession(user_id)
                        elif scheduleOption == "4":
                            Member.cancelBookedSession(user_id)
                        elif scheduleOption == "5":
                            break
                elif memberOption == "4":
                    break
            break
        elif chosenOption == "2":
            print("/////////////////////////////////////////")
            print("Trainer options:")
            while(True):
                print("1. Schedule Management \n2. Member Profile Viewing \n3. Exit")
                trainerOption = input("Enter choice: ")
                if trainerOption == "1":
                    Trainer.setTrainerAvailability(user_id)
                elif trainerOption == "2":
                    Trainer.memberProfileView()
                elif trainerOption == "3":
                    break
            break
        elif chosenOption == "3":
            print("/////////////////////////////////////////")
            print("Admin options")
            while(True):
                print("/////////////////////////////////////////")
                print("1. Room Booking Management \n2. Equipment Maintenance Monitoring\n3. Class Schedule Updating \n4. Billing and Payment Management \n5. Exit")
                adminOption = input("Enter choice: ")
                if adminOption == "1":
                    while(True):
                        print("\n1. Show booked rooms \n2. Change room \n3. Back")
                        roomOption = input("Enter choice: ")
                        if roomOption == "1":
                            Admin.roomsBooked()
                        elif roomOption == "2":
                            Admin.changeRoom()
                        elif roomOption == "3":
                            break
                elif adminOption == "2":
                    while(True):
                        print("\n1. Display all equipment \n2. Update maintenance \n3. Add Equipment \n4. Remove Equipment \n5. Back")
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
                        print("\n1. Display all classes\n2. Update class \n3. Exit")
                        classOptions = input("Enter choice: ")
                        if classOptions == "1":
                            Admin.displayAllClasses()
                        if classOptions == "2":
                            Admin.updateClass()
                        if classOptions == "3":
                            break
                elif adminOption == "4":
                    while(True):
                        print("\n1. Display all bills \n2. Update payments \n3. Back")
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