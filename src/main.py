import random
from class_data import SUBCLASSES, LOADER

# print(len(SUBCLASSES))
# print(SUBCLASSES)
# print(random.choice(SUBCLASSES))

divider = "--" * 20

def create_char():
    
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