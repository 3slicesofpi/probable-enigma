# BEGINNER CODE CHECKLIST
# - GLOBAL VARIABLES (4 at last count) TODO: REMOVE ALL OF THEM 
# - WHILE TRUE:
# - VARIABLE NAMES (lack thereof)
# - BIG LONG DICTS

# - at least classes are used



class menuConstructor():
    def __init__(self,menuName):
        self.menuName = menuName
        self.directory = {}
        # {key(etc: 1,2,H,Q): {'name':Monty's Menu,'goto':menuMonty},..}
    def addGlobalOptions(self):
        self.directory['H'] = {'name':'Get Help','goto':'viewHelp','type':'nav'}
        self.directory['R'] = {'name':'Return to Main Menu','goto':'menuMain','type':'nav'}
        if goback != 'mainMenu':
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
            userInput = input('>>>:')[0].upper() 
            for here in self.directory:
                if userInput == here: # first iteration
                    return self.directory[here]['goto']
            # try: # second iteration
            #     return self.directory[input('>>>:')[0].upper()]['goto']
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
    def inputHandler(self):
        while True:
            userInput = input('>>>:')[0].upper() 
            for here in self.directory:
                if userInput == here: # first iteration
                    match self.directory['type']: 
                        case 'nav':
                            self.directory[here]['goto']
                        case 'tog':    
                            # global args
                            args[self.directory['name']] = (not args[self.directory['name']])
                        case 'inp':
                            # global args
                            args[self.directory['name']] = int(input('Insert number>>>:'))             
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
    content = menuConstructor('menuMain')
    content.addNewOptions('Classic','mcqClassic')
    content.addNewOptions('Custom Game','menuCustom')
    content.addNewOptions('Other Gamemodes','mcqGamemode')
    content.addNewOptions('Tutorial','mcqTutorial')
    content.addGlobalOptions()
    content.viewDirectory()
    global goto
    global goback
    goback = 'menuMain'
    goto = content.inputHandler()

def menuCustom():
    content = menuConstructor('menuCustom')
    content.addNewOptions('General Settings','mcqArgsGeneral')
    content.addNewOptions('Penalty Settings','mcqArgsPen')
    content.addNewOptions('Time Settings','mcqArgsTime')
    content.addNewOptions('Character Settings','mcqArgsChars')
    content.addNewOptions('Difficulty Presets','mcqClassic')
    content.addGlobalOptions()
    content.viewDirectory()
    global goto
    global goback
    goback = 'menuCustom'
    goto = content.inputHandler()

def mcqArgsPen():
    content = mcqConstructor_args('mcqArgsPen')
    content.addNewTFToggle('Penalty fo Incorrect Answers','penCorrect')
    content.addNewTFToggle('Exceed Puzzle Time Limit Penalty','penTime')
    content.addNewTFToggle('Exceed Puzzle Character Limit Penalty','penChars')
    content.addGlobalOptions()
    content.viewDirectory
    global goto
    goto = content.inputHandler()

def mcqArgsTime():
    content = mcqConstructor_args('mcqArgsTime')
    content.addNewTFToggle('Exceed Puzzle Time Limit Penalty','penTime')
    content.addNewInputInt('Extra Time Per Game (s)','givenTime')
    content.addNewInputInt('Extra Time per Section (s)','sectionTime')
    content.addGlobalOptions()
    content.viewDirectory()
    global goto
    goto = content.inputHandler()

def mcqArgsChars():
    content = mcqConstructor_args('mcqArgsChars')
    content.addNewTFToggle('Exceed Puzzle Character Limit Penalty','penTime')
    content.addNewInputInt('Extra Characters Per Game','givenChars')
    content.addNewInputInt('Extra Characters per Section','sectionChars')
    content.addGlobalOptions()
    content.viewDirectory()
    global goto
    goto = content.inputHandler()

def mcqArgsGeneral():
    content = mcqConstructor_args('mcqArgsGeneral')
    content.addNewInputInt('Number of puzzles','numPuzzles')
    content.addNewInputInt('Number of Sections','numSections')
    content.addNewInputInt('Extra Score per Game','givenScore') 


def viewHelp():
    content = menuConstructor('viewHelp')
    print ('''
TODO populate this  
DO NOT FORGET!!!!11!!!
           
if u see this i forgor :skull::skull:
''')
    content.addCustomOptions('Go back to previous menu','E',goback)
    content.addCustomOptions('Return to Main Menu','R','menuMain')
    content.viewDirectory()
    global goto
    goto = content.inputHandler()

def viewQuit():
    content = menuConstructor('viewQuit')
    print('''
Are you sure you want to exit this program?
''')
    content.addCustomOptions('Yes. I want to quit.','Y','EXITFLAG')
    content.addCustomOptions('Go back to previous menu','E',goback)
    content.addCustomOptions('Return to Main Menu','R','menuMain')
    content.viewDirectory()
    global goto
    goto = content.inputHandler()
    if goto == 'EXITFLAG':
        print('Exiting Program... See you next time!')
        exit()
    else:
        return goto

def mcqClassic():
    content = menuConstructor('mcqClassic')
    content.addNewOptions('Easy Difficulty','1')
    content.addNewOptions('Medium Difficulty','2')
    content.addNewOptions('Hard Difficulty','3')
    content.addNewOptions('Insane Difficulty','4')
    content.addGlobalOptions()
    content.viewDirectory()
    inputCheck = content.inputHandler()
    global goto
    match inputCheck:
        case '1': #EZ
            # TODO
            global args
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
            global args
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
            global args
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
            global args
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

# TODO: unglobal the global variable
goback = 'menuMain'
goto ='menuMain'
while True:
    match goto:
        case 'menuMain':
            menuMain()
        case 'viewHelp':
            viewHelp()
        case 'viewQuit':
            viewQuit()
        case 'mcqClassic':
            mcqClassic()
        case 'menuCustom':
            menuCustom()
        case 'mcqGamemode':
            goto = goback
            # mcqGamemode()
        case 'mcqTutorial':
            goto = goback
            # mcqTutorial()
        case 'mcqArgsPen':
            mcqArgsPen()
        case 'mcqArgsTime':
            mcqArgsTime()
        case 'mcqArgsChars':
            mcqArgsChars()
        case 'mcqArgsGeneral':
            mcqArgsGeneral()



