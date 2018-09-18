#I use a float number to indicate a position of the player. A while loop repeats until the player
#reaches the winning tile. If statments in the loop check the players location, print out the available directions
#to travel and ask for a new input telling where to travel next. In each location invalid commands make 
# an error message appear and force the player to choose again.

location = 1.1

while location != 3.1:
    print("Location: " + str(location))
    if location == 1.1:
        print("You can travel (N)orth.")
        direction = (input("Direction: "))  # remember that program should read direction as both caps and noncaps
        if direction.lower() == "n":
            location = round(location + 0.1, 2)
        elif direction.lower() != "n":
            #while loop that prompts the user for the correct input
            print("Not valid direction.")

    elif location == 1.2:
         print("You can travel (S)outh or (E)ast or (N)orth.")
         direction = (input("Direction: "))
         if direction.lower() == "n":
             location = round(location + 0.1, 2)
         elif direction.lower() == "s":
             location = round(location - 0.1, 2)
         elif direction.lower() == "e":
             location = round(location +1, 2)
         else:
            print("Not valid direction.")    

    elif location == 1.3:
            print("You can travel (E)ast or (S)outh.")
            direction = (input("Direction: "))
            if direction.lower() == "e":
                location = round(location +1, 2)
            elif direction.lower() == "s":
                location = round(location - 0.1, 2)
            else:
                print("Not valid direction.")

    elif location == 2.3:
        print("You can travel (W)est or (E)ast.")
        direction = (input("Direction: "))
        if direction.lower() == "w":
            location = round(location -1, 2)
        elif direction.lower() == "e":
            location = round(location +1, 2)
        else:
            print("Not valid direction")

    elif location == 2.2:
        print("You can travel (S)outh or (W)est.")
        direction = (input("Direction: "))
        if direction.lower() == "s":
            location = round(location -0.1, 2)
        elif direction.lower() == "w":
            location = round(location -1, 2)    
        else:
            print("Not valid direction") 

    elif location == 2.1:
        print("You can travel (N)orth.")
        direction = (input("Direction: "))
        if direction.lower() == "n":
            location = round(location +0.1, 2)
        else:
            print("Not valid direction")  

    elif location == 3.3:
        print("You can travel (W)est or (S)outh.")
        direction = (input("Direction: "))
        if direction.lower() == "w":
            location = round(location -1, 2)
        if direction.lower() == "s":
            location = round(location -0.1, 2)    
        else:
            print("Not valid direction")   

    elif location == 3.2:
        print("You can travel (N)ort or (S)outh.")
        direction = (input("Direction: "))
        if direction.lower() == "n":
            location = round(location +0.1, 2)
        if direction.lower() == "s":
            location = round(location -0.1, 2)    
        else:
            print("Not valid direction")  

    elif location == 3.1:
        print("You can travel (N)ort.")
        direction = (input("Direction: "))
        if direction.lower() == "n":
            location = round(location +0.1, 2) 
        else:
            print("Not valid direction")                                                                           
else:
    print("Victory!")