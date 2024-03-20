argDict = { # the
    'penCorrect':True,'givenScore':0,
    'givenTime':0,'randTime':0,'penTime':False,'randModeTime':0,
    'givenChars':1,'randChars':0,'penChars':False,'randModeChars':1,
    'numSections':3,'randSections':0,'randModeSections':2,
    'numPuzzles':5,'sectionTime':1
    }

def menuStart():
    print('''
REGEGAME PROTOTYPE
BASIC CLIENT

1. Classic
2. Endless
3. Custom
4. Custom Endless
5. See previous game stats

H. Help
R. Refresh Page
Q. Quit Game
''')
    global lastMenuState 
    lastMenuState = 'menuStart'
    match input('>>>:')[0].lower():
        case '1':
            return setupClassic()
        case '2':
            return setupEndless()
        case '3':
            return 'setupCustom'
        case '4':
            return 'setupCustomEndless'
        case '5':
            return 'menuStats'
        case 'h':
            lastMenuState = 'menuStart'
            return 'menuAllHelp'
        case 'e':
            lastMenuState = 'menuStart'
            return 'menuQuit'
        case 'r':
            return 'menuStart'
        case 'q':
            lastMenuState = 'menuStart'
            return 'menuQuit'

def setupClassic():
    print('''
Select Difficulty

1. Easy
2. Moderate
3. Hard
4. Insane 
          
H. Help
E. Return to Main Menu
Q. Quit Game
''')
    global lastMenuState
    lastMenuState = 'menuStart'
    match input('>>>:')[0].lower():
        case '1':
            return { # the
'penCorrect':True,'givenScore':0,
'givenTime':10,'randTime':1,'penTime':True,'randModeTime':0,
'givenChars':3,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':3,'randSections':0,'randModeSections':2,
'numPuzzles':5,'sectionTime':2
            }
        case '2':
            return { # the
'penCorrect':True,'givenScore':0,
'givenTime':5,'randTime':1,'penTime':True,'randModeTime':0,
'givenChars':2,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':5,'randSections':1,'randModeSections':2,
'numPuzzles':10,'sectionTime':2
            }
        case '3':
            return { # the
'penCorrect':True,'givenScore':0,
'givenTime':3,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':1,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':6,'randSections':2,'randModeSections':2,
'numPuzzles':15,'sectionTime':1.2
            }
        case '4':
            return { # the
'penCorrect':True,'givenScore':0,
'givenTime':1,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':0,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':8,'randSections':3,'randModeSections':2,
'numPuzzles':25,'sectionTime':1
            }
        case 'h':
            return 'menuAllHelp'
        case 'e':
            return lastMenuState
        case 'r':
            return 'menuStart'
        case 'q':
            return 'menuQuit'
    return argDict
def setupEndless():
    print('''
Select Difficulty

1. Easy
2. Moderate
3. Hard
4. Insane 
          
H. Help
E. Return to Main Menu
Q. Quit Game
''')
    global lastMenuState
    lastMenuState = 'menuStart'
    match input('>>>:')[0].lower():
        case '1':
            return { # the
'penCorrect':True,'givenScore':10,
'givenTime':10,'randTime':1,'penTime':True,'randModeTime':0,
'givenChars':3,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':3,'randSections':0,'randModeSections':2,
'numPuzzles':255,'sectionTime':3
            }
            
        case '2':
            return { # the
'penCorrect':True,'givenScore':10,
'givenTime':5,'randTime':1,'penTime':True,'randModeTime':0,
'givenChars':2,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':5,'randSections':1,'randModeSections':2,
'numPuzzles':255,'sectionTime':2
            }
        case '3':
            return { # the
'penCorrect':True,'givenScore':5,
'givenTime':3,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':1,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':6,'randSections':2,'randModeSections':2,
'numPuzzles':255,'sectionTime':1.5
            }
        case '4':
            return { # the
'penCorrect':True,'givenScore':5,
'givenTime':1,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':0,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':8,'randSections':3,'randModeSections':2,
'numPuzzles':255,'sectionTime':1
            }
        case 'h':
            return 'menuAllHelp'
        case 'e':
            return lastMenuState
        case 'r':
            return 'menuStart'
        case 'q':
            return 'menuQuit'
    return argDict

