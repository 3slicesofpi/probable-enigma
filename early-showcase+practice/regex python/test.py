import re
from random import randint

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
        case 4: # symbols
            textPos = randint(0,9)
            finalSolution = (symbolTuple[textPos])
        case 5: # \s
            textPos = 0
            finalSolution = ' '
        
    return str(finalSolution)

def integratedFactoryAndValidator(): # needs an update.
    textFactoryMode = randint(1,2)
    localValidation = 0
    while localValidation == 0:
        try:
            negatoryFlag = ''
            if randint(1,2) == 1:
                negatoryFlag = '^'
            char1 = textFactory(textFactoryMode)
            char2 = textFactory(textFactoryMode)
            if char1 == char2:
                raise KeyError
            testExpression = '['+negatoryFlag+char1+'-'+char2+']'
            re.findall(testExpression,'a')
        except re.error:
            localValidation = -1
        except KeyError:
            localValidation = -1
        finally:
            localValidation += 1
    return testExpression

def regexSectionConstructor(puzzleLength):
    puzzle = []
    totalLength = 0
    textFactoryMode = None
    for iteration in range(0,puzzleLength):
        sectionLength = 0
        matchNumRand = randint(0,100)
        match True:
            case True if matchNumRand in range(0,24):
                #[abc]
                puzzle.append('[')
                if randint(1,2) == 1:
                    puzzle.append('^')
                textFactoryMode = randint(0,100)
                if textFactoryMode in range(0,34):
                    textFactoryMode = 1 #a
                elif textFactoryMode in range(35,54):
                    textFactoryMode = 2 #A
                elif textFactoryMode in range(55,84):
                    textFactoryMode = 3 #1
                else:
                    if randint(1,5)<=2:
                        textFactoryMode = 4 #%
                    else:
                        textFactoryMode = 5 #/s

                for iteration in range(0,randint(1,4)):
                    puzzle.append(textFactory(textFactoryMode))
                puzzle.append(']')
                
            case True if matchNumRand in range(25,44):
                #[a-c]
                puzzle.append(integratedFactoryAndValidator())
                sectionLength += 1
            case True if matchNumRand in range(45,64):
                #[A-c]
                puzzle.append('[')
                if randint(1,2) == 1:
                    puzzle.append('^')
                puzzle.append(textFactory(2))
                puzzle.append('-')
                puzzle.append(textFactory(1))
                puzzle.append(']')
                sectionLength += 1
            case True if matchNumRand in range(65,100):
                #abc
                textFactoryMode = randint(0,100)
                if textFactoryMode in range(0,34):
                    textFactoryMode = 1 #a
                elif textFactoryMode in range(35,54):
                    textFactoryMode = 2 #A
                elif textFactoryMode in range(55,84):
                    textFactoryMode = 3 #1
                else:
                    textFactoryMode = 4 #/s
                match randint(1,2):
                    case 1:
                        #(abc)
                        puzzle.append('(')
                        if randint(1,2) == 1:
                            puzzle.append('^')
                        matchNumRand = randint(0,100) #watch out
                        if matchNumRand in range(0,23):
                            sectionLength = 1
                        elif matchNumRand in range(35,69):
                            sectionLength = 2
                        elif matchNumRand in range(70,84):
                            sectionLength = 3
                        elif matchNumRand in range(85,94):
                            sectionLength = 4
                        else: 
                            sectionLength = 5
                        for iterations in range(0,sectionLength):
                            puzzle.append(textFactory(textFactoryMode))
                        puzzle.append(')')
                    case _:
                        #abc no brackets
                        matchNumRand = randint(0,100) #watch out
                        if matchNumRand in range(0,39):
                            sectionLength = 1
                        elif matchNumRand in range(40,74):
                            sectionLength = 2
                        elif matchNumRand in range(75,89):
                            sectionLength = 3
                        else:
                            sectionLength = 4
                        for iterations in range(0,sectionLength):
                            puzzle.append(textFactory(textFactoryMode))
        

        totalLength += sectionLength
    return {'puzzle':puzzle, 'sectionLength':totalLength, 'totalLength':totalLength} #to maintain compatiablilty


print(regexSectionConstructor(3))
# num = randint(1,100)

# print(num)
# match True:
#     case True if num in range(1,50):
#         print('yess')
#     case True if num in range(51,100):
#         print('nooooo')
#     case _:
#         print('nothin')