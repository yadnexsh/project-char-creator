
import os
import random
import sys

cur_file_path = os.path.abspath(__file__)
print(cur_file_path)
# 
package_path = os.path.abspath(cur_file_path + "/../..")
print(package_path)

if package_path not in sys.path:
    sys.path.insert(0, package_path)
    
from config import load_config_data
GEARS , NAMES, state = load_config_data()

from .rarity import rarity

#------------------------------------------------------


class CharBase():
    """
    This class is creating  default char
    At base it will start with None values and Pre-defined primary stat names
    """
    
    char_class = None
    class_stat_min = 5
    class_stat_max = 30
    primary_stats_pool = ["Power", "Health", "Speed"]                   
    secondary_stats_pool = None
    class_gears_pool = None
    
    
    #-----------------
    def __init__(self):
        """
        In this func. on every instance of char (any class) , it will have Name , Tier , Primary Stats , [Related] Secondary Stats , Gear
        """
        
        self.name = random.choice(NAMES)
        self.tier_name , self.tier_bonus = rarity()
        self.primary_stats = self.gen_primary_stats()
        self.secondary_stats = self.gen_secondary_stats()
        self.gear = self.gen_gear()
        
    #-----------------
    def gen_primary_stats(self):
        """
        In this func. we are generating random integer for each primary stat from "primary_stats_pool"
        Further on based on the char's tier - we are giving char a bonus value in primary stat.
        Random int + Tier bonus = primary stat value
        """
        
        primary_stats = {}
    
        for each in self.primary_stats_pool:
            random_integer = random.randint(self.class_stat_min , self.class_stat_max)
            primary_stats[each] = random_integer + self.tier_bonus
            
        return primary_stats
    
    
    #-----------------
    def gen_secondary_stats(self):
        """
        In this func. we are generating random integer value for secondary stat.
        Secondary stat is getting selected on child class level - Based on child class it will have its corresponding sec stat.
        """
        
        secondary_stats = {}
    
        if not self.secondary_stats_pool:
            pass 
        else:
            for each in self.secondary_stats_pool:
                secondary_stats[each] = random.randint(self.class_stat_min , self.class_stat_max)
            
        return secondary_stats
    
    
    
    #-----------------
    def gen_gear(self):
        """
        Docstring for gen_gear
        
        :param self: Description:
        In this func. There is a pool of weapons in "gears.json" for each class. Program is choosing one weapon from corresponding class
        """
        
        if not self.class_gears_pool:
            pass  
        else:
            return random.choice(self.class_gears_pool)


#------------------------------------------------------

def load():
    print(os.path.basename(__file__), "> Loaded successfully")

#--------------------------------------------------------
    
if __name__ == "__main__":
    from rarity import load
    load()