def setupCustom():
    print('Current Settings:')
    for here in argDict:
        print(here,argDict[here])
    global lastMenuState
    lastMenuState = 'setupCustom'
    while True:
        print('''
1. Penalty Settings
2. Time Settings
3. Character Settings
4. Sections Settings
5. Duration of Game
S. Start Game
          
H. Help
E. Return to Main Menu
Q. Quit Game
''')
        match input('>>>:')[0].lower():
            case '1':
                localCommand = setupCustomPen()
            case '2':
                localCommand = setupCustomTime()
            case '3':
                localCommand = setupCustomChars()
            case '4':
                localCommand = setupCustomSections()
            case '5':
                localCommand = setupCustomDuration()
            case 's':
                return argDict
            case 'h':
                return 'menuAllHelp'
            case 'e':
                return 'menuQuit'
            case 'r':
                return 'setupCustom'
            case 'q':
                return 'menuQuit'
        if localCommand != None:
            return localCommand

def setupCustomEndless():
    print('Current Settings:')
    argDict['numPuzzles'] = 255
    for here in argDict:
        print(here,argDict[here])
    while True:
        print('''
1. Penalty Settings
2. Time Settings
3. Character Settings
4. Sections Settings
5. Duration of Game

H. Help
E. Return to Main Menu
Q. Quit Game
''')
        global lastMenuState
        lastMenuState = 'setupCustomEndless'
        match input('>>>:')[0].lower():
            case '1':
                setupCustomPen()
            case '2':
                setupCustomTime()
            case '3':
                setupCustomChars()
            case '4':
                setupCustomSections()
            case '5':
                setupCustomDuration()
            case 'h':
                lastMenuState = 'setupCustomEndless'
                return 'menuAllHelp'
            case 'e':
                lastMenuState = 'setupCustomEndless'
                return 'menuQuit'
            case 'r':
                return 'menuStart'
            case 'q':
                lastMenuState = 'setupCustomEndless'
                return 'menuQuit'

def setupCustomPen():
    print('1. Incorrect Answer Penalty:', argDict['penCorrect'])
    print('2. Exceed Time Limit Penalty:',argDict['penTime'])
    print('3. Exceed Char Limit Penalty:',argDict['penChars'])
    print('''

E. Return to previous menu.
H. General Help
Q. Quit Game
''')
    global lastMenuState
    lastMenuState = 'setupCustom'
    match input('>>>:')[0].lower():
        case '1':
            argDict['penCorrect'] = not argDict['penCorrect']
        case '2':
            argDict['penTime'] = not argDict['penTime']
        case '3':
            argDict['penChars'] = not argDict['penChars']
        case 'h':
            return 'menuAllHelp'
        case 'q':
            return 'menuQuit'
        case 'e':
            return lastMenuState
    return

def intinput(raw):
    try:
        return int(raw)
    except:
        print('exceptionCaught: input must be a number. Placing default value of 1.')
        return 1

def setupCustomTime():
    print('1. Extra Time Given:',argDict['givenTime'])
    print('2. Exceed Time Limit Penalty',argDict['penTime'])
    print('3. Time Randomness',argDict['randTime'])
    print('4. Time Randomness Mode',argDict['randModeTime'])
    print('5. Time Given per Section',argDict['sectionTime'])
    print('''

E. Return to previous menu.
H. General Help
Q. Quit Game
''')
    global lastMenuState
    lastMenuState = 'setupCustom'
    match input('>>>:')[0].lower():
        case '1':
            argDict['givenTime'] = intinput(input('Input Number >>:'))
        case '2':
            argDict['penTime'] = not argDict['penTime']
        case '3':
            argDict['randTime'] = intinput(input('Input Number >>:'))
        case '4':
            argDict['randModeTime'] = intinput(input('Input Number >>:'))
        case '5':
            argDict['sectionTime'] = intinput(input('Input Number >>:'))
        case 'h':
            return 'menuAllHelp'
        case 'e':
            return
        case 'q':
            return 'menuQuit'
    return

