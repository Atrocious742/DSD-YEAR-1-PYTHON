songs = input("what are your top 5 favourite songs "). split()
#list and print your top 5 songs.  
top5 = [songs]
print(top5)
def songadditionordeletion():
    print("would you like to add a song:")
    print("1 for add song")
    print("2 for delete song ")
    add = int(input("1 or 2: "))
    if add == 1:
        top5.append(input("what song would you like to add: "))
        print(top5)
        songadditionordeletion()
    elif add == 2:
        top5.remove(input("what is there number  "))
        