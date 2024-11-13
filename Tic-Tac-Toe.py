for Design1 in range(0,330):
    print("_",end="")
for Design2 in range(0,130):
    if(Design2==62):
        print("Welcome to the game:- 'Tic-Tac-Toe'",end="*")
    else:
        print("*",end="")
places_for_1=list()
places_for_2=list()
places_occupied=list()

Player1=(input("Enter name of Player1 : ")).title()
Player2=(input("Enter name of Player2 : ")).title()
choice1=(input("Enter choice for {0} [O or X] : ".format(Player1))).title()
while(1==1):
    if(choice1=="O"):
        choice2="X"
        break
    elif(choice1=="X"):
        choice2="O"
        break
    else:
        print("Enter only [O or X]")
        choice1=(input("Enter your choice : ")).title()
print("\n\nRules of the game are following : \n")
for x in range(1,12):
    for y in range(1,12):
        if(y%4==0 or x%4==0):
            print("#",end=" ")
        elif(x==2 and y==2):
            print("1",end=" ")
        elif(x==2 and y==6):
            print("2",end=" ")
        elif(x==2 and y==10):
            print("3",end=" ")
        elif(x==6 and y==2):
            print("4",end=" ")
        elif(x==6 and y==6):
            print("5",end=" ")
        elif(x==6 and y==10):
            print("6",end=" ")
        elif(x==10 and y==2):
            print("7",end=" ")
        elif(x==10 and y==6):
            print("8",end=" ")
        elif(x==10 and y==10):
            print("9",end=" ")
        else:
            print(" ",end=" ")
    print()
print("\nThis numbers 1 to 9 represents the all 9 places.\nPlease enter the number to choose the place\n")
number1=(input("Enter who will play first : ")).title()
while(1==1):
    if(number1==Player1 or number1=="Player1" or number1=="Player 1"):
        number1=Player1
        number2=Player2
        break
    elif(number1==Player2 or number1=="Player2" or number1=="Player 2"):
        number1=Player2
        number2=Player1
        break
    else:
        print("Please enter correct name or spelling.")
        number1=(input("Enter player's name from [{0} and {1}] : ".format(Player1,Player2))).title()
