
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
                case _:
                    print('Invaild Input: Command out of range. Try again.')
                    return 'menuStart'
            if command != None:
                return command
        else:
            return command


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
    return



def menuSessionSetup(): #PLACEHOLDER
    print(argDict)
    return 'menuStart'

argDict = { 
    'penCorrect':True,'givenScore':0,
    'givenTime':0,'randTime':0,'penTime':False,'randModeTime':0,
    'givenChars':1,'randChars':0,'penChars':False,'randModeChars':1,
    'numSections':3,'randSections':0,'randModeSections':2,
    'numPuzzles':5,'sectionTime':1
    }
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
