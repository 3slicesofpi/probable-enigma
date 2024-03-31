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
        self.directory[str(len(self.directory)+1)] = {'name':name,'goto':goto}
    
    def addCustomOptions(self,name,pos,goto):
        self.directory[pos] = {'name':name,'goto':goto}

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

class gameArgsConstructor(menuConstructor):
    # figure out how to set new target
    def addNewOptions(self, name, goto):
        # CALL THIS FIRST
        self.directory[str(len(self.directory)+1)] = {'name':name,'goto':goto,'type':'nav'}
    def addNewMultiChoice(self, name, goto):
        # CALL THIS FIRST
        self.directory[str(len(self.directory)+1)] = {'name':name,'goto':goto,'type':'mcq'}
    def addNewTFToggle(self, name, goto):
        # CALL THIS FIRST
        self.directory[str(len(self.directory)+1)] = {'name':name,'goto':goto,'type':'tog'}
    def addCustomOptions(self, name, pos, goto, type):
        self.directory[pos] = {'name':name,'goto':goto,'type':type}
    def inputHandler(self):
        while True:
            userInput = input('>>>:')[0].upper() 
            for here in self.directory:
                if userInput == here: # first iteration
                    match self.directory[here]['type']:
                        case 'nav':
                            return self.directory[here]['goto']
                        case 'mcq':
                            global gameArgs
                            try:
                                gameArgs['goto'] = int(input('>>>:'))
                            except:
                                print('Invalid Input.')
                        case 'tog':
                            global gameArgs
                            gameArgs['goto'] = (not gameArgs['goto'])
    

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
        case '1':
            global gameArgs
            gameArgs = {}# blah blah blah
            if goback == 'menuCustom': #coming from mcqPresets
                goto = goback
            else:
                goto = 'gameSetup'
        case '2':
            global gameArgs
            gameArgs = {}# blah blah blah
            if goback == 'menuCustom': #coming from mcqPresets
                goto = goback
            else:
                goto = 'gameSetup'
        case '3':
            global gameArgs
            gameArgs = {}# blah blah blah
            if goback == 'menuCustom': #coming from mcqPresets
                goto = goback
            else:
                goto = 'gameSetup'
        case '4':
            global gameArgs
            gameArgs = {}# blah blah blah
            if goback == 'menuCustom': #coming from mcqPresets
                goto = goback
            else:
                goto = 'gameSetup'
        case _:
            goto = inputCheck
            
        

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



