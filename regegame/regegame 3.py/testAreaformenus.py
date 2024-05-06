# BEGINNER CODE CHECKLIST
# - WHILE TRUE:
# - VARIABLE NAMES (lack thereof)
# - BIG LONG DICTS

# - at least classes are used
# - f-strings TODO: make them all doublequotes

from time import time
from random import randint as rnd
from random import getrandbits
import re
from time import time

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
    numPuzzles = 6,
    puzzleStart = ('you','are','playing','on','default','settings'), # add these to the start of theEx.
    puzzleEnd = ('h','e','L','l','0','!'),
    puzzleDesc = None, #TODO
    gamemode = 'classic',
    deathmode = 'none')

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
    randTime = [0,0], #modifies sectionTime/sectionChars
    randChars = [0,0],
    randSections = [0,1],
    numSections = 3,
    numPuzzles = 5,
    puzzleStart = None,
    puzzleEnd = None,
    puzzleDesc = None,
    gamemode = 'classic',
    deathmode = 'none')
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
    randTime = [0,0], #modifies sectionTime/sectionChars
    randChars = [0,0],
    randSections = [1,2],
    numSections = 4,
    numPuzzles = 5,
    puzzleStart = None,
    puzzleEnd = None,
    puzzleDesc = None,
    gamemode = 'classic',
    deathmode = 'none')
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
    randTime = [0,0], #modifies sectionTime/sectionChars
    randChars = [0,0],
    randSections = [2,2],
    numSections = 5,
    numPuzzles = 10,
    puzzleStart = None,
    puzzleEnd = None,
    puzzleDesc = None,
    gamemode = 'classic',
    deathmode = 'none')
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
    randTime = [0,0], #modifies sectionTime/sectionChars
    randChars = [0,0],
    randSections = [1,3],
    numSections = 5,
    numPuzzles = 15,
    puzzleStart = None,
    puzzleEnd = None,
    puzzleDesc = None,
    gamemode = 'classic',
    deathmode = 'none')
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

def gameSetup(): #PLACEHOLDER
    print('load:',args)
    print('Current Settings:')
    print('Length of Expression:',args['numSections'])
    print('Number of Puzzles:',args['numPuzzles'])
    print('Gamemode:',args['gamemode'])
    print('Deathmode:',args['deathmode'])
    placeholder = input('Press a key to start >>>:')
    try:
        placeholder = int(placeholder)
    except:
        placeholder = 0
    for here in ('randTime','randChars','randSections'):
        match placeholder:
            case 1: #addonly 
                args[here][0] = 1
                args[here][1] = 0
            case 2: #minusonly 
                args[here][0] = 0
                args[here][1] = -1
            case 3: #reducedminus
                args[here][0] = 1
                args[here][1] = -1
            case 4: #add add 
                args[here][0] = 2
                args[here][1] = 1
            case 5: #reducedadd 
                args[here][0] = 1
                args[here][1] = -1
    result = gameSession()
    totalScore = 0
    for here in result:
        totalScore += result[here]['score']
        print(f"/{result[here]['theEx']}/ <-- {result[here]['theAns']} Correct? {result[here]['ansCorrect']}")
    print(totalScore)
    return {'goto':'menuMain','stats':result}

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
                # do nothing
                # plh
                pass
        totalLength += sectionLength
        theQuota[numQuota] = {'type':sectionType,'textFactoryMode':textFactoryMode,'sectionLength':sectionLength}
    return {'puzzle':theEx, 'sectionLength':totalLength, 'totalLength':totalLength} #to maintain compatiablilty


