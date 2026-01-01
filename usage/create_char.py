import random
import sys
import os

cur_file_path = os.path.abspath(__file__)
package_path = os.path.abspath(cur_file_path + "/../../src/")

if package_path not in sys.path:
    sys.path.insert(0, package_path)

from gen_char.modules import ALL_CHARACTERS

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
        
        print(f"Name > {character.name}")
        print(f"Class > {character.char_class}")
        print(f"Tier > {character.tier_name}")
        print(f"Gear > {character.gear}")
        
        for key, value in character.primary_stats.items():
            print(f"{key} > {value}")
            
        for key, value in character.secondary_stats.items():
            print(f"{key} > {value}")
        
        print(divider)
        

#---------------------------------------------

if __name__ == "__main__":
    create_char()
