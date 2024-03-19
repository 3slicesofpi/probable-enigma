from random import randint as rnd
from random import getrandbits
from time import time
import re
def d2(): #fast!
    return getrandbits(1)

def bd2(TrueChance): #bit slower
    num = rnd(0,100)
    if num <= TrueChance:
        return True
    else: return False
    


textTuple = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numberTuple = ('0','1','2','3','4','5','6','7','8','9')
symbolTuple = ('!','#','%',':',';','<','>','=','_','~') 
def textFactory(mode,blacklist):
    finalSolution = ''
    while True:
        match mode:
            case 1: # a-z
                textPos = rnd(0,25)
                finalSolution = str(textTuple[textPos])
            case 2: # A-Z
                textPos = rnd(0,25)
                finalSolution = str(textTuple[textPos].upper())
            case 3: # 0-9
                textPos = rnd(0,9)
                finalSolution = str(numberTuple[textPos])
            case 4: # symbols
                textPos = rnd(0,9)
                finalSolution = str(symbolTuple[textPos])
            case 5: # \s
                textPos = 0
                finalSolution = ' ' # NO BLACKLIST ON MODE 5
        if not (finalSolution in blacklist):
            return finalSolution

def listJoinery(rawList):
    joinedString = ''
    for element in rawList:
        joinedString = joinedString+str(element)
    return joinedString

def integratedFactoryAndValidator(textFactoryMode):
    localValidation = 0
    while localValidation == 0:
        try:
            negatoryFlag = ''
            if rnd(1,2) == 1:
                negatoryFlag = '^'
            char2 = rnd(1,25)
            char1 = rnd(0,char2-1)
            if textFactoryMode:
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

def ranlistFactory(raw):
    newList = [0]
    for here in raw:
        newList.append(here)
        newList[-1]+=newList[-2]
    return newList

def regexRndChooser(numofSections):
    # use better
    sectionTypeChance = ranlistFactory((25,10,10,10,10,10,20)) # plh
    sectionTypeChance.append(101)
    textFactoryChance = ranlistFactory((35,20,25,10))
    textFactoryChance.append(101)
    sectionLengthChance = ranlistFactory((30,25,25,15))
    sectionLengthChance.append(101)
    quota = []
    for sectionnum in range(1,numofSections+1):
        rndNum = rnd(0,100)
        if rndNum in range(sectionTypeChance[0],sectionTypeChance[1]-1):
            quota.append({'type':1})
        elif rndNum in range(sectionTypeChance[1],sectionTypeChance[2]-1):
            quota.append({'type':2})
        elif rndNum in range(sectionTypeChance[2],sectionTypeChance[3]-1):
            quota.append({'type':3})
        elif rndNum in range(sectionTypeChance[3],sectionTypeChance[4]-1):
            quota.append({'type':4})
        elif rndNum in range(sectionTypeChance[4],sectionTypeChance[5]-1):
            quota.append({'type':5})
        elif rndNum in range(sectionTypeChance[5],sectionTypeChance[6]-1):
            quota.append({'type':6})
        elif rndNum in range(sectionTypeChance[6],sectionTypeChance[7]-1):
            quota.append({'type':7})
        else:
            quota.append({'type':8})
        rndNum = rnd(0,100)
        if rndNum in range(textFactoryChance[0],textFactoryChance[1]-1):
            quota[-1]['textFactoryMode']=1
        elif rndNum in range(textFactoryChance[1],textFactoryChance[2]-1):
            quota[-1]['textFactoryMode']=2
        elif rndNum in range(textFactoryChance[2],textFactoryChance[3]-1):
            quota[-1]['textFactoryMode']=3
        elif rndNum in range(textFactoryChance[3],textFactoryChance[4]-1):
            quota[-1]['textFactoryMode']=4
        else:
            quota[-1]['textFactoryMode']=5
        rndNum = rnd(0,100)
        if rndNum in range(sectionLengthChance[0],sectionLengthChance[1]-1):
            quota[-1]['sectionLength']=1
        elif rndNum in range(sectionLengthChance[1],sectionLengthChance[2]-1):
            quota[-1]['sectionLength']=2
        elif rndNum in range(sectionLengthChance[2],sectionLengthChance[3]-1):
            quota[-1]['sectionLength']=3
        elif rndNum in range(sectionLengthChance[3],sectionLengthChance[4]-1):
            quota[-1]['sectionLength']=4
        else:
            quota[-1]['sectionLength']=5
    
    # if numofSections>5 and d2():
    #     capGrpPosStart = rnd(0,len(quota)-1)
    #     quota.insert(capGrpPosStart,'(')
    #     capGrpPosEnd = rnd(capGrpPosStart+2,len(quota))
    #     quota.insert(capGrpPosEnd,')')
    return quota


