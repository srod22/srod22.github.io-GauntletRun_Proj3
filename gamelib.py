import random

class Player:
  player_list = []
  party_count = 0

  def __init__(self, name, characterChoice, numInParty):
    self.name = name
    self.characterChoice = characterChoice
    self.numInParty = numInParty
    self.level = random.randint(1, 3)
    self.attack = random.randint(10, 15)
    self.defense = random.randint(10, 15)
    self.max_health = random.randint(20, 25)
    self.max_magic = random.randint(0, 5)
    self.magic = self.max_magic
    self.health = self.max_health
    self.alive = True
    print("\nPlayer: " + self.name + " of Class: "+ str(self.characterChoice)+" \n  Level: " + str(self.level)+" \n  Attack: " + str(self.attack) + "\n  Defense: " + str(self.defense) + "\n  Maximum Health: " + str(self.max_health) + "\n  Maximum Magic: " + str(self.max_magic) +"\n\nThere are 2 members in your party including yourself.")

    Player.player_list.append(self)
    Player.party_count += self.numInParty

  def warriorMod(self, numInParty):
    self.numInParty = numInParty
    print("Since " + self.name + " is of the character class: Warrior then their health goes up by 15 and their attack and defense goes up by 10!\n") 
    self.health += 15
    self.attack += 10
    self.defense += 10
    print(self.name + " now has the following:\nHealth:" + str(self.health) + "\nAttack:"+str(self.attack)+"\nDefense: "+str(self.defense))

  def rogueMod(self, numInParty):
    self.numInParty = numInParty
    print("Since " + self.name + " is of the character class of Rogue, then their health goes down by 5 and their attack and defense goes down by 3!\n") 
    self.health -= 5
    self.attack -= 3
    self.defense -= 3
    print(self.name + " now has the following:\nHealth:" + str(self.health) + "\nAttack: "+str(self.attack)+"\nDefense: "+str(self.defense))

  def mageMod(self, numInParty):
    self.numInParty = numInParty
    print("Since " + self.name + " is of the character class of Mage, then their health goes down by 5 and their attack and defense goes down by 3! However, their magic goes up by 10!\n") 
    self.health -= 5
    self.attack -= 3
    self.defense -= 3
    self.max_magic +=10
    print(self.name + " now has the following:\nHealth:" + str(self.health) + "\nAttack: "+str(self.attack)+"\nDefense: "+str(self.defense)+"\nMagic: "+str(self.max_magic))

  def clericMod(self, numInParty):
    self.numInParty = numInParty
    print("Since " + self.name + " is of the character class of Cleric, then their health goes up by 10 and their attack and defense goes up by 5! Their magic also goes up by 5!\n") 
    self.health += 10
    self.attack += 5
    self.defense += 5
    self.max_magic +=5
    print(self.name + " now has the following:\nHealth:" + str(self.health) + "\nAttack: "+str(self.attack)+"\nDefense: "+str(self.defense)+"\nMagic:"+str(self.max_magic))

  def heal(self):
    if self.health <= 10 and self.magic >= 2:
      print("Player heals thy self! " + self.name + "'s health goes up by five!") 
      self.health += random.randint(5, 10)
      print(self.name + " now has " + str(self.health) + " health. ")

class DefaultNPC:
  player_list = []
  npc_count = 0

  def __init__(self, npcName, numInParty):
    self.numInParty = numInParty
    self.npcName = npcName
    self.max_health = random.randint(10, 15)
    self.health = self.max_health
    self.levelRogue = 2
    self.levelMage = 2
    self.levelWarrior = 2
    self.levelCleric = 2
    self.attackRogue = 10
    self.attackMage = 10
    self.attackCleric = 15
    self.attackWarrior = 20
    self.defenseRogue = 10
    self.defenseMage = 10
    self.defenseCleric = 15
    self.defenseWarrior = 20
    self.alive = True
    if self.numInParty == 1:
      DefaultNPC.npc_count += 2
      self.attack = self.attackWarrior
      self.defense = self.defenseWarrior
      print("\nIt is now you and another Warrior in the gauntlet room. They are at level: "+str(self.levelWarrior)+"\nAttack: "+str(self.attackWarrior)+"\nDefense: "+str(self.defenseWarrior)+"\nMaximum Health: "+str(self.max_health))
    if self.numInParty == 3:
      DefaultNPC.npc_count += 2
      self.attack = self.attackMage
      self.defense = self.defenseMage
      print("\nIt is now you and a Mage in the gauntlet room. They are at the following level:\nMage: "+str(self.levelMage)+"\nAttack: "+str(self.attackMage)+"\nDefense: "+str(self.defenseMage)+"\nMaximum Health: "+str(self.max_health))
    if self.numInParty == 2:
      DefaultNPC.npc_count += 2
      self.attack = self.attackRogue
      self.defense = self.defenseRogue
      print("\nIt is now you and a Rogue in the gauntlet room. They are at the following levels:\nRogue: "+str(self.levelRogue)+"\nAttack: "+str(self.attackRogue)+"\nDefense: "+str(self.defenseRogue)+"\nMaximum Health: "+str(self.max_health))
    if self.numInParty == 4: 
      DefaultNPC.npc_count += 2
      print("\nIt is now you and a Cleric in the gauntlet room. They are at the following level:\nCleric: "+str(self.levelCleric)+"\nAttack: "+str(self.attackRogue)+"\nDefense: "+str(self.defenseRogue)+"\nMaximum Health: "+str(self.max_health))

