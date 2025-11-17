def menu():
    print("type 1 for med safty")
    print("type 2 for fittness centre")
    print("type 3 for sleep tracker")
    safty = int(input("what would you like to do:"))
    if safty == 1:
        med_safe_rule()
    elif safty == 2:
        fittness_center()
    elif safty == 3:
        sleep_tracker()
    else:
        menu()

def med_safe_rule():
    age = int(input("what is the patients age: "))
    weight = int(input("what is your weight in kg: "))
    if age >= 12 and weight >= 40:
        print("safe to give: ")
    else:
        print("not safe to give")
def fittness_center():
    print(" type 1 for yes")
    print("type 2 for no")
    med_clear = int(input("are your medical records clear: "))
    age2 = int(input("what is your age: "))
    if med_clear == 1 and age2 >= 18:
        print("you can accses the interactive zone")
    else:
        print("you do not have acsses to the interactive zone")
def sleep_tracker():
    heartrate = int(input("what is your current heartrate: "))
    sleep = input("are you asleep: ")
    if sleep == 'yes' and heartrate > 100:
        print("no alert")
    else:
        print("GET TO SLEEP BUDDY")
menu()
