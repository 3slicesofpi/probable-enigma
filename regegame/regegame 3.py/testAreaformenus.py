# BEGINNER CODE CHECKLIST
# - WHILE TRUE:
# - VARIABLE NAMES (lack thereof)
# - BIG LONG DICTS

# - at least classes are used
# - f-strings TODO: make them all doublequotes



class menuConstructor():
    def __init__(self,menuName):
        self.menuName = menuName
        self.directory = {}
        # {key(etc: 1,2,H,Q): {'name':Monty's Menu,'goto':menuMonty},..}
    def addGlobalOptions(self):
        self.directory['H'] = {'name':'Get Help','goto':'viewHelp','type':'nav'}
        self.directory['R'] = {'name':'Return to Main Menu','goto':'menuMain','type':'nav'}
        self.directory['E'] = {'name':'Go back to previous menu','goto':goback,'type':'nav'}
        self.directory['Q'] = {'name':'Quit Program','goto':'viewQuit','type':'nav'}
        

    def addNewOptions(self,name,goto):
        # CALL THIS FIRST
        self.directory[str(len(self.directory)+1)] = {'name':name,'goto':goto,'type':'nav'}
    
    def viewDirectory(self):
        print(f'You are now at: {self.menuName}')
        print('')
        for here in self.directory:
            print(f"{here}. {self.directory[here]['name']}")

    def inputHandler(self):
        while True:
            userInput = input('Input a command >>>:')[0].upper() 
            for here in self.directory:
                if userInput == here: # first iteration
                    return self.directory[here]['goto']
            # try: # second iteration
            #     return self.directory[input('Input a command >>>:')[0].upper()]['goto']
            # except:
            #     print('Invalid input! Try Again.')

class mcqConstructor_args(menuConstructor):
    def __init__(self, menuName):
        super().__init__(menuName)
    def addGlobalOptions(self):
        return super().addGlobalOptions()
    def addNewOptions(self, name, goto):
        return super().addNewOptions(name, goto)
    def addNewTFToggle(self,name,target):
        self.directory[str(len(self.directory)+1)] = {'name':name,'goto':target,'type':'tog'}
    def addNewInputInt(self,name,target):
        self.directory[str(len(self.directory)+1)] = {'name':name,'goto':target,'type':'inp'}
    def viewDirectory(self):
        print(f'You are now at: {self.menuName}')
        print('')
        for here in self.directory:
            if self.directory[here]['type'] == 'nav':
                print(f"{here}. {self.directory[here]['name']}")
            else:
                print(f"{here}. {self.directory[here]['name']}: Current Value: {args[self.directory[here]['goto']]}")

    def inputHandler(self):
        while True:
            userInput = input('Input a command >>>:')[0].upper() 
            for here in self.directory:
                if userInput == here: # first iteration
                    match self.directory[here]['type']: 
                        case 'nav':
                            return self.directory[here]['goto']
                        case 'tog':
                            args[self.directory[here]['goto']] = (not args[self.directory[here]['goto']])
                            print(f"{self.directory[here]['goto']} is now {args[self.directory[here]['goto']]}")
                        case 'inp':
                            args[self.directory[here]['goto']] = int(input(f"Change {self.directory[here]['goto']} to >>>:"))             
args = dict(
    penCorrect = True, #penalties
    penTime = False,
    penChars = False,
    startingScore = 0, #given per game
    givenScore = 0,
    givenTime = 0,
    givenChars = 0,
    sectionTime = 0, #given per section
    sectionChars = 0,
    randTime = (0,0), #modifies sectionTime/sectionChars
    randChars = (0,0),
    randSections = (0,0),
    numSections = 5,
    numPuzzles = 5)

# class stats():
#     NotImplemented
# theStats = stats()

def menuMain():
    content = menuConstructor('Main Menu')
    content.addNewOptions('Classic','mcqClassic')
    content.addNewOptions('Custom Game','menuCustom')
    content.addNewOptions('Other Gamemodes','mcqGamemode')
    content.addNewOptions('Tutorial','mcqTutorial')
    content.directory['H'] = {'name':'Get Help','goto':'viewHelp'}
    content.directory['Q'] = {'name':'Exit Program','goto':'viewQuit'}
    content.viewDirectory()
    goback = 'menuMain'
    goto = content.inputHandler()
    return {'goto':goto,'goback':goback}

