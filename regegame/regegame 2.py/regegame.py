
def clientInput(raw):
    match raw[0].lower():
        case 'h':
            return 'menuHelp'
        case 'r':
            return prevMenuPos
        case 'e':
            return 'menuStart'
        case 'v': # dont print
            return 'menuView'
        case 's': # dont print
            return 'menuSessionSetup'
        case 'q':
            return 'menuQuit'
        case _:
            return raw

def menuStart():
    print('''

1. Classic
2. Custom
3. Tutorial
4. Scenario
5. Campaign (Coming Soon!)
   
H. Help
Q. Quit Game

''')
    global prevMenuPos
    prevMenuPos = 'menuStart'
    command = clientInput(input('>>>:'))
    if command.isnumeric():
        match int(command):
            case 1:
                return 'menuClassic'
            case 2:
                return 'menuCustom'
            case 3: 
                return 'menuTutorial'
            case 4:
                return 'menuScenario'
            case _:
                print('Invaild Input: Command out of range. Try again.')
                return 'menuStart'
    else:
        return command

def menuQuit():
    print('''
Are you sure you want to quit?

Y. Yes. Exit the program.
N. No. Go back to where I was.
R. Return to Main Menu.
H. Help
''')
    match input('>>>:')[0].lower():
        case 'y':
            exit()
        case 'n':
            return prevMenuPos
        case 'r':
            return 'menuStart'
        case 'h':
            return 'menuHelp'
        case _:
            print('Invalid Input! Try again.')
            return 'menuQuit'

def menuHelp():
    print('''
this is a game
regexz iz coolz
          
say gex
say gex really quick
swap g and s
say
          
press a key to continue.
''')
    if input('>>>:')[0].lower() == 'a':
        print('you got it')
    return prevMenuPos

def menuView(): #PLACEHOLDER
    for here in argDict:
        print(here,argDict[here])
    print('PLH-youre not supposed to see this function')
    print('Press a key to continue')
    input('>>>:')

def menuClassic():
    global prevMenuPos
    global argDict
    prevMenuPos = 'menuClassic'
    print('''
Select Difficulty Preset

1. Easy
2. Moderate
3. Challenging
4. Insane

H. Help
R. Return to previous Menu
E. Go to Main Menu
Q. Quit Game
''')
    command = clientInput(input('>>>:'))
    if command.isnumeric():
        match int(command):
            case 1:
                argDict = {
'penCorrect':True,'givenScore':0,
'givenTime':10,'randTime':1,'penTime':True,'randModeTime':0,
'givenChars':3,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':3,'randSections':0,'randModeSections':2,
'numPuzzles':5,'sectionTime':2}
                return 'menuSessionSetup'
            case 2:
                argDict = { # the
'penCorrect':True,'givenScore':0,
'givenTime':5,'randTime':1,'penTime':True,'randModeTime':0,
'givenChars':2,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':5,'randSections':1,'randModeSections':2,
'numPuzzles':10,'sectionTime':2}
                return 'menuSessionSetup'
            case 3: 
                argDict = { # the
'penCorrect':True,'givenScore':0,
'givenTime':3,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':1,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':6,'randSections':2,'randModeSections':2,
'numPuzzles':15,'sectionTime':1.2}
                return 'menuSessionSetup'
            case 4:
                argDict = { # the
'penCorrect':True,'givenScore':0,
'givenTime':1,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':0,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':8,'randSections':3,'randModeSections':2,
'numPuzzles':25,'sectionTime':1}
                return 'menuSessionSetup'
            case _:
                print('Invaild Input: Command out of range. Try again.')
                return 'menuStart'
    else:
        return command

