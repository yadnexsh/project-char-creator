
import os
import random
import json
from tiers import gen_tier
from tabulate import tabulate


src_dir = os.path.dirname(__file__)                                             # importing resource in file
resource_dir = os.path.join(src_dir, "resources")
gear_json = os.path.join(resource_dir , "gears.json")
name_json = os.path.join(resource_dir , "names.json")

try:
    with open(gear_json, "r") as file:
        GEARS = json.load(file)
except json.decoder.JSONDecodeError as e:
    print(f"{e}")
except Exception as e:
    print(f"{e}")
    
try:
    with open(name_json, "r") as file:
        NAMES = json.load(file)
except json.decoder.JSONDecodeError as e:
    print(f"{e}")
except Exception as e:
    print(f"{e}")
    





class DefaultChar():                                                # creating default char , which will be villager
    
    type = "Villager"
    min_stat = 5
    max_stat = 30
    list_of_stats = ["Power", "Health", "Speed"]                   
    sub_stats = None
    class_gears = None
    
    # tier_name , tier_bonus = gen_tier()
    
    def __init__(self):
        self.name = random.choice(NAMES)
        self.tier_name , self.tier_bonus = gen_tier()
        self.core_stats = self.gen_core_stat()
        self.sub_stat = self.gen_sub_stat()
        self.gear = self.gen_gear()
        

    def gen_core_stat(self):
        core_stats = {}
        for each in self.list_of_stats:
            gen_int = random.randint(self.min_stat , self.max_stat)
            core_stats[each] = gen_int + self.tier_bonus
        return core_stats
    
    def gen_sub_stat(self):
        sub_result = {}
        
        if self.sub_stats == None:
            pass 
        else:
            for each in self.sub_stats:
                sub_result[each] = random.randint(self.min_stat , self.max_stat)
                
        return sub_result
    
    def gen_gear(self):
        if self.class_gears == None:
            pass  
        else:
            return random.choice(self.class_gears)                       # define here cause we want per char not per class

class Melee(DefaultChar):
    
    min_stat = 10
    max_stat = 35
    # tier_name , tier_bonus = gen_tier()
    sub_stats = ["Armor", "Crit Chance"]
    class_gears = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.type = self.__class__.__name__
        
        tier_name , tier_bonus = gen_tier()
        
        for each in self.core_stats:
            new_value = self.core_stats[each] + tier_bonus
            self.core_stats[each] = new_value

            
            
        
        
class Magic(DefaultChar):
    
    min_stat = 20
    max_stat = 45
    
    sub_stats = ["Mana", "Spell Crit"]
    class_gears = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.type = self.__class__.__name__
        
        tier_name , tier_bonus = gen_tier()
        
        for each in self.core_stats:
            new_value = self.core_stats[each] + tier_bonus
            self.core_stats[each] = new_value

            

class Agile(DefaultChar):
    
    min_stat = 30
    max_stat = 55
    
    sub_stats = ["Evasion", "Attack Speed"]
    class_gears = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.type = self.__class__.__name__
        
        tier_name , tier_bonus = gen_tier()
        
        for each in self.core_stats:
            new_value = self.core_stats[each] + tier_bonus
            self.core_stats[each] = new_value

            
    
def show():
    
    types = [DefaultChar]           # any better way than adding main class in list ?
    all_child = DefaultChar.__subclasses__()
    for each in all_child:
        types.append(each)
    
    for each in range(3):
        char = random.choice(types)()
        # print(char)
        
        print("--" * 20)
        
        print(f"Name > {char.name}")
        print(f"Class > {char.type}")
        print(f"Tier > {char.tier_name}")
        print(f"Gear > {char.gear}")
        print("--" * 5)
        
        for key, value in char.core_stats.items():
            print(f"{key} > {value}")
            
        for key, value in char.sub_stat.items():
            print(f"{key} > {value}")
            
        

    print("--" * 20)
    return char.tier_bonus , char.tier_name

if __name__ == "__main__":
    tier_bonus , tier_name = show()
    # print(f"{tier_bonus}, {tier_name}")