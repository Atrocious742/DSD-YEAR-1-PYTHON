def display():
    print("welcome to the display")
    games = ["minecraft", "call of duty bo2", "rocket leauge", "fortnite"]
    num_of_games = len(games)
    print("currently there are", num_of_games, "games that are in your library that are popular right now")
    print(games)
    favorite = input("what game would you like to favorite: ")
    if favorite == "minecraft":
        print("minecraft is now favorited")
    elif favorite  == "call of duty bo2":
        print("call of duty bo2 is now favorited")
    elif favorite == "rocket leauge":
        print("rocket leauge is now favorited")
    elif favorite == "fortnite":
        print("fortnite is now favorited")
    else:
        display()
    def lastplayed():
        last_played = input("what was the last game that you played: ")
        if last_played== "minecraft":
            print("minecraft is now marked as last played.")
        elif last_played  == "call of duty bo2":
            print("call of duty bo2 is now marked as last played.")
        elif last_played == "rocket leauge":
            print("rocket leauge is now marked as last played.")
        elif last_played == "fortnite":
            print("fortnite is now marked as last played.")
        else:
            lastplayed()
        new_game = input("is there any new games that you would like to add to your games library: ")
        if new_game == "yes":
            games.append(input("what game would you like to add: "))
            print(games)
        elif new_game == "no":
            print("okay thanks for using this display")
            
        else:
            print("there may be a game soon but currently your library consists of", games)
    lastplayed()
display()