def menuCustom():
    content = menuConstructor('View and Edit Current Settings')
    content.addNewOptions('General Settings','mcqArgsGeneral')
    content.addNewOptions('Penalty Settings','mcqArgsPen')
    content.addNewOptions('Time Settings','mcqArgsTime')
    content.addNewOptions('Character Settings','mcqArgsChars')
    content.addNewOptions('Difficulty Presets','mcqClassic')
    content.directory['S'] = {'name':'Start Game using Current Settings','goto':'gameSetup'}
    content.addGlobalOptions()
    content.viewDirectory()
    goback = 'menuCustom'
    goto = content.inputHandler()
    return {'goto':goto,'goback':goback}

def mcqArgsPen():
    content = mcqConstructor_args('Penalty Settings')
    content.addNewTFToggle('Penalty for Incorrect Answers','penCorrect')
    content.addNewTFToggle('Exceed Puzzle Time Limit Penalty','penTime')
    content.addNewTFToggle('Exceed Puzzle Character Limit Penalty','penChars')
    content.addGlobalOptions()
    content.viewDirectory()
    return {'goto':content.inputHandler()}

def mcqArgsTime():
    content = mcqConstructor_args('Time Settings')
    content.addNewTFToggle('Exceed Puzzle Time Limit Penalty','penTime')
    content.addNewInputInt('Extra Time Per Game (s)','givenTime')
    content.addNewInputInt('Extra Time per Section (s)','sectionTime')
    content.addGlobalOptions()
    content.viewDirectory()
    return {'goto':content.inputHandler()}

def mcqArgsChars():
    content = mcqConstructor_args('Character Settings')
    content.addNewTFToggle('Exceed Puzzle Character Limit Penalty','penTime')
    content.addNewInputInt('Extra Characters Per Game','givenChars')
    content.addNewInputInt('Extra Characters per Section','sectionChars')
    content.addGlobalOptions()
    content.viewDirectory()
    return {'goto':content.inputHandler()}

def mcqArgsGeneral():
    content = mcqConstructor_args('General Settings')
    content.addNewInputInt('Number of puzzles','numPuzzles')
    content.addNewInputInt('Number of Sections','numSections')
    content.addNewInputInt('Extra Score per Game','givenScore') 
    content.addGlobalOptions()
    content.viewDirectory()
    return {'goto':content.inputHandler()}

def viewHelp():
    content = menuConstructor('Help Menu')
    print ('''
TODO populate this  
DO NOT FORGET!!!!11!!!
           
if u see this i forgor :skull::skull:
''')
    content.directory['E'] = {'name':'Go back to previous menu','goto': goback}
    content.directory['R'] = {'name':'Return to Main Menu','goto':'menuMain'}
    content.viewDirectory()
    return {'goto':content.inputHandler()}

def viewQuit():
    content = menuConstructor('Exit Menu')
    print('''
Are you sure you want to exit this program?
''')
    content.directory['Y'] = {'name':'Yes. I want to quit.','goto':'EXITFLAG'}
    content.directory['E'] = {'name':'Go back to previous menu','goto':goback}
    content.directory['R'] = {'name':'Return to Main Menu','goto':'menuMain'}
    content.viewDirectory()
    goto = content.inputHandler()
    if goto == 'EXITFLAG':
        print('Exiting Program... See you next time!')
        exit()
    else:
        return {'goto':goto}

