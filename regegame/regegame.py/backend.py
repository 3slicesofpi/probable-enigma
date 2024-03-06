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
    return {'puzzle':puzzle, 'sectionLength':sectionLength}

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

def gameSession(numRepeats,numSections,maxAnsLen):
    score = 0
    for iteration in range(0,numRepeats):
        # creating puzzle...
        print('puzzle no.'+str(iteration+1))
        theExpression = regexSectionConstructor(numSections)
        theExpression['puzzle'] = listJoinery(theExpression['puzzle'])
        match maxAnsLen:
            case 0:
                theExpression['sectionLength'] = int(theExpression['sectionLength']*3.5)-3
            case 1:
                theExpression['sectionLength'] = int(theExpression['sectionLength']*1.5)-1
            case 2:
                theExpression['sectionLength'] = int(theExpression['sectionLength']*1.2)+1
            case 3:
                theExpression['sectionLength'] += 1
        print('Solve: /'+theExpression['puzzle']+'/ in',theExpression['sectionLength'],'charcters')
        answer = input('/i Your Answer >>>:' )
        
        # validating answer...
        score += 1
        if re.match(theExpression['puzzle'],answer) != None:
            print('Match! Your answer satisfies the regex.')
        else:
            print('Your answer does not satisfy the regex.')
            print('a point has been deducted.')
            score -= 1
        if len(answer) > theExpression['sectionLength']:
            print('Your answer was too long at',len(answer),'characters long.')
            print('It should be',theExpression['sectionLength'],'characters long.')
            print('a point has been deducted.')
    
    # puzzle done
    print("This session's final score:",str(score)+'/'+str(numRepeats))

gameSession(4,1,2)