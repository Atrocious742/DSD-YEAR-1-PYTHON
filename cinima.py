def movies():
    movie = ["minecraft movie 2", "fortnite movie", "toystory 5", "sonic 4", "incredibles 3"]
    print("dev menue")
    print("enter 1 to add a movie")
    print("enter 2 to remove a movie")
    print("enter 3 to find a movie ")
    print("enter 4 to exit")
    number = int(input("what option would you like to change:"))
    if number == 1:
        movie.append(input("what movie would you like to add:"))
        print(movie)
        movies()
    elif number == 2:
        print(movie)
        movie.remove("what movie would you like to remove.")
        movies()
    elif number == 3:
        print(movie)
        movies()
    elif number == 4:
        print("bye bye ")
        movies()
    else:
        print("bye bye ")
movies()