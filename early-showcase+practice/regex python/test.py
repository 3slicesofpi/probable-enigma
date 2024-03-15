import re
from random import randint as rnd
from random import getrandbits


def ranlistFactory(raw):
    newList = [0]
    for here in raw:
        newList.append(here)
        newList[-1]+=newList[-2]
    return newList

a = ranlistFactory((25,10,10,10,10,10,20))
a.append(101)   
print(a)