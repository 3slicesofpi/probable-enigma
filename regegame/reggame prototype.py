from random import randint
import re
def integratedFactoryAndValidator():
    textFactoryMode = randint(1,2)
    localValidation = 0
    while localValidation == 0:
        try:
            testExpression = '['+textFactory(textFactoryMode)+'-'+textFactory(textFactoryMode)+']'
            re.findall(testExpression,'a')
        except re.error:
            localValidation = -1
        finally:
            localValidation += 1
    return testExpression

def regexSectionConstructor(puzzleLength):
    puzzle = []
    textFactoryMode = None
    for iteration in range(0,puzzleLength):
        match randint(1,4):
            case 1:
                # [abc]
                textFactoryMode = randint(1,5)
                puzzle.append('[')
                for jteration in range(0,randint(1,5)):
                    puzzle.append(textFactory(textFactoryMode))
                puzzle.append(']')
            case 2:
                # [a-c]
                puzzle.append(integratedFactoryAndValidator())
            case 3:
                # [A-c]
                puzzle.append('[')
                puzzle.append(textFactory(2))
                puzzle.append('-')
                puzzle.append(textFactory(1))
                puzzle.append(']')
            case 4:
                # a
                textLength = randint(1,5)
                match randint(1,3):
                    case 1:
                        for jteration in range(0,textLength):
                            puzzle.append(textFactory(randint(1,4)))
                    case 2:
                        textLength += 1
                        puzzle.append('(')
                        for jteration in range(0,textLength):
                            puzzle.append(textFactory(randint(1,3)))
                        puzzle.append(')')
                    case 3:
                        textLength += 1
                        puzzle.append('[')
                        for jteration in range(0,textLength):
                            puzzle.append(textFactory(randint(1,4)))
                        puzzle.append(']')
        match randint(1,4):
            case 1:
                match randint(1,4): 
                    case 1:
                        puzzle.append('+')
                    case 2:
                        puzzle.append('?')
                    case 3:
                        puzzle.append('*')
                    case 4:
                        puzzle.append('')
            case 2: # nothing
                pass
            case 3:
                puzzle.append('.')
            case 4:
                puzzle.append('{')
                puzzle.append(str(randint(0,3)))
                puzzle.append('}')
    return puzzle

textTuple = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numberTuple = ('0','1','2','3','4','5','6','7','8','9')
symbolTuple = ('!','#','%',':',';','<','>','=','_','~') 
def textFactory(mode):
    match mode:
        case 1: # a-z
            textPos = randint(0,25)
            finalSolution = (textTuple[textPos])
        case 2: # A-Z
            textPos = randint(0,25)
            finalSolution = (textTuple[textPos].upper())
        case 3: # 0-9
            textPos = randint(0,9)
            finalSolution = (numberTuple[textPos])
        case 5: # symbols
            textPos = randint(0,9)
            finalSolution = (symbolTuple[textPos])
        case 4: # \s
            textPos = 0
            finalSolution = ' '
        
    return str(finalSolution)
                
def listJoinery(rawList):
    joinedString = ''
    for element in rawList:
        joinedString = joinedString+str(element)
    return joinedString

print(listJoinery(regexSectionConstructor(1)))