for x in range(5):
    place1=input("\nEnter your place {0} : ".format(number1))
    while(1==1):
        if(place1.isdigit()):
            place1=int(place1)
            if(place1 in places_for_1) or (place1 in places_for_2):
                print("This place is already occupied")
                place1=input("Enter another place rather than {0} : ".format(places_occupied))
            elif(place1>=1 and place1<=9):
                places_for_1.append(place1)
                break
            else:
                print("Please enter number of single digit from 0 to 9.")
                place1=input("\nEnter your place {0} : ".format(number1))
        else:
            print("Please enter only single digit numbers between 0 to 9")
            place1=input("\nEnter your place {0} : ".format(number1))
    places_occupied=places_for_2+places_for_1
    places_occupied.sort()
    if(1 in places_for_1) and (4 in places_for_1) and (7 in places_for_1):
        print("  |   #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("  |   #       #       ")
        print("# # # # # # # # # # # ")
        print("  |   #       #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("  |   #       #       ")
        print("# # # # # # # # # # # ")
        print("  |   #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("  |   #       #       ")
        print("\nHurray {0} won the match.".format(number1))
        break
    elif(2 in places_for_1) and (5 in places_for_1) and (8 in places_for_1):
        print("      #   |   #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #   |   #       ")
        print("# # # # # # # # # # # ")
        print("      #   |   #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #   |   #       ")
        print("# # # # # # # # # # # ")
        print("      #   |   #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #   |   #       ")
        print("\nHurray {0} won the match.".format(number1))
        break
    elif(3 in places_for_1) and (6 in places_for_1) and (9 in places_for_1):
        print("      #       #   |")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #   |   ")
        print("# # # # # # # # # # # ")
        print("      #       #   |   ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #   |   ")
        print("# # # # # # # # # # # ")
        print("      #       #   |   ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #   |")
        print("\nHurray {0} won the match.".format(number1))
        break
    elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
        print("      #       #       ")
        print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("\nHurray {0} won the match.".format(number1))
        break
    elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
        print("      #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("\nHurray {0} won the match.".format(number1))
        break
    elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
        print("      #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
        print("      #       #       ")
        print("\nHurray {0} won the match.".format(number1))
        break
    elif(1 in places_for_1) and (5 in places_for_1) and (9 in places_for_1):
        print("\     #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("    \ #       #       ")
        print("# # # # # # # # # # # ")
        print("      # \     #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #     \ #       ")
        print("# # # # # # # # # # # ")
        print("      #       # \     ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #     \ ")
        print("\nHurry {0} won the match.".format(number1))
        break
    elif(3 in places_for_1) and (5 in places_for_1) and (7 in places_for_1):
        print("      #       #   /")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       # /     ")
        print("# # # # # # # # # # # ")
        print("      #     / #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      # /     #       ")
        print("# # # # # # # # # # # ")
        print("    / #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("/     #       #       ")
        print("\nHurry {0} won the match.".format(number1))
        break
    else:
        print("      #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
    if(x==4):
        print("\nNo one won the match . It's a tie")
        break
    place2=input("\nEnter your place {0} : ".format(number2))
    while(1==1):
        if(place2.isdigit()):
            place2=int(place2)
            if(place2 in places_for_1) or (place2 in places_for_2):
                print("This place is already occupied")
                place2=input("Enter another place rather than {0} : ".format(places_occupied))
            elif(place2>=1 and place2<=9):
                places_for_2.append(place2)
                break
            else:
                print("Please enter number of single digit from 0 to 9.")
                place2=input("\nEnter your place {0} : ".format(number1))
        else:
            print("Please enter only single digit numbers between 0 to 9")
            place2=input("\nEnter your place {0} : ".format(number1))
    places_occupied=places_for_2+places_for_1
    places_occupied.sort()
    if(1 in places_for_2) and (4 in places_for_2) and (7 in places_for_2):
        print("  |   #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("  |   #       #       ")
        print("# # # # # # # # # # # ")
        print("  |   #       #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("  |   #       #       ")
        print("# # # # # # # # # # # ")
        print("  |   #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("  |   #       #       ")
        print("\nHurray {0} won the match.".format(number2))
        break
    elif(2 in places_for_2) and (5 in places_for_2) and (8 in places_for_2):
        print("      #   |   #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #   |   #       ")
        print("# # # # # # # # # # # ")
        print("      #   |   #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #   |   #       ")
        print("# # # # # # # # # # # ")
        print("      #   |   #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #   |   #       ")
        print("\nHurray {0} won the match.".format(number2))
        break
    elif(3 in places_for_2) and (6 in places_for_2) and (9 in places_for_2):
        print("      #       #   |")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #   |   ")
        print("# # # # # # # # # # # ")
        print("      #       #   |   ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #   |   ")
        print("# # # # # # # # # # # ")
        print("      #       #   |   ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #   |")
        print("\nHurray {0} won the match.".format(number2))
        break
    elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
        print("      #       #       ")
        print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("\nHurray {0} won the match.".format(number2))
        break
    elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
        print("      #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("\nHurray {0} won the match.".format(number2))
        break
    elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
        print("      #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
        print("      #       #       ")
        print("\nHurray {0} won the match.".format(number2))
        break
    elif(1 in places_for_2) and (5 in places_for_2) and (9 in places_for_2):
        print("\     #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("    \ #       #       ")
        print("# # # # # # # # # # # ")
        print("      # \     #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #     \ #       ")
        print("# # # # # # # # # # # ")
        print("      #       # \     ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #     \ ")
        print("\nHurry {0} won the match.".format(number2))
        break
    elif(7 in places_for_2) and (5 in places_for_2) and (3 in places_for_2):
        print("      #       #   /")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       # /     ")
        print("# # # # # # # # # # # ")
        print("      #     / #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      # /     #       ")
        print("# # # # # # # # # # # ")
        print("    / #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("/     #       #       ")
        print("\nHurry {0} won the match.".format(number2))
        break
    else:
        print("      #       #       ")
        if(1 in places_occupied) or (2 in places_occupied) or (3 in places_occupied):
            if(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (3 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 not in places_for_2) and (3 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and (3 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and(2 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(1 in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 not in places_for_2) and (2 not in places_for_1) and (3 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 in places_for_2) and (1 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 in places_for_2) and (3 not in places_for_2) and (1 not in places_for_1) and (3 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(1 in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and(2 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(1 not in places_for_2) and (2 not in places_for_2) and (3 in places_for_2) and (1 not in places_for_1) and (2 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(1 in places_for_1) and (2 in places_for_2) and (3 not in places_for_2) and (3 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_2) and (3 in places_for_2) and (2 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 not in places_for_2) and(3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 not in places_for_2) and (2 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 in places_for_1) and (1 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(1 not in places_for_1) and (2 in places_for_1) and (3 not in places_for_1) and (1 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(1 not in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (1 in places_for_2) and (2 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(1 in places_for_1) and (2 not in places_for_1) and (3 not in places_for_1) and (2 in places_for_2) and (3 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(1 not in places_for_1) and (3 in places_for_1) and (2 in places_for_2) and (1 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(1 in places_for_1) and (2 in places_for_1) and (3 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(1 in places_for_1) and (2 not in places_for_1) and (2 not in places_for_2) and (3 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(1 not in places_for_1) and (2 in places_for_1) and (1 not in places_for_2) and (3 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(4 in places_occupied) or (5 in places_occupied) or (6 in places_occupied):
            if(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (6 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 not in places_for_2) and (6 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and (6 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and(5 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(4 in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 not in places_for_2) and (5 not in places_for_1) and (6 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 in places_for_2) and (4 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 in places_for_2) and (6 not in places_for_2) and (4 not in places_for_1) and (6 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(4 in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and(5 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(4 not in places_for_2) and (5 not in places_for_2) and (6 in places_for_2) and (4 not in places_for_1) and (5 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(4 in places_for_1) and (5 in places_for_2) and (6 not in places_for_2) and (6 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_2) and (6 in places_for_2) and (5 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 not in places_for_2) and(6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 not in places_for_2) and (5 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 in places_for_1) and (4 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(4 not in places_for_1) and (5 in places_for_1) and (6 not in places_for_1) and (4 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(4 not in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (4 in places_for_2) and (5 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(4 in places_for_1) and (5 not in places_for_1) and (6 not in places_for_1) and (5 in places_for_2) and (6 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(4 not in places_for_1) and (6 in places_for_1) and (5 in places_for_2) and (4 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(4 in places_for_1) and (5 in places_for_1) and (6 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(4 in places_for_1) and (5 not in places_for_1) and (5 not in places_for_2) and (6 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(4 not in places_for_1) and (5 in places_for_1) and (4 not in places_for_2) and (6 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")
        print("# # # # # # # # # # # ")
        print("      #       #       ")
        if(7 in places_occupied) or (8 in places_occupied) or (9 in places_occupied):
            if(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_1):
                print("--{0}---#---{1}---#---{2}---".format(choice1,choice1,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (9 not in places_for_2):
                print("  {0}   #   {1}   #       ".format(choice1,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 not in places_for_2) and (9 not in places_for_2):
                print("  {0}   #       #       ".format(choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 not in places_for_2):
                print("      #   {0}   #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and (9 not in places_for_2):
                print("      #   {0}   #       ".format(choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and(8 not in places_for_2):
                print("  {0}   #       #   {1}   ".format(choice1,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 not in places_for_2):
                print("      #       #   {0}   ".format(choice1))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 in places_for_2):
                print("--{0}---#---{1}---#---{2}---".format(choice2,choice2,choice2))
            elif(7 in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice2,choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 not in places_for_2) and (8 not in places_for_1) and (9 not in places_for_1):
                print("  {0}   #       #       ".format(choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 in places_for_2) and (7 not in places_for_1):
                print("      #   {0}   #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 in places_for_2) and (9 not in places_for_2) and (7 not in places_for_1) and (9 not in places_for_1):
                print("      #   {0}   #       ".format(choice2))
            elif(7 in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and(8 not in places_for_1):
                print("  {0}   #       #   {1}   ".format(choice2,choice2))
            elif(7 not in places_for_2) and (8 not in places_for_2) and (9 in places_for_2) and (7 not in places_for_1) and (8 not in places_for_1):
                print("      #       #   {0}   ".format(choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice2))
            elif(7 in places_for_1) and (8 in places_for_2) and (9 not in places_for_2) and (9 not in places_for_1):
                print("  {0}   #   {1}   #       ".format(choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_2) and (9 in places_for_2) and (8 not in places_for_1):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 not in places_for_2) and(9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 not in places_for_2) and (8 in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 in places_for_1) and (7 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice2,choice1,choice1))
            elif(7 not in places_for_1) and (8 in places_for_1) and (9 not in places_for_1) and (7 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #".format(choice2,choice1))
            elif(7 not in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (7 in places_for_2) and (8 not in places_for_2):
                print("  {0}   #       #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice2,choice1))
            elif(7 in places_for_1) and (8 not in places_for_1) and (9 not in places_for_1) and (8 in places_for_2) and (9 not in places_for_2):
                print("  {0}   #   {1}   #   ".format(choice1,choice2))
            elif(7 not in places_for_1) and (9 in places_for_1) and (8 in places_for_2) and (7 not in places_for_2):
                print("      #   {0}   #   {1}".format(choice2,choice1))
            elif(7 in places_for_1) and (8 in places_for_1) and (9 in places_for_2):
                print("  {0}   #   {1}   #   {2}".format(choice1,choice1,choice2))
            elif(7 in places_for_1) and (8 not in places_for_1) and (8 not in places_for_2) and (9 in places_for_2):
                print("  {0}   #       #   {1}".format(choice1,choice2))
            elif(7 not in places_for_1) and (8 in places_for_1) and (7 not in places_for_2) and (9 in places_for_2):
                print("      #   {0}   #   {1}".format(choice1,choice2))
        else:
            print("      #       #       ")
        print("      #       #       ")