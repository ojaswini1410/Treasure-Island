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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#Write your code below this line 👇

choose_1 = input("Your at the cross road.\nWhere do you want to go, 'left' or 'right'?\n").lower()

if choose_1 == "left":
  choose_2 = input("You've come to a sea.There is an island in the middle of the sea.\nType 'swim' to swim across the sea or 'wait' to wait for the boat.\n").lower()
else:
  print("Opps! \nYou fell in the hole. \nGAME OVER!")

if choose_2 == "wait":
  choose_3 = input("You are successful in crossing the sea.\nYou reached the island unharmed.\nThere is a house with 3 doors 'red','yellow' and 'blue'.Which colour would you choose?\n").lower()
else:
  print("You are attacked by the crocodile.\nGAME OVER!")

if choose_3 == "red":
  print("It's a room full of fire.\nGAME OVER!")
elif choose_3 == "blue":
  print("You entered a room of beasts.\nGAME OVER!")

else:
  print("Congratulations!\nYou surpassed every obstacle and you found the treasure\nYOU WIN! ")

#End of program
#Sarthak and me















