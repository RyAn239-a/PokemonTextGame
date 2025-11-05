# pokemon battle game
import random, time, sys, math

# print and input like a typewriter
def typewriter(message, delay=0.02, end='\n'):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if end == '\n':
        print()

def typewriterInput(prompt, delay=0.02):
    typewriter(prompt, delay, end='')
    return input()

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

# introduction and get user to pick starting pokemon
typewriter("Get ready to begin your Pokemon Journey! \nBefore you begin you must select your starter pokemon:")
typewriter(f"1. {starterPokemon[0]["name"]}\n2. {starterPokemon[1]["name"]}\n3. {starterPokemon[2]["name"]}")
print()
starter = starterPokemon[int(typewriterInput("Select 1, 2 or 3: ")) - 1]
typewriter(f"You have selected {starter["name"]} as your starter pokemon.")

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
    # track leveling up
    starterLevel = starter["level"]

    # you encounter a wild pokemon
    encounter = wildPokemon[random.randint(0, 2)]
    print()
    typewriter(f"You have encountered a {encounter["name"]}.")

    # while it is alive, do these actions
    encounterAlive = True
    while encounterAlive:
        action = int(typewriterInput("Would you like to fight(1) or run away(2): "))
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
                starter["level"] = int(100 * math.sqrt(starter["exp"]/1000))

                # if pokemon leveled up
                if starter["level"] > starterLevel:
                    levelup = starter["level"] - starterLevel
                    starter["health"] += 5 * levelup
                    starter["attack"] += 5 * levelup
                    starter["defense"] += 5 * levelup

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
                break
            else:
                typewriter("You failed to run away...")
                print()

        # wild pokemon attacks you
        damage = int(encounter["attack"]/starter["defense"] * (10) + random.randint(0, 10))
        typewriter(f"{encounter["name"]} dealt {damage} damage to your pokemon")
        starter["health"] = starter["health"] - damage
        if starter["health"] <= 0:
            typewriter("Your pokemon has died.")
            print()
            quit()
        else:
            typewriter(f"Your pokemon has {starter["health"]} health left.")
            print()
