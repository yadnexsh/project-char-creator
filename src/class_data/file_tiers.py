

# create 4 tiers - Common , Rare Epic Legendary


import random
import os

# Below base class , just creates range fun with default 0 values at start | Framework class

class Base():
    
    min_range = 0
    max_range = 0
    
    def gen_range(self):
        tier_range = random.randint(self.min_range , self.max_range)
        return tier_range

# Below classes are actual rarities/tiers of the character.

class Common(Base):
    min_range = 5
    max_range = 10
    
class Rare(Base):
    min_range = 10
    max_range = 20
    
class Epic(Base):
    min_range = 20
    max_range = 30
    
class Legendry(Base):
    min_range = 30
    max_range = 40
    

# This func. is choosing one tier for char , its based on percentage aka rarity.

def gen_tier():
    roll = random.randint(1, 100)

    if roll <= 3:
        chosen_tier = Legendry
    elif roll <= 11:        
        chosen_tier = Epic
    elif roll <= 31:        
        chosen_tier = Rare
    else:
        chosen_tier = Common

    instance = chosen_tier()
    bonus = instance.gen_range()

    return chosen_tier.__name__, bonus

#----------------------------------------

def load():
    print(os.path.basename(__file__), "> Loaded successfully")

#----------------------------------------

if __name__ == "__main__":
    bonus, tier_name = gen_tier()
    print(f"{bonus} > {tier_name}")
    