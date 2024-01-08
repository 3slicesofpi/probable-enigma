import random # honestly asking ChatGPT would be 99.8% faster

def dictLonger(length,lis):
    result = {}
    for here in range(1,length):
        result[str(here)] = [lis[random.randint(0,len(lis)-1)],random.randint(1,100)]
    return result

# this one for market1.py
def dictLonger(lis):
    result = {}
    for here in range(1,len(lis)):
        result[str(here)] = [lis[here-1],random.randint(1,100)]
    return result

# courtesy of our ai overlords
myList = ["Tomatoes", "Corn", "Green Beans", "Peas", "Carrots", "Chickpeas", "Black Beans", "Kidney Beans", "Baked Beans", "Lentils", "Tuna", "Salmon", "Sardines", "Chicken", "Soup",]
print(dictLonger(myList))