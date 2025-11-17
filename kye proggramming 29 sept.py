patient_name = "greg donaldson"
patient_age = 25
patient_hight = 6.2 
patient_weight = 70 

print("hello", patient_name, " you are in our data base as your aged", patient_age, "and your height is", patient_hight, "ft and your weight is", patient_weight, "kg")
change = (input("is you data correct: "))
if change == "yes":
     print("thank you for your data and its up to date.")
elif change == "no":
    patient_name = input("what is your name: ")
    patient_age = input("what is your new age:")
    patient_hight = input("what is your new height: ")
    patient_weight = input("what is your new weight: ")
    patient_confirm = input("hello", patient_name, " you are in our data base as your aged", patient_age, "and your height is", patient_hight, "ft and your weight is", patient_weight, "kg  is this data correct? ")
if patient_confirm == "yes":
     print("thank you for confirming your data is correct.")
elif change == "no":
     