def menuCustom():
    global prevMenuPos
    global argDict
    prevMenuPos = 'menuCustom'
    while True:
        print('''
1. Penalty Settings
2. Time Settings
3. Character Settings
4. Sections Settings
5. Duration of Game
6. Change Gamemode

V. View Current Settings     
S. Start Game
H. Help
E. Return to Main Menu
Q. Quit Game
''')
        prevMenuPos = 'menuCustom'
        command = clientInput(input('>>>:'))
        if command.isnumeric():
            match int(command):
                case 1:
                    command = setupCustomPen()
                case 2:
                    command = setupCustomTime()
                case 3: 
                    command = setupCustomChars()
                case 4:
                    command = setupCustomSections()
                case 5:
                    command = setupCustomDuration()
                case 6:
                    command = setupCustomModes()
                case _:
                    print('Invaild Input: Command out of range. Try again.')
                    return 'menuStart'
            if command != None:
                return command
        else:
            return command

# allows user to change specific variables/args
def setupCustomPen():
    print('1. Incorrect Answer Penalty:', argDict['penCorrect'])
    print('2. Exceed Time Limit Penalty:',argDict['penTime'])
    print('3. Exceed Char Limit Penalty:',argDict['penChars'])
    print('''

E. Return to previous menu.
H. General Help
Q. Quit Game
''')
    global argDict
    match input('>>>:')[0].lower():
        case '1':
            argDict['penCorrect'] = not argDict['penCorrect']
        case '2':
            argDict['penTime'] = not argDict['penTime']
        case '3':
            argDict['penChars'] = not argDict['penChars']
        case 'h':
            return 'menuHelp'
        case 'q':
            return 'menuQuit'
        case 'e':
            return
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
    global argDict
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
            return 'menuHelp'
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
    global argDict
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
            return 'menuHelp'
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
    global argDict
    match input('>>>:')[0].lower():
        case '1':
            argDict['givenChars'] = intinput(input('Input Number >>:'))
        case '2':
            argDict['penChars'] = not argDict['penChars']
        case 'e':
            return prevMenuPos
        case 'h':
            return 'menuHelp'
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
    global argDict
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
            return 'menuHelp'
        case 'q':
            return 'menuQuit'
        case _:
            print('Invalid Input!')
            return 
    return

def setupCustomModes():
    print('1. Toggle Gamemode:',argDict['gamemode'])
    print('Choices: 1. Classic, 2. Endless')
    print('2. Toggle Deathmode:',argDict['deathmode'])
    print('Choices: 1. None, 2. Score Countdown, 3. Time Countdown')
    print('''
          
E. Return to previous menu.
H. General Help
Q. Quit Game
''')
    global modeDict
    match input('>>>:')[0].lower():
        case '1':
            try:
                modeDict['gamemode'] = ('classic','endless')[intinput(input('Input Number >>:'))-1]
            except:
                print('Invaild Input! Defaulting to default (classic).')
                modeDict['gamemode'] = 'classic'
        case '2':
            try:
                modeDict['deathmode'] = ('none','scoredown','timedown')[intinput(input('Input Number >>:'))-1]
            except:
                print('Invaild Input! Defaulting to default (none)')
                modeDict['deathmode'] = 'none'
        case 'e':
            return
        case 'h':
            return 'menuHelp'
        case 'q':
            return 'menuQuit'
        case _:
            print('Invalid Input!')
            return 
    return


# GAME SECTION AREA
# start the game 
def menuSessionSetup(): #PLACEHOLDER
    print('load:',argDict)
    print('Current Settings:')
    print('Length of Expression:',argDict['numSections'])
    print('Number of Puzzles:',argDict['numPuzzles'])
    print('Gamemode:',modeDict['gamemode'])
    print('Deathmode:',modeDict['deathmode'])
    input('Press a key to start >>>:')

    result = gameSession(argDict,modeDict)
    return 'menuStart'

