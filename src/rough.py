import random

def loop():
    for each in range(2):
        x = random.randint(1,10)
    return x

class v():

    
    def func_1(self):
        
        for each in range(3):
            x = loop()
            print(f"This is {x}")
        
    
class a(v):
    
    y = loop()
    def func_1(self):
        for each in range(3):
            print(f"This is {self.y}")
        
c = v()
c.func_1()