def setupCustomChars():
    print('1. Extra Characters Given:',argDict['givenChars'])
    print('2. Exceed Character Limit Penalty',argDict['penChars'])
    print('3. char Randomness',argDict['randChars'])
    print('4. char Randomness Mode',argDict['randModeChars'])
    print('''

E. Return to previous menu.
H. General Help
Q. Quit Game
''')
    global lastMenuState
    lastMenuState = 'setupCustom'
    match input('>>>:')[0].lower():
        case '1':
            argDict['givenChars'] = intinput(input('Input Number >>:'))
        case '2':
            argDict['penChars'] = not argDict['penChars']
        case '3':
            argDict['randChars'] = intinput(input('Input Number >>:'))
        case '4':
            argDict['randModeChars'] = intinput(input('Input Number >>:'))
        case 'e':
            return
        case 'h':
            return 'menuAllHelp'
        case 'q':
            return 'menuQuit'
    return

def setupCustomSections():
    print('1. Number of Sections:',argDict['numSections'])
    print('2. Exceed Time Limit Penalty',argDict['randModeSections'])
    print('''

E. Return to previous menu.
H. General Help
Q. Quit Game
''')
    global lastMenuState
    lastMenuState = 'setupCustom'
    match input('>>>:')[0].lower():
        case '1':
            argDict['givenChars'] = intinput(input('Input Number >>:'))
        case '2':
            argDict['penChars'] = not argDict['penChars']
        case 'e':
            return
        case 'h':
            return 'menuAllHelp'
        case 'q':
            return 'menuQuit'
    return

def setupCustomDuration():
    print('1. Extra Score Given',argDict['givenScore'])
    print('2. Number of Sections',argDict['numSections'])
    print('3. Number of Puzzles',argDict['numPuzzles'])
    print('''

E. Return to previous menu.
H. General Help
Q. Quit Game
''')
    global lastMenuState
    lastMenuState = 'setupCustom'
    match input('>>>:')[0].lower():
        case '1':
            argDict['givenScore'] = intinput(input('Input Number >>:'))
        case '2':
            argDict['numSections'] = intinput(input('Input Number >>:'))
        case '3':
            argDict['numPuzzles'] = intinput(input('Input Number >>:'))
        case 'e':
            return
        case 'h':
            return 'menuAllHelp'
        case 'q':
            return 'menuQuit'
    return

def menuStats(stats):
    mode = 0
    while stats:
        print('Your statistics:')
        statsViewer(stats,mode)
        print('''
    Press B or N to change view mode.
    Press E to go back or R to go to main menu.
    ''')
        localInput = input('>>>:')[0].lower()
        match localInput:
            case 'b':
                mode -= 1
                if mode <1:
                    mode = 0
            case 'n':
                mode += 1
            case 'r':
                return 'menuStart'
            case 'e':
                return lastMenuState
            case 'h':
                return 'menuAllHelp'
            case 'q':
                return 'menuQuit'
            case _:
                try:
                    mode = int(localInput)
                except:
                    mode = None
    print('No data! Play a game first.')
    return lastMenuState
        


def menuAllHelp():
    print('Input commands.')
    input('Press any key. >>>:')
    return lastMenuState

def menuQuit():
    print('''
Are you sure you want to quit?

Y. Yes. I want to exit the program. 
N. No. Bring me back.
M. No. Bring me to the main menu.
          ''')
    match input('>>>:')[0].lower():
        case 'y':
            exit()
        case 'n':
            return lastMenuState
        case 'm':
            return 'menuStart'


