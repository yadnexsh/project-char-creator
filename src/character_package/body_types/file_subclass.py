
from base_body import body

class warrior(body):
    min_stat = 15
    max_stat = 65

    def __init__(self):
        gear = "Sword"
        super().__init__(gear=gear)

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