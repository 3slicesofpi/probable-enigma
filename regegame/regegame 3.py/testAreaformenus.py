class menuConstructor():
    def __init__(self,menuName):
        self.menuName = menuName
        self.directory = {}
        # {key(etc: 1,2,H,Q): {'name':Monty's Menu,'goto':menuMonty},..}
    def addGlobalOptions(self):
        self.directory['H'] = {'name':'Get Help','goto':'viewHelp'}
        self.directory['R'] = {'name':'Return to Main Menu','goto':'menuMain'}
        if goback != 'mainMenu':
            self.directory['E'] = {'name':'Go back to previous menu','goto':goback}
        self.directory['Q'] = {'name':'Quit Program','goto':'viewQuit'}

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

class mcqConstructor(menuConstructor):
    # think over it
    pass

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
    content.addNewOptions('Difficulty Presets','mcqArgsPresets')
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
            mcqGamemode()
        case 'mcqTutorial':
            mcqTutorial()



