def move_north(position):
    new_location = round(position + 0.1, 2)
    return new_location

def move_west(position):
    new_location = round(location -1, 2)
    return new_location

def move_south(position):
    new_location = round(location - 0.1, 2)
    return new_location

def move_east(position):
    new_location = round(location + 1, 2)
    return new_location





location = 1.1

while location != 3.1:
    if location == 1.1:
        print("You can travel: (N)orth.")

        direction = (input("Direction: ")) 
        while direction.lower() not in ['n']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "n":
            location = move_north(location)

    elif location == 1.2:
         print("You can travel: (N)orth or (E)ast or (S)outh.")
         direction = (input("Direction: "))
         while direction.lower() not in ['n', 's', 'e']:
            print("Not a valid direction!")  
            direction = (input("Direction: ")) 
         if direction.lower() == "n":
             location = move_north(location)
         elif direction.lower() == "s":
             location = move_south(location)
         elif direction.lower() == "e":
             location = move_east(location)

    elif location == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        direction = (input("Direction: "))
        while direction.lower() not in ['s', 'e']:
            print("Not a valid direction!")  
            direction = (input("Direction: ")) 
        if direction.lower() == "e":
            location = move_east(location)
        elif direction.lower() == "s":
            location = move_south(location)

    elif location == 2.3:
        print("You can travel: (E)ast or (W)est.")
        direction = (input("Direction: "))
        while direction.lower() not in ['w', 'e']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "w":
            location = move_west(location)
        elif direction.lower() == "e":
            location = move_east(location)

    elif location == 2.2:
        print("You can travel: (S)outh or (W)est.")
        direction = (input("Direction: "))
        while direction.lower() not in ['s', 'w']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "s":
            location = move_south(location)
        elif direction.lower() == "w":
            location = move_west(location)   

    elif location == 2.1:
        print("You can travel: (N)orth.")
        direction = (input("Direction: "))
        while direction.lower() not in ['n']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "n":
            location = move_north(location) 

    elif location == 3.3:
        print("You can travel: (S)outh or (W)est.")
        direction = (input("Direction: "))
        while direction.lower() not in ['s', 'w']:
            print("Not a valid direction!")
            direction = (input("Direction: ")) 
        if direction.lower() == "w":
            location = move_west(location)
        elif direction.lower() == "s":
            location = move_south(location)     

    elif location == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        direction = (input("Direction: "))
        while direction.lower() not in ['n', 's']:
            print("Not a valid direction!")
            direction = (input("Direction: "))
        if direction.lower() == "n":
            location = move_north(location)
        elif direction.lower() == "s":
            location = move_south(location)                                                                          
else:
    print("Victory!")