print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print('''You're at a cross road. Where do you want to go?
       Type "left or "right"''')
cross_road = input()
if cross_road == "left" or cross_road =="Left":
    print('''You're at a cross road.Where do you want to go?
             Type "wait" to wait for a boat. Type "swim to swim across.''')
    river = input()
    if river == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?")
        door = input()
        if door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue":
            print("Eaten by beast.\nGame Over.")
        else:
            print("Game Over.")

    elif river == "swim":
        print("Attacked by crocodile.\nGame Over.")
    else:
        print("You typed wrong input.")
elif cross_road == "right" or cross_road == "Right":
    print("You fell in a Hole.\nGame over.")
else:
    print("You typed wrong input.")