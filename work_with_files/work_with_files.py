while 1:
    try:
        choice = int(input("0 -> Exit\n1 -> Add a player\n2 -> Read a file\n"))
        if(choice == 0):
            break
        elif(choice == 1):
            name = input("Enter the name of the player: ")
            team = input("Enter which team the player will play for: ")
            number = int(input("Enter on what number the player will play: "))
            fayl = open(f"{team}.txt", "a")
            fayl.write(f"{name}    {number}    {team}\n")
            fayl.close()
        elif(choice == 2):
            team = input("Enter which team the player played for: ")
            fayl = open(f"{team}.txt", "r")
            print(fayl.read())
            fayl.close()
        else:
            print("You entered an incorrect number!\n")
    except ValueError:
        print("Please enter only numbers!")