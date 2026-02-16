
from gen_char.modules.character import Villager, Agile, Magic, Agile
from .rarity_tiers import Legendry, Epic, Rare, Common
import random

def rarity(char_type):
    
    roll = random.randint(1, 100)
    

    if char_type != "Villager" and roll <= 3:
        chosen_tier = Legendry
    elif char_type != "Villager" and roll <= 11:        
        chosen_tier = Epic
    elif roll <= 31:        
        chosen_tier = Rare
    else:
        chosen_tier = Common

    instance = chosen_tier()
    bonus = instance.gen_range()

    return chosen_tier.__name__, bonus