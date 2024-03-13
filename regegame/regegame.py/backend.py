from random import randint
from time import time
import re

textTuple = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numberTuple = ('0','1','2','3','4','5','6','7','8','9')
symbolTuple = ('!','#','%',':',';','<','>','=','_','~') 
def integratedFactoryAndValidator():
    textFactoryMode = randint(1,2)
    localValidation = 0
    while localValidation == 0:
        try:
            negatoryFlag = ''
            if randint(1,2) == 1:
                negatoryFlag = '^'
            char2 = randint(1,25)
            char1 = randint(0,char2-1)
            if randint(1,2) == 1:
                testExpression = '['+negatoryFlag+textTuple[char1].upper()+'-'+textTuple[char2].upper()+']'
            else:
                testExpression = '['+negatoryFlag+textTuple[char1]+'-'+textTuple[char2]+']'
            re.findall(testExpression,'a')
        except re.error: # WHEN ERROR
            localValidation = -1
        except KeyError: # RAISE NEW
            localValidation = -1
        finally:
            localValidation += 1
    return testExpression

def regexSectionConstructor(puzzleLength): #mk. IB stable
    puzzle = []
    totalLength = 0
    textFactoryMode = None
    for iteration in range(0,puzzleLength):
        sectionLength = 0
        matchNumRand = randint(0,100)
        blacklist = []
        match True:
            case True if matchNumRand in range(0,24):
                #[abc]
                puzzle.append('[')
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
                if randint(1,2) == 1:
                    puzzle.append('^')

                for iteration in range(0,randint(1,4)):
                    puzzle.append(textFactory(textFactoryMode,blacklist))
                    blacklist.append(puzzle[-1])
                puzzle.append(']')
                sectionLength += 1
                
            case True if matchNumRand in range(25,44):
                #[a-c]
                puzzle.append(integratedFactoryAndValidator())
                sectionLength += 1
            case True if matchNumRand in range(45,64):
                #[A-c]
                puzzle.append('[')
                if randint(1,2) == 1:
                    puzzle.append('^')
                puzzle.append(textFactory(2,blacklist))
                puzzle.append('-')
                puzzle.append(textFactory(1,blacklist))
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
                            puzzle.append(textFactory(textFactoryMode,blacklist))
                            blacklist.append(puzzle[-1])
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
                            puzzle.append(textFactory(textFactoryMode,blacklist))
                            blacklist.append(puzzle[-1])

        

        totalLength += sectionLength
    return {'puzzle':puzzle, 'sectionLength':totalLength, 'totalLength':totalLength} #to maintain compatiablilty

def textFactory(mode,blacklist):
    ignition = True
    finalSolution = ''
    while (finalSolution in blacklist) or ignition:
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

def listJoinery(rawList):
    joinedString = ''
    for element in rawList:
        joinedString = joinedString+str(element)
    return joinedString


def gameSetup(argType,argDict):
    match argType:
        case 1: # difficulty scale, not endless
            match argDict['difficulty']:
                case 0:
                    argDict = {'givenTime':0,'givenChars':0,'penaltyTime':True,'penaltyChars':True,'numSections':1,'randSections':0,'numPuzzles':5}
                case 1:
                    argDict = {'givenTime':1,'givenChars':1,'penaltyTime':True,'penaltyChars':True,'numSections':2,'randSections':1,'numPuzzles':5}
                case 2:
                    argDict = {'givenTime':2,'givenChars':2,'penaltyTime':True,'penaltyChars':True,'numSections':3,'randSections':1,'numPuzzles':10}
                case 3:
                    argDict = {'givenTime':3,'givenChars':3,'penaltyTime':True,'penaltyChars':True,'numSections':5,'randSections':2,'numPuzzles':13}

        case 2: # difficulty scale endless
            match argDict['difficulty']:
                case 0:
                    argDict = {'givenTime':0,'givenChars':0,'penaltyTime':True,'penaltyChars':True,'numSections':2,'randSections':1}
                case 1:
                    argDict = {'givenTime':1,'givenChars':1,'penaltyTime':True,'penaltyChars':True,'numSections':2,'randSections':1}
                case 2:
                    argDict = {'givenTime':1,'givenChars':2,'penaltyTime':True,'penaltyChars':True,'numSections':3,'randSections':1}
                case 3:
                    argDict = {'givenTime':2,'givenChars':3,'penaltyTime':True,'penaltyChars':True,'numSections':4,'randSections':2}
            argDict['numPuzzles'] = None


        case 3: # allargsgiven not endless  
            if argDict['numPuzzles'] == (0 or None):
                argDict['numPuzzles'] = randint(5,25)
        case 4: 
            argDict['numPuzzles'] = None
    return argDict
       