def gameSession():
    timeAnchorSession = time()
    stats = []
    # MOVE THESE TO ANOTHER AREA
    #time, chars, sections
    # randNamesFloor = [0,0,0]
    # randNamesCeil = [0,0,0]
    # randNamesMode = (args['randModeTime'],args['randModeChars'],args['randModeSections'])
    # randNamesQuantity = (args['randTime'],args['randChars'],args['randSections'])
    # for randSelected in range(3):
    #     if randNamesQuantity[randSelected]>0:
    #         match randNamesMode[randSelected]:
    #             case 0: # default
    #                 randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
    #                 randNamesCeil[randSelected] = randNamesQuantity[randSelected]
    #             case 1: # addonly
    #                 # randNamesFloor[randSelected] = 0
    #                 randNamesCeil[randSelected] = randNamesQuantity[randSelected]
    #             case 2: # minusonly
    #                 randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
    #                 # randNamesFloor[randSelected] = 0
    #             case 3: # reduced minus
    #                 randNamesFloor[randSelected] = 1-randNamesQuantity[randSelected]
    #                 randNamesCeil[randSelected] = randNamesQuantity[randSelected]
    #             case 4: # additional add
    #                 randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
    #                 randNamesCeil[randSelected] = 1+randNamesQuantity[randSelected]
    #             case 5: # reduced add
                    # randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    # randNamesCeil[randSelected] = randNamesQuantity[randSelected]-1
    puzzleNum = -1
    if args['gamemode'] == 'endless':
        totalScore = 10
        args['numPuzzles'] = 256
    else:
        totalScore = 0
    killswitch = False
    # for here in ('puzzleStart','puzzleEnd','puzzleDesc'):
    #         if args[here] == None:
    #             for iteration in range(args['numPuzzles']):
    #                 args[here][iteration] = ''
    while (puzzleNum < args['numPuzzles']):  #or killswitch):
        if killswitch: # i guess python hates non-pythonic code? it dont work
            # use this to ensure killswitch kills gameSession
            return stats
        puzzleNum += 1
        print('puzzle no.:',(puzzleNum+1))
        # compute totals
        totalSections = args['numSections']+rnd(args['randSections'][0],args['randSections'][1])
        totalTime = args['givenTime']+rnd(args['randTime'][0],args['randTime'][0])+totalSections*args['sectionTime']
        theEx = regexSectionConstructor(totalSections)
        theEx['puzzle'] = listJoinery(theEx['puzzle'])
        totalChars = args['givenChars']+rnd(args['randChars'][1],args['randChars'][1])+theEx['totalLength']
        if args['penTime']:
            print('In',totalTime,'seconds,')
        print('Solve /'+theEx['puzzle']+'/')
        if args['penChars']:
            print('using',totalChars,'characters')
        timeAnchorLocal = time()
        theAns = input('>>>:')

        # count penalties and tally stats
        localStats = {'score':args['givenScore']+1,'ansCorrect': True,'theAns':theAns,'theEx':theEx['puzzle'],'ansTime':time()-timeAnchorLocal,'totalTime':totalTime,'totalChars':totalChars}
        if re.match(theEx['puzzle'],theAns) == None: #wrong
            print('Incorrect Answer.')
            localStats['ansCorrect'] = False
            if args['penCorrect']:
                localStats['score']-=2
        if args['penTime']:
            if localStats['ansTime']>=totalTime:
                localStats['score']-=1
                print('Exceeded Time Limit of',totalTime,'; You took',localStats['ansTime'],'seconds')
        if args['penChars']:
            if len(theAns)>totalChars:
                localStats['score']-=1
                print('Exceeded character Limit of',totalChars,'; Your answer was',len(theAns),'long.')
        totalScore += localStats['score']
        stats.append(localStats)

        # check whether to end the game
        # match args['deathmode']:
        #     case 'none':
        #         pass
        #     case 'scoredown':
        #         if totalScore <=0:
        #             print('Out of Score!')
        #             killswitch = True
        #         elif totalScore <=3:
        #             print('You only have',totalScore,'score left.')
        #     case 'timedown':
        #         timeAnchorSession += totalTime
        #         if time()>timeAnchorSession:
        #             print('Out of time!')
        #             killswitch = True
        #         else:
        #             print('Total time Left (Estimated):'-int(time()-timeAnchorSession)+args['givenTime']+(args['numSections']*args['sectionTime']))
        
    return stats
        

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


