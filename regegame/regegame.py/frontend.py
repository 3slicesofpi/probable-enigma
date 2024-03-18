argDict = { # the
    'penCorrect':True,'givenScore':0,
    'givenTime':0,'randTime':0,'penTime':False,'randModeTime':0,
    'givenChars':1,'randChars':0,'penChars':False,'randModeChars':1,
    'numSections':3,'randSections':0,'randModeSections':2,
    'numPuzzles':5
    }

def menuStart():
    print('''
REGEGAME PROTOTYPE
BASIC CLIENT

1. Classic
2. Endless
3. Custom
4. Custom Endless

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
'numPuzzles':5
            }
        case '2':
            return { # the
'penCorrect':True,'givenScore':0,
'givenTime':5,'randTime':1,'penTime':True,'randModeTime':0,
'givenChars':2,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':5,'randSections':1,'randModeSections':2,
'numPuzzles':10
            }
        case '3':
            return { # the
'penCorrect':True,'givenScore':0,
'givenTime':3,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':1,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':6,'randSections':2,'randModeSections':2,
'numPuzzles':15
            }
        case '4':
            return { # the
'penCorrect':True,'givenScore':0,
'givenTime':1,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':0,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':8,'randSections':3,'randModeSections':2,
'numPuzzles':25
            }
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
'numPuzzles':255
            }
            
        case '2':
            return { # the
'penCorrect':True,'givenScore':10,
'givenTime':5,'randTime':1,'penTime':True,'randModeTime':0,
'givenChars':2,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':5,'randSections':1,'randModeSections':2,
'numPuzzles':255
            }
        case '3':
            return { # the
'penCorrect':True,'givenScore':5,
'givenTime':3,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':1,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':6,'randSections':2,'randModeSections':2,
'numPuzzles':255
            }
        case '4':
            return { # the
'penCorrect':True,'givenScore':5,
'givenTime':1,'randTime':0,'penTime':True,'randModeTime':0,
'givenChars':0,'randChars':0,'penChars':True,'randModeChars':1,
'numSections':8,'randSections':3,'randModeSections':2,
'numPuzzles':255
            }
        case 'h':
            return 'menuAllHelp'
        case 'e':
            return 'menuQuit'
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

R. Return to previous menu.
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



def menuAllHelp():
    print('a')
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


# working area
gotoMenu = 'menuStart'
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
        case None:
            exit()
        case _:
            print(gotoMenu)
            print('a')
            exit()
            # gotoMenu = gameSession()