# BACKEND
        
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
    # sectionTypeChance = ranlistFactory((25,10,10,10,10,10,20)) # plh
    # sectionTypeChance.append(101)
    # textFactoryChance = ranlistFactory((35,20,25,10))
    # textFactoryChance.append(101)
    # sectionLengthChance = ranlistFactory((30,25,25,15))
    # sectionLengthChance.append(101)
    # quantifierTypeChance = ranlistFactory((10,10,10,10))
    sectionTypeChance = (0,25,35,45,55,65,75,95,101)
    textFactoryChance = (0,35,55,80,90,101)
    sectionLengthChance = (0,30,55,80,95,101)
    quantifierTypeChance = (0,10,20,30,70,101)
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
        rndNum=rnd(0,100)
        if rndNum in range(quantifierTypeChance[0],quantifierTypeChance[1]-1):
            quota[-1]['quantifierType']=1
        elif rndNum in range(quantifierTypeChance[1],quantifierTypeChance[2]-1):
            quota[-1]['quantifierType']=2
        elif rndNum in range(quantifierTypeChance[2],quantifierTypeChance[3]-1):
            quota[-1]['quantifierType']=3
        elif rndNum in range(quantifierTypeChance[3],quantifierTypeChance[4]-1):
            quota[-1]['quantifierType']=4
        else:
            quota[-1]['quantifierType']=5
    
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
        quantifierType = theQuota[numQuota]['quantifierType'] #TODO
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
                theEx.append('.')
                print('eh') # plh
        match quantifierType:
            case 1:
                theEx.append('+')
            case 2:
                theEx.append('*')
                if bd2(70):
                    if sectionLength:
                        sectionLength = 1
                    else:
                        sectionLength = 0
            case 3:
                theEx.append('?')
                if bd2(90):
                    if sectionLength:
                        sectionLength = 1
                    else:
                        sectionLength = 0
            case 4:
                theEx.append('{')
                quantifierRand = rnd(0,3)
                sectionLength = quantifierRand
                theEx.append(str(quantifierRand))
                theEx.append('}')
            case _:
                pass

        totalLength += sectionLength
        theQuota[numQuota] = {'type':sectionType,'textFactoryMode':textFactoryMode,'sectionLength':sectionLength}
    return {'puzzle':theEx, 'sectionLength':totalLength, 'totalLength':totalLength} #to maintain compatiablilty

def gamePlay(givenTime,givenChars,numSections,sectionTime):

    timeAnchorLocal = time()
    theExpression = regexSectionConstructor(numSections)
    theExpression['puzzle'] = listJoinery(theExpression['puzzle'])
    givenChars += theExpression['totalLength']
    givenTime += (numSections*sectionTime)

    print('Solve /'+theExpression['puzzle']+'/ in',givenChars,'characters and',givenTime,'seconds')

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
    
def gameSession(argDict):
    timeAnchorSession = time()
    score = argDict['givenScore']
    stats = [] # list of dicts
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
                case 1: # addonly
                    # randNamesFloor[randSelected] = 0
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]
                case 2: # minusonly
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    # randNamesFloor[randSelected] = 0
                case 3: # reduced minus
                    randNamesFloor[randSelected] = 1-randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]
                case 4: # additional add
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = 1+randNamesQuantity[randSelected]
                case 5: # reduced add
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]-1

    for iteration in range(0,argDict['numPuzzles']):
        print('Puzzle',iteration+1)
        puzzleResult = gamePlay(
                argDict['givenTime']+rnd(randNamesFloor[0],randNamesCeil[0]),
                argDict['givenChars']+rnd(randNamesFloor[1],randNamesCeil[1]),
                argDict['numSections']+rnd(randNamesFloor[2],randNamesCeil[2]),
                argDict['sectionTime']
                )
        
        score += 1
        if (not puzzleResult['correct']) and argDict['penCorrect']:
            score -= 1
            print('Incorrect Answer.')
        if (not puzzleResult['inChars']) and argDict['penChars']:
            score -= 1
            print('Exceeded Character Limit')
        if (not puzzleResult['inTime']) and argDict['penTime']:
            score -= 1
            print('Exceeded Time Limit')
        
        stats.append(puzzleResult)
        print(score)
        print(int(time()-timeAnchorSession))
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
# sectionender in regexsectionconstructor





# working area
gotoMenu = 'menuStart'
sessionStats = None
while True:
    # print(gotoMenu)
    match gotoMenu:
        case 'menuStart':
            gotoMenu = menuStart()
        case 'setupCustom':
            gotoMenu = setupCustom()
        case 'setupCustomEndless':
            gotoMenu = setupCustomEndless()
        case 'menuAllHelp':
            gotoMenu = menuAllHelp()
        case 'menuQuit':
            gotoMenu = menuQuit()
        case 'menuStats':
            gotoMenu = menuStats(sessionStats)
        case None:
            exit()
        case _:
            print(gotoMenu)
            sessionStats = gameSession(gotoMenu)['stats']
            gotoMenu = menuStats(sessionStats)







