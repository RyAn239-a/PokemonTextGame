# pokemon battle game
import random, time, sys, math, copy

# print and input like a typewriter
def typewriter(message, delay=0.03, end='\n'):
    
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if end == '\n':
        print()

def typewriterInput(prompt, delay=0.03):
    while True:
        typewriter(prompt, delay, end='')
        answer = input().upper()
        if answer == "E":
            inventoryWriter()
        else:
            return answer

# used to add in the lines to differentiate the inventory from gameplay
def inventoryWriter():
    print()
    typewriter("Inventory:")
    typewriter("-----------------------------------------------")
    for line in inventory:
        typewriter(f"{line['item']} - {line['quantity']}")
    typewriter("-----------------------------------------------")
    print()

# define the pokemon
starterPokemon = [
    {"name": "Bulbasaur", "health": 60, "attack": 49, "defense": 49, "exp": 0, "level": 1},
    {"name": "Squirtle", "health": 44, "attack": 48, "defense": 65, "exp": 0, "level": 1},
    {"name": "Charmander", "health": 39, "attack": 60, "defense": 43, "exp": 0, "level": 1}
]

forestPokemon = [
    {"name": "Caterpie", "health": 45, "attack": 30, "defense": 35},
    {"name": "Pidgey", "health": 40, "attack": 40, "defense": 40},
    {"name": "Weedle", "health": 40, "attack": 35, "defense": 30}
]

mountainPokemon = [
    {"name": "Mankey", "health": 30, "attack": 60, "defense": 30},
    {"name": "Magnemite", "health": 25, "attack": 35, "defense": 70},
    {"name": "Clefairy", "health": 60, "attack": 45, "defense": 35}
]

desertPokemon = [
    {"name": "Diglett", "health": 10, "attack": 55, "defense": 25},
    {"name": "Sandshrew", "health": 50, "attack": 65, "defense": 30},
    {"name": "Eevee", "health": 45, "attack": 45, "defense": 45}
]

bossPokemon = {
    "name": "Gyarados",
    "health": 95,
    "attack": 125,
    "defense": 79
}
bossMoves = [
    {"name": "Waterfall", "power": 80},
    {"name": "Hurricane", "power": 110},
    {"name": "Dragon Pulse", "power": 85}
]

# introduction 
typewriter("Welcome to the Pokémon Adventure Game!")
userChoice = "A"
# inventory starts empty
inventory = [{"item": "Potions", "quantity": 0}, {"item": "Pokeballs", "quantity": 0}]
while userChoice != "C":
    userChoice = typewriterInput("Press (Q) to learn more about Pokémon, (C) to continue to the game, or (E) to access your inventory at any time: ").upper()
    if userChoice == "Q":
        typewriter("Welcome to the world of Pokémon! A Pokémon is a creature you can catch, train, and battle with on your adventure! \nYou will be able to explore regions, catch wild Pokémon, battle Pokémon, and use items to help you and your pokemon on your journey.")
        print()
    elif userChoice == "E":
        inventoryWriter()

# get user to pick starting pokemon
typewriter("Before you begin, select your starter pokémon:")
typewriter(f"1. {starterPokemon[0]['name']}\n2. {starterPokemon[1]['name']}\n3. {starterPokemon[2]['name']}")
print()
starter = typewriterInput("Select 1, 2 or 3: ")
while starter not in ["1", "2", "3"]:
    starter = typewriterInput("Select 1, 2 or 3: ")
starter = copy.deepcopy(starterPokemon[int(starter) - 1])
typewriter(f"You have selected {starter['name']} as your starter pokémon.")

#get random starting location and assign the wild pokemon accordingly to region
wildPokemon = []
location = random.randint(0, 2)
if location == 0:
    location = "forest"
    wildPokemon = forestPokemon
elif location == 1:
    location = "mountain"
    wildPokemon = mountainPokemon
else:
    location = "desert"
    wildPokemon = desertPokemon
typewriter(f"Your starting location is the {location} region.")

