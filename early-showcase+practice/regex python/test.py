import re
from random import randint
import time
print(time.time())


textTuple = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numberTuple = ('0','1','2','3','4','5','6','7','8','9')
symbolTuple = ('!','#','%',':',';','<','>','=','_','~') 
def textFactory(mode,blacklist):
    ignition = True
    finalSolution = ''
    while ((finalSolution in blacklist) and finalSolution != ' ') or ignition:
        ignition = False
        match mode:
            case 1: # a-z
                textPos = randint(0,25)
                finalSolution = str(textTuple[textPos])
            case 2: # A-Z
                textPos = randint(0,25)
                finalSolution = str(textTuple[textPos].upper())
            case 3: # 0-9
                textPos = randint(0,9)
                finalSolution = str(numberTuple[textPos])
            case 4: # symbols
                textPos = randint(0,9)
                finalSolution = str(symbolTuple[textPos])
            case 5: # \s
                textPos = 0
                finalSolution = ' ' # NO BLACKLIST ON MODE 5
    return finalSolution
    
print(textFactory(5,(' ')))