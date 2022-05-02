import random
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Welcome to the ADventuture.")
choice1 = input("Please type 'W' to continue").lower()
if choice1 == 'w':
  print("I am your assistant. Please assign me a name.")
else:
  print("You should really pay attention. Please assign my callsign.")
robot1 = input("Type my name here.")
print(f"Command accepted. Agreed. I am {robot1}.")
choice2 = input("Do you have a callsign? Please type 'W' to attribute a callsign. If not please type any key.")
if choice2 == 'w':
  callsign1 = input("Insert your callsign here.")
  planet1 = "Neg2"
else:
  callsign1 = "Seven"
  print("I see. Yes then I will call you by your planet.")
  planet1 = input("Please enter the name of this planet.")
  print(f"Now we have association sorted, {planet1}.")
print(f"We have been here on {planet1} for less than 7.777 hours.")
print("According to my readings, you seem adequate. What is your background?")
background1 = input("Type 'T' for thief. Type 'E' for engineer. Type 'M' for musketbearer. Type 'A' for allrounder.").lower()
if background1 == 't':
  attack = 5
  defense = 3
  speed = 7
  hp = 5
  curHP = 5
  class1 = 'Thief'
  print("-----------------------------")
  print(f"You are {class1}.")
  print("-----------------------------")
  print(f"Your values are:\n [attack]{attack}\n[defense]{defense}\n [speed]{speed}\n [hp]{hp}")
elif background1 == 'e':
  attack = 3
  defense = 5
  speed = 5
  hp = 7
  curHP = 7
  class2 = 'Engineer'
  print("-----------------------------")
  print(f"You are {class2}.")
  print("-----------------------------")
  print(f"Your values are:\n [attack]{attack}\n[defense]{defense}\n[speed]{speed}\n[hp]{hp}")
elif background1 == 'm':
  attack = 7
  defense = 4
  speed = 5
  hp = 4
  curHP = 4
  class3 = 'Musketbearer'
  print("-----------------------------")
  print(f"You are {class3}.")
  print("-----------------------------")
  print(f"Your values are:\n [attack]{attack}\n[defense]{defense}\n[speed]{speed}\n[hp]{hp}")
elif background1 == 'a':
  attack = 5
  defense = 5
  speed = 5
  hp = 5
  curHP = 5
  class4 = 'Allrounder'
  print("-----------------------------")
  print(f"You are {class4}.")
  print("-----------------------------")
  print(f"Your values are:\n [attack]{attack}\n[defense]{defense}\n[speed]{speed}\n[hp]{hp}")
else:
  attack = 1
  defense = 9
  speed = 7
  hp = 3
  curHP = 3
  class5 = 'Aberrant'
  print("-----------------------------")
  print(f"You are {class5}.")
  print("-----------------------------")
  print(f"Your values are:\n [attack]{attack}\n[defense]{defense}\n[speed]{speed}\n[hp]{hp}")

print("-----------------------------")
enemyList = ["akaka", "nukni", "shawi"]

homebase = print(f"Now {callsign1} we need to get moving.")
choice7 = input("Type 'e' to explore.\nType 'r' to revitilize.\nType 't' to train.")
if choice7 == 'e':
  print(f"You encounter a {random.choice(enemyList)}.")
  if 'akaka':
    print("You encounter an akaka. It looks like a chicken with a large red feather on its back. It serves a minimal risk.")
    choice8 = input("Type 'a' to attack. Type 'r' to run.")
    if choice8 == 'a':
      print("You punch the akaka. He gets angry and runs away.")
    elif choice8 == 'r':
      input(choice7)
  elif 'nukni':
    print("You encounter a nukni. It looks like a boar with a large mossridden exterior. It serves a moderate risk.")
    choice8 = input("Type 'a' to attack. Type 'r' to run.")
    if choice8 == 'a':
      print("You punch the nukni. He gets angry and flies away.")
    elif choice8 == 'r':
      input(choice7)
  elif 'shawi':
    print("You encounter a shawi. It looks like a monkey with a tanned yellow hide. It is over 2 meters. It serves a detrimental risk.")
    choice8 = input("Type 'a' to attack. Type 'r' to run.")
    if choice8 == 'a':
      print(f"You punch the shawi. He gets angry and pommels {callsign1}.")
    elif choice8 == 'r':
      input(choice7)
    
elif choice7 == 'r':
  print(f"You restore your condition.")
  curHP = hp
  print(f"HP: {curHP}")
    
  

