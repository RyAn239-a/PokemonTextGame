import random, time, sys

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
# pokemon battle game

# define the pokemon 
starterPokemon = [
    {"name": "Bulbasaur", "health": 45, "attack": 49, "defense": 49},
    {"name": "Squirtle", "health": 44, "attack": 48, "defense": 65},
    {"name": "Charmander", "health": 39, "attack": 52, "defense": 43}
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
typewriter(f"You have selected {starter["name"]} as your starter pokemon")

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
typewriter(f"Your starting location is the {location} region")

playerAlive = True
while playerAlive:
    encounter = wildPokemon[random.randint(0, 2)]
    print()
    typewriter(f"You have encountered a {encounter["name"]}")
    action = int(typewriterInput("Would you like to fight(1) or run away(2): "))
    if action == 1:
        damage = int(starter["attack"]/encounter["defense"] * (10) + random.randint(0, 10))
        typewriter(f"You have dealt {damage} damage to {encounter["name"]}")
        encounter["health"] = encounter["health"] - damage
        if encounter["health"] >= 0: 
            typewriter(f"{encounter["name"]} has died")
        else:
            typewriter(f"{encounter["name"]} has {encounter["health"]} health left")
    elif action == 2:
        continue
    quit()


