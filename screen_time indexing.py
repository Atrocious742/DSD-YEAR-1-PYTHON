screen_time = [120, 95, 140, 160, 80, 100, 200]
print(screen_time[2])

print("..............................")
average = (screen_time[0] + screen_time[1] + screen_time[2]) / 3
print(average)
print("..............................")
screen_time[-1] = int(input("enter the new digit at the end of the list: "))
print(screen_time)

print("...............................")
print(str(max(screen_time)), "is the new biggest number")
print("...............................")
print(str(min(screen_time)), "is the new smallest number")