def regexSectionConstructor(numofSections): #mk. IIA
    theEx = []
    totalLength = 0
    theQuota = regexRndChooser(numofSections)
    for numQuota in range(0,numofSections):
        sectionType = theQuota[numQuota]['type']
        sectionLength = theQuota[numQuota]['sectionLength']
        textFactoryMode = theQuota[numQuota]['textFactoryMode']
        match sectionType:  
            case 1: # [abc] blacklist causes crashes
                theEx.append('[')
                blacklist = []

                if d2():
                    negatoryFlag = True
                    theEx.append('^')
                else:
                    negatoryFlag = False
                match textFactoryMode:
                    case 1: #a
                        if bd2(60) and negatoryFlag:
                            theEx.append('A-Z0-9') # TODO update to include symbols
                    case 2: #A
                        if bd2(60) and negatoryFlag:
                            theEx.append('a-z0-9')
                    case 3: #1
                        if bd2(60) and negatoryFlag:
                            theEx.append('A-z')
                    case 4: #%
                        if d2() and negatoryFlag:
                            theEx.append('A-z0-9') #remain as is
                    case 5:
                        pass

                # there is a better way involving maths
                # centralize in  regexRndChooser
                # carshes happen here
                for char in range(0,sectionLength):
                    theEx.append(textFactory(textFactoryMode,blacklist))
                    # blacklist.append(theEx[-1])
                sectionLength = 1
                theEx.append(']')
            case 2: # [A-Z]/[a-z]
                # blacklist = []
                negatoryFlag = d2()
                match rnd(1,5): # theres a better way involving: theEx[-1] = '', then appending ret of inteFact&Validor
                    case 1:
                        if d2():
                            theEx.append('[')
                            if negatoryFlag:
                                theEx.append('^')
                            theEx.append('a-')
                            theEx.append(textFactory(1,('a','z')))
                            textFactoryMode = 1
                        else:
                            theEx.append('[')
                            if negatoryFlag:
                                theEx.append('^')
                            theEx.append('A-')
                            theEx.append(textFactory(2,('A','Z','a','z')))
                            textFactoryMode = 2
                        theEx.append(']')
                    case 2:
                        if d2():
                            theEx.append('[')
                            if negatoryFlag:
                                theEx.append('^')
                            theEx.append(textFactory(1,('z','a')))
                            theEx.append('-z]')
                            textFactoryMode = 1
                        else:
                            theEx.append('[')
                            if negatoryFlag:
                                theEx.append('^')
                            theEx.append(textFactory(2,('Z','A','z','a')))
                            theEx.append('-Z]')
                            textFactoryMode = 2
                    case _:
                        textFactoryMode = d2()
                        theEx.append(integratedFactoryAndValidator(textFactoryMode))
                        textFactoryMode += 1 # scary!
            case 3: # [A-z]
                # blacklist = []
                sectionLength = 1
                theEx.append('[')
                if d2():
                    theEx.append('^')
                match rnd(1,5):
                    case 1:
                        theEx.append('A-')
                        theEx.append(textFactory(1,('a')))
                    case 2:
                        theEx.append(textFactory(2,('Z','z')))
                        theEx.append('-z')
                    case _:
                        theEx.append(textFactory(2,()))
                        theEx.append('-')
                        theEx.append(textFactory(1,()))
                theEx.append(']')
                textFactoryMode = 1 # its actually both 1 and 2
            case 4: # .
                for char in range(0,sectionLength):
                    theEx.append('.')
            case 5: # .\.\*\s
                for char in range(0,sectionLength):
                    match rnd(1,4):
                        case 1:
                            theEx.append('.')
                        case 2:
                            theEx.append('\.')
                        case 3:
                            theEx.append('\*')
                        case 4:
                            theEx.append('\s')           
            case 6: # n45$! 
                for char in range(0,sectionLength):
                    theEx.append(textFactory(rnd(1,5),()))
            case 7: # (abc), crashes
                blacklist = []
                if textFactoryMode == 4:
                    textFactoryMode = rnd(1,3)
                if d2():
                    #(abc)
                    # TODO BRACKETS HERE
                    theEx.append('(')
                    for iterations in range(0,sectionLength):
                        theEx.append(textFactory(textFactoryMode,blacklist))
                        # blacklist.append(theEx[-1])
                    theEx.append(')')
                else:
                    #abc no brackets
                    for iterations in range(0,sectionLength):
                        theEx.append(textFactory(textFactoryMode,blacklist))
                        # blacklist.append(theEx[-1])
            case _:
                print('eh') # plh
        totalLength += sectionLength
        theQuota[numQuota] = {'type':sectionType,'textFactoryMode':textFactoryMode,'sectionLength':sectionLength}
    return {'puzzle':theEx, 'sectionLength':totalLength, 'totalLength':totalLength} #to maintain compatiablilty

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
                argDict['givenTime']+rnd(randNamesFloor[0],randNamesCeil[0]),
                argDict['givenChars']+rnd(randNamesFloor[1],randNamesCeil[1]),
                argDict['numSections']+rnd(randNamesFloor[2],randNamesCeil[2])
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


# TODO 
# EXCEPTIONCATCHER
    