class Enemy:
  enemy_list = []
  enemy_count = 0

  def __init__(self, name):
    self.name = name
    self.level = random.randint(1, 4)
    self.attack = random.randint(5, 10)
    self.defense = random.randint(10, 15)
    self.max_health = random.randint(15, 20)
    self.health = self.max_health
    self.alive = True
    print("\nEnemy: " + self.name + " has entered the game. \nLevel: "+str(self.level)+"\nAttack: " + str(self.attack) + "\nDefense: " + str(self.defense) + "\nMaximum health: " + str(self.max_health) + ".\n")
    Enemy.enemy_list.append(self)
    Enemy.enemy_count += 1
    print("There are currently " + str(Enemy.enemy_count) + " enemy(enemies) in the gauntlet room.\n\n")

  def boss(self):
    if self.level == 4:
      print("A boss has entered the gauntlet room! " + self.name + "'s health goes up by five to ten points!") 
      self.health += random.randint(5, 10)
      print(self.name + " now has " + str(self.health) + " health. ")

class Battle:
  attackValue = 0

  def __init__(self, player, enemy, defaultNPC):
    self.player = player
    self.enemy = enemy
    self.defaultNPC = defaultNPC

  def attack(self):
   while ((self.player.health > 0) and (self.enemy.health > 0)):
      input("\nTo begin the gauntlet press enter. \n\n")
      print("Enemy's Health: " + str(self.enemy.health))
      print("Player's Health: " + str(self.player.health))
      print("NPC's Health: " + str(self.defaultNPC.health))

      print("\n----------------------------")
      print(self.player.name + " attempts to attack for ", self.player.attack, " damage!")
      attackValue = random.randint(0, self.player.attack)
      self.enemy.health -= attackValue

      #attack values for NPC
      if self.player.numInParty == 1:
        print(self.defaultNPC.npcName + " attempts to attack for ", self.defaultNPC.attackWarrior, " damage!")
        attackValue = random.randint(0, self.defaultNPC.attackWarrior)
        self.enemy.health -= attackValue
      elif self.player.numInParty == 2:
        print(self.defaultNPC.npcName + " attempts to attack for ", self.defaultNPC.attackRogue, " damage!")
        attackValue = random.randint(0, self.defaultNPC.attackRogue)
        self.enemy.health -= attackValue
      elif self.player.numInParty == 3:
        print(self.defaultNPC.npcName + " attempts to attack for ", self.defaultNPC.attackMage, " damage!")
        attackValue = random.randint(0, self.defaultNPC.attackMage)
        self.enemy.health -= attackValue
      elif self.player.numInParty == 4:
        print(self.defaultNPC.npcName + " attempts to attack for ", self.defaultNPC.attackCleric, " damage!")
        attackValue = random.randint(0, self.defaultNPC.attackCleric)
        self.enemy.health -= attackValue

      print(self.enemy.name, " attempts to attack you for ", self.enemy.attack, " damage!")
      attackValue = random.randint(0, self.enemy.attack)  
      self.player.health -= attackValue

      print(self.enemy.name, " attempts to attack ",self.defaultNPC.npcName," for ", self.enemy.attack, " damage!")
      attackValue = random.randint(0, self.enemy.attack)  
      self.defaultNPC.health -= attackValue

      print("\nEnemy's Health: " + str(self.enemy.health))
      print("Player's Health: " + str(self.player.health))
      print("NPC's Health: " + str(self.defaultNPC.health))

      #health values for unconcious NPC
      if self.player.numInParty == 1 and self.defaultNPC.health <= 0:
        print("The battle is almost over. Your default NPC by the name of " + self.defaultNPC.npcName + " is unconscious. It is just you left to fight.")
        self.defaultNPC.attackWarrior = 0
      elif self.player.numInParty == 2 and self.defaultNPC.health <= 0:
        print("The battle is almost over. Your default NPC by the name of " + self.defaultNPC.npcName + " is unconscious. It is just you left to fight.")
        self.defaultNPC.attackRogue = 0
      elif self.player.numInParty == 3 and self.defaultNPC.health <= 0:
        print("The battle is almost over. Your default NPC by the name of " + self.defaultNPC.npcName + " is unconscious. It is just you left to fight.")
        self.defaultNPC.attackMage = 0
      elif self.player.numInParty == 4 and self.defaultNPC.health <= 0:
        print("The battle is almost over. Your default NPC by the name of " + self.defaultNPC.npcName + " is unconscious. It is just you left to fight.")
        self.defaultNPC.attackCleric = 0
      
      #final comparisons between player and enemy
      if self.player.health <= 0:
        print("The battle is over. This story cannot continue without you. " + self.enemy.name + " wins.")
        self.player.alive = False
      elif self.enemy.health <= 0:
        print("Finally the battle is over, " + self.player.name + " wins.")
        self.enemy.alive = False  
      
 