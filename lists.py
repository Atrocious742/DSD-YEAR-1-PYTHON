energy_levels = ["sleep inertia" , "morning peak" , "afternoon slump" , "seccond wind" , "winding down"
                ]
usernames = ["Atrocious742" , "vipervipes189" , "TTV_Jake" , "XoptimalninjaX" , "TTVWest"
            ]
step_count = ["4000" , "1320" "2400" , "3200" , "100"
            ]

print(energy_levels)
print(usernames)
print(step_count)
print("........................................")
print(energy_levels[0])
print(energy_levels[len(energy_levels) // 2])
print(energy_levels[-1])
print("........................................")
print(usernames[0])
print(usernames[len(usernames) // 2])
print(usernames[-1])
print("........................................")
print(step_count[0])
print(step_count[len(step_count) // 2])
print(step_count[-1])

add_energy = energy_levels.append(input("what would you like to add to energy levels: "))
add_usernames = usernames.append(input("what would you like to add to usernames: "))
add_steps = step_count.append(input("what number of steps would you like to add to step count: ")) 

print(energy_levels)
print(usernames)
print(step_count)
print("........................................")
print(energy_levels[0])
print(energy_levels[len(energy_levels) // 2])
print(energy_levels[-1])
print("........................................")
print(usernames[0])
print(usernames[len(usernames) // 2])
print(usernames[-1])
print("........................................")
print(step_count[0])
print(step_count[len(step_count) // 2])
print(step_count[-1])