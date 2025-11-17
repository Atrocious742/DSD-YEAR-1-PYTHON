hourspernight = int(input("How many hours per night do you sleep? "))

hoursperweek = hourspernight * 7

print ("You sleep",hoursperweek,"hours per week") 



dayspermonth = int((hourspermonth)) / 24

print ("This equates to",dayspermonth,"days per month")





word = input("Input a word to reverse it:  ")

for char in range(leng(word) -1, -1, -1):

print (word[char], end="")


fahrenheight = celsius * 1.8 +32 

celsius = 37.5

fahrenheit = (celsius * 1.8) + 32

print ("%0.1f degree Celsius is equil to %0.1 degree fahrenheit" %(celsius, fahrenheit))




def calculate(last, secondlast):
        next = last + seccondlast
        if next > 50:
                 return
        else:
                 print(next + " "
                 count += 1
                 calculate(next, last, index)

print("1 ")
calculate(1, 0)
print("\n")