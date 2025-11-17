#arithmetic basics 

percent_of_steps = int(7345)
remaining_steps = int(10000)

percent_of_total_steps = percent_of_steps / remaining_steps
percent = percent_of_total_steps * 100 
print(percent)

#bmi buckets
weight = int(input("what is your weight in KG: "))
height = int(input("what is your height in meters: "))

bmi = height * 2
compute_bmi = bmi / weight
if compute_bmi <= 18.5:
    print("underweight")
elif compute_bmi <= 25:
    print("healthy")
elif compute_bmi <= 30:
    print("overweight")
else:
    print("obese")

#screen flag time
screen_time = int(input("what is your daly screen time: "))
steps = int(input("what is your steps today: "))
night_screen_time = int(input("what is your night screen time: "))
if (screen_time > 240) and (steps< 5000) or (night_screen_time > 60):
    print("flag user")
else:
    print("no flag")

#hydration streak
daily_water = int(input("how many ml have you drank today ML: "))
points = daily_water / 250 + daily_water / (2000 * 5)
print(points)


