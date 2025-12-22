import random
from tabulate import tabulate

NAMES = ["Aeron", "Nyx", "Zane", "Kira", "Vex", "Orin"]
# classes = [warrior, mage, medic]

class body():
    
    min_stat = 5
    max_stat = 50
    stat_limit = 80
    is_god = False
    gear = None
    
    def __init__(self, gear):
        self.name = random.choice(NAMES)
        self.char_class = random.choice(classes)
        self.stats = self.generate_stats()
        self.gear = gear
        # self.list_class = list_class
        # self.is_god = is_god
        self.char_TYPE = "villager"
    
    def generate_stats(self):
        stats = ["Power", "Health", "Speed"]
        result = {}
        for each in stats:
            result[each] = random.randint(self.min_stat, self.max_stat)
        return result
            

    def show(self):

        headers = ["Name", "Class", "Gear"]
        values = [self.name, self.__class__.__name__, self.gear]

        print(tabulate([values], headers=headers, tablefmt="outline"))      #gpt 
        
        stats_table = []
        
        for key, value in self.stats.items():
            stats_table.append([key, value])


        print(tabulate(stats_table, headers=["Stat", "Value"], tablefmt="outline"))
    

god_min = 55
god_max = 85

mage_range = random.choice(range(15, 40))
medic_range = random.choice(range(25, 45))
warrior_range = random.choice(range(35, 50))

god_range = random.choice(range(god_min, god_max))
    
    
class warrior(body):
    self.class_Type = "Warrior"
    
    if random.choice(range(1, 100)) == 1:
        max_stat = min_stat = warrior_range
    else:
        min_stat = max_stat = god_range
        
    def __init__(self):
        gear = "Sword"
        super().__init__(gear=gear)
        
        

class mage(body):
    
    if random.choice(range(1, 100)) == 1:
        max_stat = min_stat = mage_range
    else:
        min_stat = max_stat = god_range

        
    def __init__(self):
        gear = "Wand"
        super().__init__(gear=gear)

class medic(body):
    
    if random.choice(range(1, 100)) == 1:
        max_stat = min_stat = medic_range
    else:
        min_stat = max_stat = god_range

    def __init__(self):
        gear = "Staff"
        super().__init__(gear=gear)
            

classes = [warrior, mage, medic]

def create_char():
    create_class = random.choice(classes)
    return create_class()


#------
sol1 = create_char() # warrior
sol2 = # knight
sol3 =# knight
sol4 = # archer
sol5 = # gmeneral
    command
    

char.show()