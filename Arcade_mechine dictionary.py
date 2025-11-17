Arcade_mechine = {
    "pin ball wizard": {"catorgory": "pinball" , "status": "working"},
    "retro racer": {"catorgry": "racing" , "status": "needs matinence"}
}

def menue(Arcade_mechine):
    print("          MENU")
    print("1 to veiw all mechines")
    print("2 to add a new arcade mechine")
    print("3 to update a arcade mechines status")
    print("4 to delete a arcade mechine")
    print("5 to close the menue")
    option = int(input("what would you like to choose: "))
    if option == 1:
        print(Arcade_mechine)
        menue()
    elif option == 2:
            machine_name = input("What would you like to add: ")
            machine_category = input("What category is it: ")
            machine_status = input("What is the status of the machine: ")
            Arcade_mechine[machine_name] = machine_category , machine_status 
            print(Arcade_mechine)
    elif option == 3:
        name = input("Which machine do you want to update? ")
        if name in Arcade_mechine:
            new_status = input("Enter new status: ")
            Arcade_mechine[name]["status"] = new_status
            print(f"{name}'s status updated to '{new_status}'")
        else:
            print("Machine not found!")
        print(Arcade_mechine)
    elif option == 4:
         
         
menue(Arcade_mechine)
