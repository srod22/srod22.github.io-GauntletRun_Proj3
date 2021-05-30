#Project #3 - Object Oriented Game called Gauntlet Run
# Shanua Rodriguez
# April - May 2021
#Requirements: 
##Create multiple classes, and create multiple instances of each class
##Create complex `__init__` methods, which including instance variables set to default values, lists, and/or dictionaries
##Write custom instance methods and explain why they are used
##Know what a class is and why it is used

from gamelib import *
import random
import time


print("""         *********************           """)
print("""             GAUNTLET RUN          """)
print("""         *********************           """)
print("""     Program Created By Shanua Rodriguez """)

print("""\n****************************************************""")
gameContinue = "Y"
while gameContinue == "Y" or gameContinue == "y":
  choice = input("\nAre you sure you would like to continue? Y/N? ")
  if choice == "Y" or choice == "y":
    print("""\nWelcome to Gauntlet Run player! Your adventure awaits!""")
    time.sleep(2)

    name = input("\nWhat is your name player? ")
    character = int(input("\nAre you a warrior, rogue, mage, or a cleric? Enter 1-Warrior 2-Rogue 3-Mage or 4-Cleric "))
    partyType = int(input("\nThis is Gauntlet Run so there has to be at least 2 members to your party. Is it a Warrior - '1'? A Rogue - '2'? A Mage - '3'? Or A Cleric - '4'? Press the number for who you want to be as a part of your two member team. "))

    #applying input to the class
    player1 = Player(name, character, partyType)

    #assigning player information to specific upgrades
    player_Descrip1 = player1
    player_Descrip2 = player1
    player_Descrip3 = player1
    player_Descrip4 = player1

    if character == 1:
      player_Descrip1.warriorMod(character)
    elif character == 2:
      player_Descrip2.rogueMod(character)
    elif character == 3:
      player_Descrip3.mageMod(character)
    else:
      player_Descrip4.clericMod(character)
    
    #naming other members in the gauntlet room
    npc = DefaultNPC("Goku", partyType)
    enemy1 = Enemy("Nine Fingers")

    #check if enemy is a breakpoint
    enemy1.boss()

    #beginning battle
    encounter1 = Battle(player1, enemy1, npc)
    encounter1.attack()

    #check if player needs to heal
    player_Descrip1.heal()

  #Option for user to begin the story again or quit
    gameContinue = input("Want to play again? (Y/N): ")
  else:
    print("\n\nSorry that this isn't the right time. Maybe later.")
    break

input("""\n\nYou have reached the end of the program. If 
you have played Gauntlet Run, I hope you have enjoyed it. Press any key to end the program.""")