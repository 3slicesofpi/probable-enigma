def foolBar(num,checkNum):
    if num%checkNum != 0:
        return 'F'
    else: return 'T'

def foolsDicts(num,checks):
    resultDict = {'n':num}
    for iterationChecks in range(2,checks+1):
        resultDict[iterationChecks] = iterationChecks = (foolBar(num,iterationChecks))
    return resultDict

for n in range(0,100000):
    print(foolsDicts(n,17))
