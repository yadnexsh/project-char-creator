
import os
import json
from .file_mainbody import CharMainBody

# Importing Names and Gears from json files

src_dir = os.path.dirname(os.path.dirname(__file__))
character_data_dir = os.path.join(src_dir, "character_data")

gear_json_file = os.path.join(character_data_dir , "gears.json")
name_json_file = os.path.join(character_data_dir , "names.json")

try:
    
    with open(gear_json_file, "r") as file:
        GEARS = json.load(file)
        
except json.decoder.JSONDecodeError as e:
    print(f"{e}")
    
except Exception as e:
    print(f"{e}")
    
try:
    
    with open(name_json_file, "r") as file:
        NAMES = json.load(file)
        
except json.decoder.JSONDecodeError as e:
    print(f"{e}")
    
except Exception as e:
    print(f"{e}")
    
    
    
#------------------------------------------------------


class Villager(CharMainBody):
        
    secondary_stats = None
    class_gears_pool = None

    def __init__(self):
        super().__init__()
        self.char_class = self.__class__.__name__
        

class Melee(CharMainBody):
    
    class_stat_min = 10
    class_stat_max = 35
    secondary_stats = ["Armor", "Crit Chance"]
    class_gears_pool = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.char_class = self.__class__.__name__
        
        
class Magic(CharMainBody):
    
    class_stat_min = 20
    class_stat_max = 45
    
    secondary_stats = ["Mana", "Spell Crit"]
    class_gears_pool = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.char_class = self.__class__.__name__
        


class Agile(CharMainBody):
    
    class_stat_min = 30
    class_stat_max = 55
    
    secondary_stats = ["Evasion", "Attack Speed"]
    class_gears_pool = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.char_class = self.__class__.__name__
        
#----------------------------------------

def load():
    print(os.path.basename(__file__), "> Loaded sucessfully")

#----------------------------------------
if __name__ == "__main__":
    
    from file_mainbody import load
    load()