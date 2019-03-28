from numpy.random import *

def return_ransu(name):
    if name == "野田総理":
        a = randint(1, 6)
    elif name == "福田首相":
        a = randint(1, 7)
    else:
        a = randint(1, 5)
    return a
