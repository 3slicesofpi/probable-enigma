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
            case 2:
                # [a-c]
                puzzle.append(integratedFactoryAndValidator())
            case 3:
                # [A-c]
                puzzle.append('[')
                if randint(1,2) == 1:
                    puzzle.append('^')
                puzzle.append(textFactory(2))
                puzzle.append('-')
                puzzle.append(textFactory(1))
                puzzle.append(']')
            case 4:
                # a
                textLength = randint(1,5)
                match randint(1,3):
                    case 1:
                        for jteration in range(0,textLength):
                            puzzle.append(textFactory(randint(1,4)))
                    case 2:
                        textLength += 1
                        puzzle.append('(')
                        for jteration in range(0,textLength):
                            puzzle.append(textFactory(randint(1,3)))
                        puzzle.append(')')
                    case 3:
                        textLength += 1
                        puzzle.append('[')
                        for jteration in range(0,textLength):
                            puzzle.append(textFactory(randint(1,4)))
                        puzzle.append(']')
        match randint(1,4):
            case 1:
                match randint(1,4): 
                    case 1:
                        puzzle.append('+')
                    case 2:
                        puzzle.append('?')
                    case 3:
                        puzzle.append('*')
                    case 4:
                        puzzle.append('')
            case 2: # nothing
                pass
            case 3:
                puzzle.append('.')
            case 4:
                puzzle.append('{')
                puzzle.append(str(randint(0,3)))
                puzzle.append('}')
    return puzzle

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


# finalPuzzle = listJoinery(regexSectionConstructor(3))
# print('/'+finalPuzzle+'/')
# answer = input('answer>>>:')
# if re.match(finalPuzzle,answer) != None:
#     print('Correct!')
# else:
#     print('wrong. answer.')
def gameEngine(menuState):
    match menuState:
        case 'introMenu':
            print('''
/regular game/ is a game about solving regex puzzles. Are you up for the challenge?
/n
/n
/i Press any key except 'e' to continue.
                  ''')
            if input('>>>:') == 'e':
                return 'exit' 
            else:
                return 'startMenu'
        case 'exit':
            print('''
/m exit
/n
/n
/t Goodbye!
                  ''')
            exit()
            print('/error exit() failed to end program. Try Again.')
            return
        case 'startMenu':
            print('''
/m start
/n
/c -game
''')
            gameLevelLength = int(input('/i select number of levels >>>:'))
            print('/c &lvlen:',str(gameLevelLength))
            gameExpressionLength = int(input('/i select length of expression >>>:'))
            print('/c &exlen:',str(gameExpressionLength))
            print('/n')
            print('/t starting game...')
            score = 0
            for level in range(1,gameLevelLength):
                print('/n')
                print('/t',level)
                theExpression = listJoinery(regexSectionConstructor(gameExpressionLength))
                print('/t Solve: /'+theExpression+'/')
                answer = input('/i Your Answer >>>:' )
                if re.match(theExpression,answer) != None:
                    print('Correct!')
                    score += 1
                else:
                    print('wrong. answer.')
            print('/t final score =',str(score)+'/'+str(gameLevelLength))
            if score == gameLevelLength:
                print('/t Decoder Dominus! Victory is yours this day.')
            elif score == 0:
                print('regex reject. Tray again next time.')
            else:
                print('not bad. But you can do better.')
            return 'startMenu'

            


menuState = 'introMenu'
while True:
    menuState = gameEngine(menuState)


