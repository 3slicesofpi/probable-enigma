def uplicator(num):
    return lambda a: a*a*num

doubler = uplicator(4)
print(doubler(3))


