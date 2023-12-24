# 2 business class

class passes():
    name = ''
    flight = ''
    time = ''
    date = ''

boardingPasses = []

for parseIteration in range(0,10):
    emptyTuple = passes()
    emptyTuple.name = input('your name here> ')
    emptyTuple.flight = parseIteration
    boardingPasses.append(emptyTuple)


print(boardingPasses[1].name)