import random
from character_package import copy_classes

def create_char():
    create_class = random.choice(copy_classes)
    return create_class()

char = create_char()

char.show()