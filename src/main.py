
import os
import random
import json



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
    core_stats = ["Power", "Health", "Speed"]
    sub_stats = None
    class_gears = None
    
    def __init__(self):
        self.name = random.choice(NAMES)
        self.core_stat = self.gen_core_stat()
        self.sub_stat = self.gen_sub_stat()
        self.gear = self.gen_gear()
    

    def gen_core_stat(self):
        core_result = {}
        for each in self.core_stats:
            core_result[each] = random.randint(self.min_stat , self.max_stat)
        return core_result
    
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
    
    sub_stats = ["Armor", "Crit Chance"]
    class_gears = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.type = self.__class__.__name__
        
        
class Magic(DefaultChar):
    
    min_stat = 20
    max_stat = 45
    
    sub_stats = ["Mana", "Spell Crit"]
    class_gears = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.type = self.__class__.__name__
        

class Agile(DefaultChar):
    
    min_stat = 30
    max_stat = 55
    
    sub_stats = ["Evasion", "Attack Speed"]
    class_gears = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.type = self.__class__.__name__

    
def show():
    
    types = [DefaultChar]           # any better way than adding main class in list ?
    all_child = DefaultChar.__subclasses__()
    for each in all_child:
        types.append(each)
    
    for each in range(3):
        char = random.choice(types)()
        
        print("--" * 20)
        
        print(f"Name > {char.name}")
        print(f"Class > {char.type}")
        
        print("--" * 5)
        
        for key, value in char.core_stat.items():
            print(f"{key} > {value}")
            
        for key, value in char.sub_stat.items():
            print(f"{key} > {value}")
            
        print(f"Gear > {char.gear}")
        
    print("--" * 20)




if __name__ == "__main__":
    show()