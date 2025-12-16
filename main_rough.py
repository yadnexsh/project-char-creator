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
        print(f"God ? {self.is}")
    
    def god_roll():
        if random.choice(range(1, 100)) == 1:
            is_god = True
        

class warrior(body):
    min_stat = 15
    max_stat = 65

    def __init__(self):
        gear = "Sword"
        super().__init__(gear=gear)
        
        
# class warrior(body):
#     min_stat = 15
#     max_stat = 65
#     is_god = False
    
#     if random.choice(range(1, 100)) == 1:
#         is_god = True
        
#     if is_god:
#         min_stat = 35
#         max_stat = 95
#     else:
#         min_stat = 15
#         max_stat = 65
    
    
            
#     def __init__(self):
#         gear = "Sword"
#         is_god = is_god
#         super().__init__(gear=gear, is_god=is_god)
        
            
#     # if random.choice(range(1, 100)) == 1:
#     #     is_god = True                                         maybe put it in init ?


class mage(body):
    min_stat = 5
    max_stat = 55

    def __init__(self):
        gear = "Wand"
        super().__init__(gear=gear)

class medic(body):
    min_stat = 25
    max_stat = 65

    def __init__(self):
        gear = "Staff"
        super().__init__(gear=gear)
            

char_class = [warrior, mage, medic]

def create_char():
    create_class = random.choice(char_class)
    return create_class()

char = create_char()

char.show()