rounds = 0
playerAlive = True
visitedRegions = 1
while playerAlive:
    # track leveling up for this round
    starterLevel = starter["level"]

    # get random chance for there to be a fork in the path
    if random.randint(0,3) == 1 and rounds > 2:
        # if all three regions have been visited, then start BOSS battle. 
        if visitedRegions == 3:
            print()
            typewriter("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            typewriter("The ground trembles. Your final trial has awakened.")
            encounter = copy.deepcopy(bossPokemon)
            typewriter(f"{encounter['name']} appears!!!")
            typewriter("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()

            bossAlive = True
            while bossAlive:
                action = typewriterInput("Would you like to fight(1), use potion(2): ")
                while action not in ["1", "2"]:
                    action = typewriterInput("Would you like to fight(1), use potion(2): ")
                action = int(action)
                print()

                if action == 1:
                    # 1% chance the boss evades your attack
                    if random.randint(0,100) != 1:
                        damage = int(starter['attack']/encounter['defense'] * (10) + random.randint(0, 10))
                        typewriter(f"You have dealt {damage} damage to {encounter['name']}")
                        encounter['health'] = encounter['health'] - damage
                        if encounter['health'] <= 0:
                            typewriter(f"{encounter['name']} has died!!")
                            typewriter("Congratulations, you have beat the game!")
                            playerAlive = False
                            sys.exit()
                        else:
                            typewriter(f"{encounter['name']} has {encounter['health']} health left.")
                            print()
                    else:
                        typewriter(f"{encounter['name']} evaded your attack, it had no effect")
                        typewriter(f"{encounter['name']} has {encounter['health']} health left.")
                elif action == 2:
                    # potion usage
                    if inventory[0]["quantity"] == 0:
                        typewriter("You have no potions available for use")
                    else:
                        starter['health'] += 10
                        typewriter(f"You have used a potion. You pokémon has {starter['health']} health left")
                        # reduce number of pokeballs by 1 
                        inventory[0]["quantity"] -= 1
                    continue
                
                # boss pokemon attacks you ADD POWER INTO DAMAGE EQUATION
                damage = int(encounter['attack']/starter['defense'] * (10) + random.randint(0, 5))
                typewriter(f"{encounter['name']} uses {bossMoves[random.randint(0,2)]['name']} and deals {damage} damage to your pokémon")
                starter['health'] = starter['health'] - damage
                if starter['health'] <= 0:
                    typewriter("Your pokémon has been defeated... Game Over!")
                    playerAlive = False
                    print()
                    sys.exit()
                else:
                    typewriter(f"Your pokémon has {starter['health']} health left.")
                    print()         

        # user chooses but in actuality it is actually predetermined 
        fakeChoice = typewriterInput(f"You have encountered a fork in the path. Will you go left or right: ").lower()
        while fakeChoice not in ["left", "right"]:
            fakeChoice = typewriterInput(f"You have encountered a fork in the path. Will you go left or right: ").lower()
        
        # options for path based on your current location
        path_options = {
            "desert": "mountain",
            "mountain": "forest",
            "forest": "desert"
        }
        newLocation = path_options[location]

        # link the location to type of pokemon
        wildPokemon_map = {
            "desert": desertPokemon,
            "mountain": mountainPokemon,
            "forest": forestPokemon
        }

        # set the new values
        wildPokemon = wildPokemon_map[newLocation]
        location = newLocation
        typewriter("...............", delay=0.25)
        typewriter(f"You have made it to the {location} region!")
        visitedRegions += 1
        rounds = 0

    # random encounters/events
    randomEvent = random.randint(1,100)
    # random chance you encounter an abandoned wagon
    if 1 <= randomEvent <= 10 and rounds != 0:
        print()
        typewriter("You come across an abandoned wagon...")

        # user chooses to search or not
        userChoice = typewriterInput("Would you like to search it for items? (Y/N): ").upper()
        while userChoice not in ["Y", "N"]:
            userChoice = typewriterInput("Would you like to search it for items? (Y/N): ").upper()

        if userChoice == "Y":
            loot = random.randint(1, 4)
            if loot == 1:
                # get potion
                inventory[0]['quantity'] += 2 
                typewriter(">>> You found 2 potions!")
            elif loot == 2:
                # get pokeball
                inventory[1]['quantity'] += 2    
                typewriter(">>> You found 2 pokéballs!")
            elif loot == 3:
                # get 
                inventory[0]['quantity'] += 1
                inventory[1]['quantity'] += 1    
                typewriter(">>> You found a potion and a pokéball!")
            elif loot == 4:
                # get two of both
                inventory[0]['quantity'] += 2
                inventory[1]['quantity'] += 2    
                typewriter(">>> You found two potions and two pokéballs!")
        else:
            typewriter("You decided not to search the wagon and continue on the path.")

    # random chance to encounter a berry patch
    elif 11 <= randomEvent <= 20 and rounds != 0:
        print()
        # user chooses to eat or not
        userChoice = typewriterInput("You encounter a berry patch... Would you like to eat some berries? (Y/N): ").upper()
        while userChoice not in ["Y", "N"]:
            userChoice = typewriterInput("You encounter a berry patch. Would you like to eat some berries? (Y/N): ").upper()

        if userChoice == "Y":
            healAmount = random.randint(5, 10)
            starter['health'] += healAmount
            typewriter(f">>> You have eaten some berries and healed {healAmount} health. Your pokémon now has {starter['health']} health.")
        else:
            typewriter("You decided not to eat any berries and continue on the path.")
    
    # random chance to encounter a shimmering pond
    elif 21 <= randomEvent <= 30 and rounds != 0:
        print()
        typewriter("You come across a shimmering pond...")

        # user chooses to drink or not
        userChoice = typewriterInput("Would you like to drink from the pond? (Y/N): ").upper()
        while userChoice not in ["Y", "N"]:
            userChoice = typewriterInput("Would you like to drink from the pond? (Y/N): ").upper()
        
        if userChoice == "Y":
            boostChance = random.randint(1, 3)
            if boostChance == 1:
                starter['attack'] += 5
                typewriter(">>> You feel a surge of power!")
            elif boostChance == 2:
                starter['defense'] += 5
                typewriter(">>> You feel a surge of resilience!")
            elif boostChance == 3:
                starter['defense'] -= 10
                if starter['defense'] <= 0:
                    starter['defense'] = 1
                typewriter("You choke on the water and your defense lowers.")
        else:
            typewriter("You decide not to drink and continue on the path.")

    # random chance to encounter a collapsed den
    elif 31 <= randomEvent <= 40 and rounds != 0:
        print()
        typewriter("You stumble upon a collapsed den...")

        # user chooses to dig or not
        userChoice = typewriterInput("Would you like to dig through the rubble? (Y/N): ").upper()
        while userChoice not in ["Y", "N"]:
            userChoice = typewriterInput("Would you like to dig through the rubble? (Y/N): ").upper()
        
        if userChoice == "Y":
            lootChance = random.randint(1, 4)
            if lootChance == 1:
                inventory[0]['quantity'] += 1   
                typewriter(">>> You found a potion!")   
            elif lootChance == 2:
                inventory[1]['quantity'] += 1    
                typewriter(">>> You found a pokéball!") 
            elif lootChance == 3:
                typewriter(">>> You found nothing of value.")
            elif lootChance == 4:
                starter['health'] -= 10
                typewriter("The rubble collapses as you search. You lose 10 health.")
                if starter['health'] <= 0:
                    typewriter("Your pokémon has fainted... Game Over!")
                    playerAlive = False
                    sys.exit()
                else:
                    typewriter(f"Your pokémon now has {starter['health']} health.")
        else:
            typewriter("You decide not to dig and continue on the path.")

    # random chance to encounter a shrine
    elif 41 <= randomEvent <= 50 and rounds != 0:
        print()
        typewriter("You have found a mysterious shrine...")

        # user chooses to pray or not
        userChoice = typewriterInput("Would you like to pray at the shrine? (Y/N): ").upper()
        while userChoice not in ["Y", "N"]:
            userChoice = typewriterInput("Would you like to pray at the shrine? (Y/N): ").upper()
        
        if userChoice == "Y":
            typewriter("You feel a surge of energy flow through you...")
            starter['health'] += 10
            starter['attack'] += 10
            starter['defense'] += 10
            typewriter("** Your pokémon's stats have increased! **")
        else:
            typewriter("You leave the shrine and continue on the path.")
    
    # chance to encounter a pokemon center
    elif 51 <= randomEvent <= 60 and rounds != 0:
        print()
        typewriter("You see a Pokémon Center ahead...")

        # user chooses to enter or not
        userChoice = typewriterInput("Would you like to enter the Center? (Y/N): ").upper()
        while userChoice not in ["Y", "N"]:
            userChoice = typewriterInput("Would you like to enter the Center? (Y/N): ").upper()

        # if they enter heal them, if not continue    
        if userChoice == "Y":
            starter['health'] += 20
            typewriter(f"Your pokémon has been partially healed to {starter['health']} health")
        else:
            typewriter("You decide not to enter the Center and continue on the path.")

    # you encounter a wild pokemon
    encounter = copy.deepcopy(random.choice(wildPokemon))
    print()
    typewriter(f"=== A wild {encounter['name']} appears! ===")

    # while it is alive, do these actions
    encounterAlive = True
    while encounterAlive:
        # user chooses an option
        action = typewriterInput("Would you like to fight(1), run away(2), catch(3), or use potion(4): ")
        while action not in ["1", "2", "3", "4"]:
            action = typewriterInput("Would you like to fight(1), run away(2), catch(3), or use potion(4): ")
        action = int(action)
        print()

        # attack action
        if action == 1:
            damage = int(starter['attack']/encounter['defense'] * (10) + random.randint(0, 5))
            typewriter(f"You have dealt {damage} damage to {encounter['name']}")
            encounter['health'] = encounter['health'] - damage
            if encounter['health'] <= 0:
                typewriter(f"{encounter['name']} has died.")
                print()

                # level up the pokemon
                starter['exp'] += 50
                starter['level'] = int(100 * math.sqrt(starter['exp']/300000))

                # if pokemon leveled up
                if starter["level"] > starterLevel:
                    levelup = starter["level"] - starterLevel
                    starter['health'] += 5 * levelup
                    starter['attack'] += 5 * levelup
                    starter['defense'] += 5 * levelup
                    typewriter("** Your Pokémon has leveled up **")
                    print()
                
                # at the end of every round, when you kill the encounter, you get random loot
                loot = random.randint(1, 2)
                if loot == 1:
                    # get potion
                    inventory[0]['quantity'] += 1   
                    typewriter(">>> You found a potion!")   
                else:
                    inventory[1]['quantity'] += 1    
                    typewriter(">>> You found a pokéball!") 

                encounterAlive = False
                break
            else:
                typewriter(f"{encounter['name']} has {encounter['health']} health left.")
                print()

        # runaway action
        elif action == 2:
            runawayChance = random.randint(0, 2)
            if runawayChance != 2:
                typewriter("You successfully escaped battle.")
                encounterAlive = False
                break 
            else:
                typewriter("You failed to run away...")
                print()
        
        # catch action
        elif action == 3:
            # check for avaialable pokeballs 
            if inventory[1]['quantity'] == 0:
                typewriter("You have no pokéballs available for use")
            else:
                # reduce number of pokeballs by 1
                inventory[1]['quantity'] -= 1

                # chance that pokeball does not work
                if random.randint(1,2) == 2:
                    typewriter(f"You have used your pokéball... however, it had no effect.")
                else:
                     # display text if you catch it
                    typewriter(f"You have used your pokéball... and successfully caught {encounter['name']}")

                    # level up the pokemon
                    starter['exp'] += 50
                    starter['level'] = int(100 * math.sqrt(starter['exp']/100000))

                    # if pokemon leveled up
                    if starter["level"] > starterLevel:
                        levelup = starter["level"] - starterLevel
                        starter['health'] += 5 * levelup
                        starter['attack'] += 5 * levelup
                        starter['defense'] += 5 * levelup
                        typewriter("** Your Pokémon has leveled up **")
                    encounterAlive = False
                    break
            continue
            
        # potion usage
        elif action == 4:
            if inventory[0]['quantity'] == 0:
                typewriter("You have no potions available for use")
            else:
                starter['health'] += 10
                typewriter(f"You have used a potion. You pokémon has {starter['health']} health left")
                # reduce number of potions by 1 
                inventory[0]['quantity'] -= 1
            continue

        # wild pokemon attacks you
        damage = int(encounter['attack']/starter['defense'] * (10) + random.randint(0, 5))
        typewriter(f"{encounter['name']} dealt {damage} damage to your pokémon")
        starter['health'] = starter['health'] - damage
        if starter['health'] <= 0:
            typewriter("Your pokémon has fainted... Game Over!")
            print()
            playerAlive = False
            sys.exit()
        else:
            typewriter(f"Your pokémon has {starter['health']} health left.")
            print()

    # track rounds since last fork
    rounds += 1
