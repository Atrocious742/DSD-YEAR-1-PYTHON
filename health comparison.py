today = input("what day is it today:")
yesterday = input("what day was it yesterday: ")
def healthcomparison():
    print("what would you like to track")
    print("1 for steps")
    print("2 for glucose")
    ans = input("enter your selection here: ")
    if ans == '1':
        step_on_day_1 = input("What were your total steps on "+ today+ ": ")
        step_on_day_2 = input("What were your total steps on "+ yesterday+ ": ")
        if step_on_day_1 > step_on_day_2:
            print("You have walked more than yesterday")
        else:
            print("Get walking cause u walked more "+ yesterday +"than "+ today +", LAZY")
    elif ans == '2':
        glucose_today = input("What was your glucose "+ today)
        glucose_yesterday = input("What was your glucose on "+ yesterday)
        if glucose_today < glucose_yesterday:
            print("Welldone your glucose is going down.")
        else:
            print("YOU NEED TO GO EXERCISE FATTY🏃‍♂️🏃‍♂️🏃‍♂️🏃‍♂️🍔🍔🍔")
    else:
        print("INCORECT INFOMATION")
        healthcomparison()
healthcomparison()

