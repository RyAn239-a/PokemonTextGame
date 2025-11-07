# pokemon battle game
import random, time, sys, math

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
        answer = input()
        if answer == "E":
            inventoryWriter()
        else:
            return answer

# used to add in the lines to differentiate the inventory from gameplay
def inventoryWriter():
    print()
    typewriter("-----------------------------------------------")
    for line in inventory:
        typewriter(f"{line["item"]}: {line["quantity"]}")
    typewriter("-----------------------------------------------")
    print()

# define the pokemon
starterPokemon = [
    {"name": "Bulbasaur", "health": 45, "attack": 49, "defense": 49, "exp": 0, "level": 1},
    {"name": "Squirtle", "health": 44, "attack": 48, "defense": 65, "exp": 0, "level": 1},
    {"name": "Charmander", "health": 39, "attack": 52, "defense": 43, "exp": 0, "level": 1}
]

forestPokemon = [
    {"name": "Caterpie", "health": 45, "attack": 30, "defense": 35},
    {"name": "Pidgey", "health": 40, "attack": 45, "defense": 40},
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

# introduction 
typewriter("Welcome to the Pokémon Adventure!")
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
typewriter(f"1. {starterPokemon[0]["name"]}\n2. {starterPokemon[1]["name"]}\n3. {starterPokemon[2]["name"]}")
print()
starter = typewriterInput("Select 1, 2 or 3: ")
while starter not in ["1", "2", "3"]:
    starter = typewriterInput("Select 1, 2 or 3: ")
starter = starterPokemon[int(starter) - 1]
typewriter(f"You have selected {starter["name"]} as your starter pokémon.")

# create your lineup of pokemon and add pokemon that you catch to it
lineup = [
    {"pokemon": starter, "active": True}
    ]

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

playerAlive = True
while playerAlive:
    # track leveling up for this round
    starterLevel = starter["level"]

    # get random chance for there to be a fork in the path
    if random.randint(0,3) == 1:
        # user chooses but in actuality it is just random ahahahahahahahahahahahahahahaha
        fakeChoice = typewriterInput(f"You have encounteres a fork in the path. Will you go left or right: ").lower()
        while fakeChoice not in ["left", "right"]:
            fakeChoice = typewriterInput(f"You have encounteres a fork in the path. Will you go left or right: ").lower()
        
        # options for path based on your current location
        path_options = {
            "desert": ["mountain", "forest"],
            "mountain": ["desert", "forest"],
            "forest": ["desert", "mountain"]
        }
        newLocation = random.choice(path_options[location])

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

    # you encounter a wild pokemon
    encounter = wildPokemon[random.randint(0, 2)]
    print()
    typewriter(f"A wild {encounter["name"]} appears!")

    # while it is alive, do these actions
    encounterAlive = True
    while encounterAlive:
        # user chooses an option
        action = typewriterInput("Would you like to fight(1), run away(2), or catch(3): ")
        while action not in ["1", "2", "3"]:
            action = typewriterInput("Would you like to fight(1), run away(2), or catch(3): ")
        action = int(action)
        print()

        # attack action
        if action == 1:
            damage = int(starter["attack"]/encounter["defense"] * (10) + random.randint(0, 10))
            typewriter(f"You have dealt {damage} damage to {encounter["name"]}")
            encounter["health"] = encounter["health"] - damage
            if encounter["health"] <= 0:
                typewriter(f"{encounter["name"]} has died.")
                print()

                # level up the pokemon
                starter["exp"] += 50
                starter["level"] = int(100 * math.sqrt(starter["exp"]/100000))

                # if pokemon leveled up
                if starter["level"] > starterLevel:
                    levelup = starter["level"] - starterLevel
                    starter["health"] += 5 * levelup
                    starter["attack"] += 5 * levelup
                    starter["defense"] += 5 * levelup
                    typewriter(f"Your Pokémon has leveled up by {levelup}")
                    print()

                encounterAlive = False
                break
            else:
                typewriter(f"{encounter["name"]} has {encounter["health"]} health left.")
                print()

        # runaway action
        elif action == 2:
            runawayChance = random.randint(0, 2)
            if runawayChance != 2:
                typewriter("You successfully escaped battle.")
                print()
                encounterAlive = False
                # at the end of every round, when you kill the encounter, you get random loot
                loot = random.randint(1, 2)
                if loot == 1:
                 # get potion
                    inventory[0]["quantity"] += 1   
                    typewriter("You found a potion!")   
                else:
                    inventory[1]["quantity"] += 1    
                    typewriter("You found a pokéball!") 
                break
            else:
                typewriter("You failed to run away...")
                print()
        
        # catch action
        elif action == 3:
            continue
        # wild pokemon attacks you
        damage = int(encounter["attack"]/starter["defense"] * (10) + random.randint(0, 5))
        typewriter(f"{encounter["name"]} dealt {damage} damage to your pokémon")
        starter["health"] = starter["health"] - damage
        if starter["health"] <= 0:
            typewriter("Your pokémon has fainted... Game Over!")
            print()
            quit()
        else:
            typewriter(f"Your pokémon has {starter["health"]} health left.")
            print()

    print(f"***{starter["health"]}, {starter["attack"]}, {starter["defense"]}")
