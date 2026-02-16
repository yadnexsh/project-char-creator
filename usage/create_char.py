import random
import sys
import os

cur_file_path = os.path.abspath(__file__)
package_path = os.path.abspath(cur_file_path + "/../../src/")

if package_path not in sys.path:
    sys.path.insert(0, package_path)

from gen_char.modules import ALL_CHARACTERS
from gen_char.modules.rarity.rarity_tiers import rarity

divider = "--" * 20

# ----------------------------------------



def create_char():
    """
    Docstring for create_char
    Given code generates a character with instancing class method  class , where Name tier and the stats , gear related to class are getting auto assigned to char.
    The count of character you want to generate is getting controlled by instance_count , by default it's 3.
    """
    
    instance_count = 3
    
    print(divider)
    
    for each in range(instance_count):
        
        character = random.choice(ALL_CHARACTERS)()
        tier , bonus = rarity()

        while character.char_class == "Villager" and tier in ("Epic", "Legendry") :
            tier , bonus = rarity()
        
        

        print(f"Name > {character.name}")
        print(f"Class > {character.char_class}")
        print(f"Tier > {tier}")
        
        print(f"Gear > {character.gear}")
        
        for key, value in character.primary_stats.items():
            value = value + bonus
            print(f"{key} > {value}")
            
        for key, value in character.secondary_stats.items():
            print(f"{key} > {value}")
        
        print(divider)
        



#---------------------------------------------

if __name__ == "__main__":
    create_char()
