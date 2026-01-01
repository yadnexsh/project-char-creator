import random

from class_data import SUBCLASSES, LOADER

"""
SUBCLASSES = The list of all classes 
LOADER = Creates log / for debug
"""

divider = "--" * 20

def create_char():
    
    """
    Docstring for create_char
    In this func we are just creating character with instancing class method , in this func the count of char is getting controlled by instance_count
    Rest of the things are automated.
    """
    
    instance_count = 3
    
    print(divider)
    
    for each in range(instance_count):
        
        character = random.choice(SUBCLASSES)()
        
        print(f"Name > {character.char_name}")
        print(f"Class > {character.char_class}")
        print(f"Tier > {character.char_tier_name}")
        print(f"Gear > {character.char_gear}")
        
        for key, value in character.primary_stats.items():
            print(f"{key} > {value}")
            
        for key, value in character.secondary_stats.items():
            print(f"{key} > {value}")
        
        print(divider)
        
# create_char()

if __name__ == "__main__":
    
    print(divider)
    
    for each in LOADER:
        
        instance = each()
        
    create_char()