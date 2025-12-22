GEARS = {
    "Melee": [
        "Iron Sword",
        "Steel Axe",
        "Battle Hammer",
        "Longsword",
        "War Shield",
        "Chainmail Armor",
        "Plate Helmet",
        "Gauntlets",
        "Greaves",
        "Battle Axe"
    ],

    "Agile": [
        "Twin Daggers",
        "Short Bow",
        "Throwing Knives",
        "Light Leather Armor",
        "Hooded Cloak",
        "Boots of Swiftness",
        "Bracers",
        "Crossbow",
        "Rapier",
        "Smoke Bombs"
    ],

    "Magic": [
        "Magic Staff",
        "Wizard Hat",
        "Spellbook",
        "Robes of Power",
        "Enchanted Ring",
        "Crystal Orb",
        "Wand",
        "Amulet of Mana",
        "Potion Belt",
        "Cloak of Shadows"
    ]
}


x = GEARS["Melee"]
# print(x)
import random

y = random.choice(x)
print(y)

import json

with open(r"src\character_data\gears.json", "r") as file:
    GEARS = json.load(file)


x = GEARS["Melee"]
# print(x)
import random

y = random.choice(x)
print(y)