def gamePlay(givenTime,givenChars,numSections):
    timeAnchorLocal = time()
    theExpression = regexSectionConstructor(numSections)
    theExpression['puzzle'] = listJoinery(theExpression['puzzle'])
    givenChars += theExpression['totalLength']

    print('Solve /',theExpression['puzzle']+'/ in',givenChars,'characters and',givenTime,'seconds')

    ansWer = str(input('>>>:'))
    ansLen = len(ansWer)
    usedTime = (time()-timeAnchorLocal)

    puzzleResult = {
        'correct':False,
        'inChars':False,
        'inTime':False,
        'usedChars':ansLen,
        'usedTime':usedTime,
        'expression':theExpression['puzzle']
    }
    if re.match(theExpression['puzzle'],ansWer) != None:
        puzzleResult['correct'] = True
    if ansLen <= givenChars:
        puzzleResult['inChars'] = True
    if usedTime <= givenTime:
        puzzleResult['inTime'] = True
    return puzzleResult
    

# EXAMPLE ARGDICT
# givenchars add to minimum.
argDict = {
    'penCorrect':True,'givenScore':0,
    'givenTime':0,'randTime':0,'penTime':False,'randModeTime':0,
    'givenChars':1,'randChars':0,'penChars':False,'randModeChars':1,
    'numSections':3,'randSections':0,'randModeSections':2,
    'numPuzzles':5
    }
def gameSession(argDict):
    timeAnchorSession = time()
    score = argDict['givenScore']
    stats = [] # list of dicts
    #TODO: test
    #TODO: stat viewer
    #time, chars, sections
    randNamesFloor = [0,0,0]
    randNamesCeil = [0,0,0]
    randNamesMode = (argDict['randModeTime'],argDict['randModeChars'],argDict['randModeSections'])
    randNamesQuantity = (argDict['randTime'],argDict['randChars'],argDict['randSections'])
    for randSelected in range(3):
        if randNamesQuantity[randSelected]>0:
            match randNamesMode[randSelected]:
                case 0: # default
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]
                case 1:
                    # randNamesFloor[randSelected] = 0
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]
                case 2:
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    # randNamesFloor[randSelected] = 0
                case 3:
                    randNamesFloor[randSelected] = 1-randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]
                case 4:
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = 1+randNamesQuantity[randSelected]
                case 5:
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]-1

    for iteration in range(0,argDict['numPuzzles']):
        print('Puzzle',iteration)
        puzzleResult = gamePlay(
                argDict['givenTime']+randint(randNamesFloor[0],randNamesCeil[0]),
                argDict['givenChars']+randint(randNamesFloor[1],randNamesCeil[1]),
                argDict['numSections']+randint(randNamesFloor[2],randNamesCeil[2])
                )
        
        score += 1
        if (not puzzleResult['correct']) and argDict['penCorrect']:
            score -= 1
            print(False)
        if (not puzzleResult['inChars']) and argDict['penChars']:
            score -= 1
            print(False)
        if (not puzzleResult['inTime']) and argDict['penTime']:
            score -= 1
            print(False)
        
        stats.append(puzzleResult)
    return {'stats':stats,'score':score}

def statsViewer(stats,mode):
    index = 0
    match mode:
        case None:
            for iteration in stats:
                index += 1
                print(iteration)
        case 0:
            for iteration in stats:
                index += 1
                print(str(index)+'.',iteration['expression'],iteration['correct'],iteration['usedChars'],str(int(iteration['usedTime'])))
        case 1:
            for iteration in stats:
                index += 1
                print(str(index)+'.',iteration['correct'])
        case 2:
            for iteration in stats:
                index += 1
                print(str(index)+'.',iteration['expression'])
        case 3:
            for iteration in stats:
                index += 1
                print(str(index)+'.',iteration['inChars'],iteration['usedChars'])
        case 4:
            for iteration in stats:
                index += 1
                print(str(index)+'.',iteration['inTime'],str(int(iteration['usedTime'])))
        case _:
            for iteration in stats:
                index += 1
                print(str(index)+'.',iteration[str(mode)])




    