def mcqClassic():
    args = None
    content = menuConstructor('Difficulty Select')
    content.addNewOptions('Easy Difficulty','1')
    content.addNewOptions('Medium Difficulty','2')
    content.addNewOptions('Hard Difficulty','3')
    content.addNewOptions('Insane Difficulty','4')
    content.addGlobalOptions()
    content.viewDirectory()
    inputCheck = content.inputHandler()
    match inputCheck:
        case '1': #EZ
            args = dict(
    penCorrect = True, #penalties
    penTime = True,
    penChars = True,
    startingScore = 0, #given per game
    givenScore = 0, #given per puzzle
    givenTime = 3,
    givenChars = 3,
    sectionTime = 5, #given per section
    sectionChars = 2,
    randTime = (0,0), #modifies sectionTime/sectionChars
    randChars = (0,0),
    randSections = (0,1),
    numSections = 3,
    numPuzzles = 5)
            if goback == 'menuCustom': #coming from mcqPresets
                goto = goback
            else:
                goto = 'gameSetup'
        case '2': #MADOROTE
            args = dict(
    penCorrect = True, #penalties
    penTime = True,
    penChars = True,
    startingScore = 0, #given per game
    givenScore = 0, #given per puzzle
    givenTime = 2,
    givenChars = 1,
    sectionTime = 2, #given per section
    sectionChars = 1,
    randTime = (0,0), #modifies sectionTime/sectionChars
    randChars = (0,0),
    randSections = (1,2),
    numSections = 4,
    numPuzzles = 5)
            if goback == 'menuCustom': #coming from mcqPresets
                goto = goback
            else:
                goto = 'gameSetup'
        case '3': #HORD
            args = dict(
    penCorrect = True, #penalties
    penTime = True,
    penChars = True,
    startingScore = 0, #given per game
    givenScore = 0, #given per puzzle
    givenTime = 2,
    givenChars = 1,
    sectionTime = 1, #given per section
    sectionChars = 1,
    randTime = (0,0), #modifies sectionTime/sectionChars
    randChars = (0,0),
    randSections = (2,2),
    numSections = 5,
    numPuzzles = 10)
            if goback == 'menuCustom': #coming from mcqPresets
                goto = goback
            else:
                goto = 'gameSetup'
        case '4': #INSAME
            args = dict(
    penCorrect = True, #penalties
    penTime = True,
    penChars = True,
    startingScore = 0, #given per game
    givenScore = 0, #given per puzzle
    givenTime = 1,
    givenChars = 0,
    sectionTime = 0, #given per section
    sectionChars = 0,
    randTime = (0,0), #modifies sectionTime/sectionChars
    randChars = (0,0),
    randSections = (1,3),
    numSections = 5,
    numPuzzles = 15)
            if goback == 'menuCustom': #coming from mcqPresets
                goto = goback
            else:
                goto = 'gameSetup'
        case _: #^above are exceptions
            goto = inputCheck
    if args != None:
        return {'goto':goto,'goback':goback,'args':args}
    else:
        return {'goto':goto,'goback':goback}

def gameSetup():
    print('Current Settings')
    for here in args:
        print(f"{here}:{args[here]}")
    return {'goto':goback}

# TODO: unglobal the global variable
goback = 'menuMain'
goto ='menuMain'
while True:
    match goto:
        case 'menuMain':
            menuInfo = menuMain()
        case 'viewHelp':
            menuInfo = viewHelp()
        case 'viewQuit':
            menuInfo = viewQuit()
        case 'mcqClassic':
            menuInfo = mcqClassic()
        case 'menuCustom':
            menuInfo = menuCustom()
        case 'mcqGamemode':
            goto = goback
            # mcqGamemode()
        case 'mcqTutorial':
            goto = goback
            # mcqTutorial()
        case 'mcqArgsPen':
            menuInfo = mcqArgsPen()
        case 'mcqArgsTime':
            menuInfo = mcqArgsTime()
        case 'mcqArgsChars':
            menuInfo = mcqArgsChars()
        case 'mcqArgsGeneral':
            menuInfo = mcqArgsGeneral()
        case 'gameSetup':
            menuInfo = gameSetup()
    if 'goto' in menuInfo:
        goto = menuInfo['goto']
    if 'goback' in menuInfo:
        goback = menuInfo['goback']
    if 'args' in menuInfo: #TODO: modify args line by line.
        args = menuInfo['args']
    if 'stats' in menuInfo:
        stats = menuInfo['stats']


