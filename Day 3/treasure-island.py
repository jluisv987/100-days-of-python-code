print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('Welcome to Treasure Island. Your mision is to find the treasure')
opt1=input("You are at a crossroad. Where do you want to go? Type 'left' or 'right' \n").lower()
if opt1 == "right":
    print ("You fell into a hole, GAME OVER")
else:
    opt2= input("You have come to a lake and there is an island in the middle. Type 'wait' to wait for a boat or 'swim' to swim to the island \n").lower()
    if opt2 == "wait":
        opt3= input("You arrive to the island and see a house with three doors (blue,red and yellow) what door should you open? \n").lower()
        if opt3 == "blue":
            print ("The blue door was a water trap with piranhas, GAME OVER")
        elif opt3 == "red":
            print ("The red door was a fire trap, GAME OVER")
        elif opt3 == "yellow":
            print ("You find the treasure chest. YOU WIN!")
        else:
            print("Invalid door name. GAME OVER")
    else:
        print("You got eaten by a hungry crocodile. GAME OVER")