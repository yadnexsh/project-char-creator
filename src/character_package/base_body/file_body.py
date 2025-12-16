import random

NAMES = ["Aeron", "Nyx", "Zane", "Kira", "Vex", "Orin"]
# char_class = [warrior, mage, medic]

class body():
    
    min_stat = 5
    max_stat = 50
    stat_limit = 80
    god_stat = 95
    
    def __init__(self, gear,  is_god = False):
        self.name = random.choice(NAMES)
        self.char_class = random.choice(char_class)
        self.stats = self.generate_stats()
        self.gear = gear
        # self.list_class = list_class
        self.is_god = is_god
    
    def generate_stats(self):
        stats = ["Power", "Health", "Speed"]
        result = {}
        for each in stats:
            result[each] = random.randint(self.min_stat, self.max_stat)
        return result
            

    def show(self):
        print(f"Name > {self.name}")
        print(f"Class > {self.__class__.__name__}")
        print(f"---- Stats ----")
        for key, value in self.stats.items():
            print(f"{key} > {value}")
        print("---- * ----")
        print(f"Gear > {self.gear}")
        
        