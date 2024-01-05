# function to make big lists

def randInt(targetN,max,min):
    import random
    result = []
    for iteration in range(targetN):
        result.append(random.randint(min,max))
    return result

print(randInt(100000,500000,-500000))
