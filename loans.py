import time

loans = [
    {
        "loan_id": 1,
        "student_name": "Alex Green",
        "student_id": "S12345",
        "device_type": "Laptop",
        "device_id": "L-001",
        "date_out": "2025-11-24",
        "due_back": "2025-12-01",
        "returned": False
    },
    {
        "loan_id": 2,
        "student_name": "Alfie Becker",
        "student_id": "S67890",
        "device_type": "Laptop",
        "device_id": "L-002",
        "date_out": "2025-09-12",
        "due_back": "2025-12-01",
        "returned": False
    }
]

def menue():
    print("..................")
    print("WELCOME TO THE MENUE")
    print("..................")
    print("WHAT WOULD YOU LIKE TO DO ")
    print("..................")
    print("1 FOR A QUICK SEARCH")
    print("2 FOR ACCSES TO UPDATE THE DATA")
    print("3 TO DELETE THE RECORD WHEN LOAN WAS FINISHED OR ENTERED BY MISTAKE")
    print("4 TO ADD A NEW USER")
    print("5 TO EXIT THE MENUE")
    print("..................")
    option = int(input("WHAT NUMBER WOULD YOU LIKE TO DO: "))
    if option == 1:
        search()
    elif option == 2:
        update()
    elif option == 3:
        delete()
    elif option == 4:
        add()
    elif option == 5:
        print("exiting the menue")
        exit
    else:
        print("ERROR ENTERED, ENTER A CORRECT NUMBER")

def search():
    print("..................")
    print("ENTER THE NAME THAT YOU WOULD LIKE TO SEARCH")
    name = input("ENTER NAME HERE: ")
    found = False
    for loan in loans:
        if loan["student_name"].lower() == name.lower():
            print("VALID NAME ENTERED")
            print("..................")
            print("LOADING LOAN DEATAILS")
            print("..................")
            print("Loan details:")
            for key, value in loan.items():
                print(f"{key}: {value}")
            found = True
            break
    
    if not found:
        print("INVALID NAME, PLEASE TRY AGAIN")
    menue()

def update():
    print("..................")
    print("WHAT DATA WOULD YOU LIKE TO UDATE TODAY: ")
    name = input("ENTER USER NAME HERE: ")
    
    student_found = False
    for loan in loans:
        if loan['student_name'].lower() == name.lower():
            student_found = True
            print(f"STUDENT {name} FOUND, WHAT WOULD YOU LIKE TO UPDATE?")
            print("1. DEVICE TYPE")
            print("2.DEVICE ID")
            print("3. DATE OUT")
            print("4. DUE BACK")
            print("5. RETUREND SUFICENTLY")
            update_option = int(input("ENTER THE NUMBER TO THE COROSPONDING DATA: "))
            
            if update_option == 1:
                new_device_type = input("Enter new device type: ")
                loan['device_type'] = new_device_type
            elif update_option == 2:
                new_device_id = input("Enter new device ID: ")
                loan['device_id'] = new_device_id
            elif update_option == 3:
                new_date_out = input("Enter new date out (YYYY-MM-DD): ")
                loan['date_out'] = new_date_out
            elif update_option == 4:
                new_due_back = input("Enter new due back date (YYYY-MM-DD): ")
                loan['due_back'] = new_due_back
            elif update_option == 5:
                new_returned = input("Has the loan been returned? (True/False): ")
                loan['returned'] = new_returned.lower() == 'true'
            else:
                print("INVALLID OPTION")
            
            print("SUCSESFULLY UPDATED!")
            break
    
    if not student_found:
        print("STUDENT NAME NOT FOUND, TRY AGAIN")
    menue()
    
def delete():
    print("..................")
    print("WHICH USER WOULD YOU LIKE TO REMOVE")
    name = input("ENTER NAME HERE: ")
    student_found = False
    for loan in loans:
        if loan["student_name"].lower() == name.lower():
            student_found = True
            print(f"USER {name} IS BEING REMOVED IN...")
            final_check = input("ARE YOU SURE? (yes/no): ")
            
            if final_check.lower() == "yes":

                for i in range(5, 0, -1):
                    print(i)
                    time.sleep(1)  

                loans.remove(loan)
                print(f"USER {name} REMOVED")
            else:
                print("USER REMOVEL CANCLED.")
            break
    
    if not student_found:
        print("USER NOT FOUND. PLEASE TRY AGAIN.")
    menue()
def add():
    print("..................")
    loans.append = student_name = input("ENTER THE NAME OF THE STUDENT: ")
    loans.append = student_id = input("ENTER THE NEW STUDENTS ID: ")
    loans.append = device_type = input("ENTER THE NEW DEVICE TYPE: ")
    loans.append = device_id = input("ENTER THE NEW DEVICE ID: ")
    loans.append = date_out = input("ENTER THE DATE THE DEVICE WAS GIVEN OUT: ")
    loans.append = due_back = input("ENTER TGE DATE THE DEVICE IS DUE BACK: ")
    loans.append = returned = input("IS THE DEVICE IN YOUR POSSESION: ")
    print("DATA STORED")
    menue()
    
menue()