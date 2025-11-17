def calories():
    workout_time = int(input("how long was your workout: "))
    callories_permin = int(input("hoe many callories do you burn a minute: "))
    total_calories = callories_permin * workout_time
    print(total_calories)

def steps():
    total_steps = int(input("how many steps have you done: "))
    step_conver = total_steps / 1300
    print(step_conver)

def med_timing():
    total_min = int(input("how many minuets since last meds: "))
    total_timeh = total_min // 60
    total_timem = total_min % 60
    print(total_timeh, + total_timem)