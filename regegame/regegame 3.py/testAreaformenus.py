class menuConstructor():
    def __init__(self,menuName):
        self.menuName = menuName
        self.directory = {}
        # {key(etc: 1,2,H,Q): {'name':Monty's Menu,'goto':menuMonty},..}
    def addGlobalOptions(self):
        self.directory['H'] = {'name':'Get Help','goto':'viewHelp'}
        self.directory['R'] = {'name':'Return to Main Menu','goto':'menuMain'}
        # self.directory.append({'E':{'name':'Go back','goto':'menuMain'}}) #TODO
        self.directory['Q'] = {'name':'Quit Program','goto':'menuQuit'}

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
            for here in self.directory:
                if input('>>>:')[0].upper() == here:
                    return self.directory[here]['goto']
            print('Invalid input! Try Again.')

def menuMain():
    content = menuConstructor
    content.addNewOptions('Classic','menuClassic')
    content.addNewOptions('Custom Game','menuCustom')
    content.addNewOptions('Other Gamemodes','menuGamemode')
    content.addNewOptions('Tutorial','menuTutorial')
    content.viewDirectory()
    return {'goto':content.inputHandler()}


goto ='menuMain'
while True:
    match goto:
        case 'menuMain':
            infoObject = menuMain()
    
    goto = infoObject['goto']