from time import time
def gameSession(argDict,modeDict):
    timeAnchorSession = time()
    score = argDict['givenScore']
    stats = {}
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
    for puzzlehere in range(argDict['numPuzzles']):
        print('Puzzle No.',puzzlehere) 
        totalSections = argDict['numSections']+rnd(randNamesFloor[2],randNamesCeil[2])
        theExObject = regexSectionConstructor(totalSections)
        theEx = listJoinery(theExObject['puzzle'])
        totalTime = argDict['givenTime']+rnd(randNamesFloor[0],randNamesCeil[0])+totalSections*argDict['sectionTime']
        totalChars = argDict['givenChars']+rnd(randNamesFloor[1],randNamesCeil[1])+totalSections
        localTimeAnchor = time()
        theAns = gamePlay(theEx,totalTime,argDict['penTime'],totalChars,argDict['penChars'])
        localStats = {'inCorrect':True,'inTime':True,'ansTime':0,'totalTime':totalTime,'inChars':True,'ansChars':len(theAns),'totalChars':totalChars,'theEx':theEx,'theAns':theAns}
        if re.match(theEx,theAns) == None:
            localStats['inCorrect'] = False
        if (localTimeAnchor-time())>totalTime:
            localStats['inTime'] = False
        if localStats['ansChars']>totalTime:
            localStats['inChars'] = False
            


# old
    # for iteration in range(0,argDict['numPuzzles']):
    #     print('Puzzle',iteration+1)
    #     puzzleResult = gamePlay(
    #             argDict['givenTime']+rnd(randNamesFloor[0],randNamesCeil[0]),
    #             argDict['givenChars']+rnd(randNamesFloor[1],randNamesCeil[1]),
    #             argDict['numSections']+rnd(randNamesFloor[2],randNamesCeil[2]),
    #             argDict['sectionTime']
    #             )
        
    #     score += 1
    #     if (not puzzleResult['correct']) and argDict['penCorrect']:
    #         score -= 1
    #         print('Incorrect Answer.')
    #     if (not puzzleResult['inChars']) and argDict['penChars']:
    #         score -= 1
    #         print('Exceeded Character Limit')
    #     if (not puzzleResult['inTime']) and argDict['penTime']:
    #         score -= 1
    #         print('Exceeded Time Limit')
        
    #     stats.append(puzzleResult)
    #     print(score)
    #     print(int(time()-timeAnchorSession))
    # return {'stats':stats,'score':score}



def gamePlay(theEx,timeGiven,penTime,charsGiven,penChars):
    if penTime:
        print('In',timeGiven,'seconds,')
    print('Solve /'+theEx+'/')
    if penChars:
        print('in',charsGiven,'characters.')
    return str(input('>>>:'))



from random import randint as rnd
from random import getrandbits
import re

# BACKEND DO NOT TOUCH 
# PNP - JUST CALL FUNCTION regexSectionConstructor-->dict['puzzle'], ['totalLength']

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


# gamemode: classic, endless, scenario, tutorial
# deathmode: none, scoredown, countdown(time) 
argDict = { 
    'penCorrect':True,'givenScore':0,
    'givenTime':0,'randTime':0,'penTime':False,'randModeTime':0,
    'givenChars':1,'randChars':0,'penChars':False,'randModeChars':1,
    'numSections':3,'randSections':0,'randModeSections':2,
    'numPuzzles':5,'sectionTime':2
    }
modeDict = {'gamemode':'classic','deathmode':'none'}
statsDict = None # populate this with something after 
prevMenuPos = 'menuStart'
currentMenuPos = 'menuStart'
while True:
    match currentMenuPos:
        case 'menuStart':
            currentMenuPos = menuStart()
        case 'menuQuit':
            currentMenuPos = menuQuit()
        case 'menuHelp':
            currentMenuPos = menuHelp()
        case 'menuClassic':
            currentMenuPos = menuClassic()
        case 'menuCustom':
            currentMenuPos = menuCustom()
        case 'menuTutorial':
            currentMenuPos = menuTutorial()
        case 'menuScenario':
            currentMenuPos = menuScenario() 
        case 'menuView':
            currentMenuPos = menuView()
        case 'menuSessionSetup':
            currentMenuPos = menuSessionSetup()
        case _:
            print('Invaild Input.')
            currentMenuPos = prevMenuPos
