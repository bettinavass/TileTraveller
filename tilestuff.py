#I use a float number to indicate a position of the player. A while loop repeats until the player
#reaches the winning tile. If statments in the loop check the players location, print out the available directions
#to travel and ask for a new input telling where to travel next. In each location invalid commands make 
# an error message appear and force the player to choose again.

location = 1.1

while location != 3.1:
    if location == 1.1:
        print("You can travel: (N)orth.")

        direction = (input("Direction: ")) 
        while direction.lower() not in ['n']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "n":
            location = round(location + 0.1, 2)

    elif location == 1.2:
         print("You can travel: (N)orth or (E)ast or (S)outh.")
         direction = (input("Direction: "))
         while direction.lower() not in ['n', 's', 'e']:
            print("Not a valid direction!")  
            direction = (input("Direction: ")) 
         if direction.lower() == "n":
             location = round(location + 0.1, 2)
         elif direction.lower() == "s":
             location = round(location - 0.1, 2)
         elif direction.lower() == "e":
             location = round(location + 1, 2)  

    elif location == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        direction = (input("Direction: "))
        while direction.lower() not in ['s', 'e']:
            print("Not a valid direction!")  
            direction = (input("Direction: ")) 
        if direction.lower() == "e":
            location = round(location + 1, 2)
        elif direction.lower() == "s":
            location = round(location - 0.1, 2)

    elif location == 2.3:
        print("You can travel: (E)ast or (W)est.")
        direction = (input("Direction: "))
        while direction.lower() not in ['w', 'e']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "w":
            location = round(location -1, 2)
        elif direction.lower() == "e":
            location = round(location +1, 2)

    elif location == 2.2:
        print("You can travel: (S)outh or (W)est.")
        direction = (input("Direction: "))
        while direction.lower() not in ['s', 'w']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "s":
            location = round(location -0.1, 2)
        elif direction.lower() == "w":
            location = round(location -1, 2)    

    elif location == 2.1:
        print("You can travel: (N)orth.")
        direction = (input("Direction: "))
        while direction.lower() not in ['n']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "n":
            location = round(location +0.1, 2)  

    elif location == 3.3:
        print("You can travel: (S)outh or (W)est.")
        direction = (input("Direction: "))
        while direction.lower() not in ['s', 'w']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "w":
            location = round(location -1, 2)
        elif direction.lower() == "s":
            location = round(location -0.1, 2)      

    elif location == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        direction = (input("Direction: "))
        while direction.lower() not in ['n', 's']:
            print("Not a valid direction!")
            direction = (input("Direction: "))
        if direction.lower() == "n":
            location = round(location +0.1, 2)
        elif direction.lower() == "s":
            location = round(location -0.1, 2)                                                                           
else:
    print("Victory!")