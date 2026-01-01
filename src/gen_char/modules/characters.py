
import os
from .char_base import CharBase

from config import load_config_data
GEARS , NAMES, state = load_config_data()

    
#------------------------------------------------------


class Villager(CharBase):
        
    secondary_stats = None
    class_gears_pool = None

    def __init__(self):
        super().__init__()
        self.char_class = self.__class__.__name__
        

class Melee(CharBase):
    
    class_stat_min = 10
    class_stat_max = 35
    secondary_stats = ["Armor", "Crit Chance"]
    class_gears_pool = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.char_class = self.__class__.__name__
        
        
class Magic(CharBase):
    
    class_stat_min = 20
    class_stat_max = 45
    
    secondary_stats = ["Mana", "Spell Crit"]
    class_gears_pool = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.char_class = self.__class__.__name__
        


class Agile(CharBase):
    
    class_stat_min = 30
    class_stat_max = 55
    
    secondary_stats = ["Evasion", "Attack Speed"]
    class_gears_pool = GEARS["Melee"]

    def __init__(self):
        super().__init__()
        self.char_class = self.__class__.__name__
        
#----------------------------------------

def load():
    print(os.path.basename(__file__), "> Loaded successfully")

#----------------------------------------
if __name__ == "__main__":
    
    from config import load
    load()