from random import randint
import re
def integratedFactoryAndValidator():
    textFactoryMode = randint(1,2)
    localValidation = 0
    while localValidation == 0:
        try:
            negatoryFlag = ''
            if randint(1,2) == 1:
                negatoryFlag = '^'
            testExpression = '['+negatoryFlag+textFactory(textFactoryMode)+'-'+textFactory(textFactoryMode)+']'
            re.findall(testExpression,'a')
        except re.error:
            localValidation = -1
        finally:
            localValidation += 1
    return testExpression

def regexSectionConstructor(puzzleLength):
    puzzle = []
    sectionLength = 0
    textFactoryMode = None
    for iteration in range(0,puzzleLength):
        match randint(1,4):
            case 1:
                # [abc]
                textFactoryMode = randint(1,5)
                puzzle.append('[')
                if randint(1,2) == 1:
                    puzzle.append('^')
                for jteration in range(0,randint(1,5)):
                    puzzle.append(textFactory(textFactoryMode))
                puzzle.append(']')
                sectionLength += 1
            case 2:
                # [a-c]
                puzzle.append(integratedFactoryAndValidator())
                sectionLength += 1
            case 3:
                # [A-c]
                puzzle.append('[')
                if randint(1,2) == 1:
                    puzzle.append('^')
                puzzle.append(textFactory(2))
                puzzle.append('-')
                puzzle.append(textFactory(1))
                puzzle.append(']')
                sectionLength += 1
            case 4:
                # a
                textLength = randint(1,5)
                match randint(1,3):
                    case 1:
                        for jteration in range(0,textLength):
                            puzzle.append(textFactory(randint(1,4)))
                        sectionLength += textLength
                    case 2:
                        textLength += 1
                        puzzle.append('(')
                        for jteration in range(0,textLength):
                            puzzle.append(textFactory(randint(1,3)))
                        puzzle.append(')')
                        sectionLength += textLength
                    case 3:
                        textLength += 1
                        puzzle.append('[')
                        for jteration in range(0,textLength):
                            puzzle.append(textFactory(randint(1,4)))
                        puzzle.append(']')
                        if randint(1,2) ==2:
                            sectionLength += textLength-1
                        else:
                            sectionLength += 2
        match randint(1,4):
            case 1:
                match randint(1,4): 
                    case 1:
                        puzzle.append('+')
                    case 2:
                        puzzle.append('?')
                        if randint(1,2) == 1:
                            sectionLength -= 1
                    case 3:
                        puzzle.append('*')
                        if randint(1,2) == 1:
                            sectionLength -= 1
                    case 4:
                        puzzle.append('')
            case 2: # nothing
                pass
            case 3:
                puzzle.append('.')
                sectionLength += 1
            case 4:
                quantifier = randint(0,3)
                puzzle.append('{')
                puzzle.append(str(quantifier))
                puzzle.append('}')
                sectionLength += quantifier*sectionLength
    return [puzzle, sectionLength]

textTuple = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numberTuple = ('0','1','2','3','4','5','6','7','8','9')
symbolTuple = ('!','#','%',':',';','<','>','=','_','~') 
def textFactory(mode):
    match mode:
        case 1: # a-z
            textPos = randint(0,25)
            finalSolution = (textTuple[textPos])
        case 2: # A-Z
            textPos = randint(0,25)
            finalSolution = (textTuple[textPos].upper())
        case 3: # 0-9
            textPos = randint(0,9)
            finalSolution = (numberTuple[textPos])
        case 5: # symbols
            textPos = randint(0,9)
            finalSolution = (symbolTuple[textPos])
        case 4: # \s
            textPos = 0
            finalSolution = ' '
        
    return str(finalSolution)
                
def listJoinery(rawList):
    joinedString = ''
    for element in rawList:
        joinedString = joinedString+str(element)
    return joinedString

def menuIntro():
    print('press any key except "e"(which exits the game) "h"(which gets help)')
    try:
        match input('>>>:').lower()[0]:
            case 'e':
                return 'menuExit'
            case 'h':
                return 'menuHelp'
    except:
        print('fail')
        return 'menuExit'
    return 'menuMain'

def menuMain():
    print('select difficulty(how forgiving the game will be)')
    global difficulty
    difficulty = 1
    try:
        match input('>>>:').lower()[0]:
            case 'e':
                return 'menuExit'
            case 'h':
                return 'menuHelp'
            case '1':
                difficulty = 1
                return 'menuStart'
            case '2':
                difficulty = 2
                return 'menuStart'
            case '3':
                difficulty = 3
                return 'menuStart'
    except:
        print('fail')
        return 'menuExit'
    return 'menuMain'

def menuStart():
    try:
        numofRepeats = int(input('repeats (how many times you want to play.)>>>:'))
        numofSections = int(input('sections (how long your regex will be.)>>>:'))
        if (numofRepeats < 0) or (numofSections < 0):
            numofRepeats = symbolTuple[100] # cause an error
    except:
        print('fail')
        numofRepeats = 0
        numofSections = 0
        return 'menuStart'
    score = 0
    for puzzleNum in range(1,numofRepeats):
        print('puzzle no.'+str(puzzleNum))
        theExpression = regexSectionConstructor(numofSections)
        theExpression[0] = listJoinery(theExpression[0])
        match difficulty:
            case 1:
                theExpression[1] = theExpression[1]*2 +3
            case 2:
                theExpression[1] += 3
            case 3:
                theExpression[1] += 1
        print('Solve: /'+theExpression[0]+'/ in',theExpression[1],'charcters')
        answer = input('/i Your Answer >>>:' )
        score += 1
        if re.match(theExpression[0],answer) != None:
            print('Match! Your answer satisfies the regex.')
        else:
            print('Your answer does not satisfy the regex.')
            score -= 1
        if len(answer) > theExpression[1]:
            print('Your answer was too long. It needs to be',theExpression[1],'long')
            score -= 1
    print(score,'/',numofRepeats)
    return 'menuMain'

def menuHelp():
    print('''
welcome to reggame prototype.

    MENUS
You can access the help menu from anywhere in the program except when the game is running.
Just press 'h'.
Same with exiting the program
Just press 'e'.
          
    GAME
this is a regex game.
you will be given a regular expression.
Create a string of characters to satisfy the experssion to win.  
Successful matches give one point.
Exceeding the prescribed number of characters results in the deduction of points    

SCROLL UP TO READ''')
    
    return 'menuMain'

def mainLoop(menuState):
    match menuState:
        case 'menuExit':
            print('exit')
            print('have a nice day')
            exit()
        case 'menuIntro':
            return menuIntro()
        case 'menuMain':
            return menuMain()
        case 'menuStart':
            return menuStart()
        case 'menuHelp':
            return menuHelp()

menuState = 'menuIntro'    
while True:
    menuState = mainLoop(menuState)