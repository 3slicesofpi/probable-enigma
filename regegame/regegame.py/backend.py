from random import randint
from time import time
import re

textTuple = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numberTuple = ('0','1','2','3','4','5','6','7','8','9')
symbolTuple = ('!','#','%',':',';','<','>','=','_','~') 
def integratedFactoryAndValidator():
    textFactoryMode = randint(1,2)
    localValidation = 0
    while localValidation == 0:
        try:
            negatoryFlag = ''
            if randint(1,2) == 1:
                negatoryFlag = '^'
            char2 = randint(1,25)
            char1 = randint(0,char2-1)
            if randint(1,2) == 1:
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

def regexSectionConstructor(puzzleLength):
    puzzle = []
    totalLength = 0
    textFactoryMode = None
    for iteration in range(0,puzzleLength):
        sectionLength = 0
        matchNumRand = randint(0,100)
        blacklist = []
        match True:
            case True if matchNumRand in range(0,24):
                #[abc]
                puzzle.append('[')
                if randint(1,2) == 1:
                    puzzle.append('^')
                textFactoryMode = randint(0,100)
                if textFactoryMode in range(0,34):
                    textFactoryMode = 1 #a
                elif textFactoryMode in range(35,54):
                    textFactoryMode = 2 #A
                elif textFactoryMode in range(55,84):
                    textFactoryMode = 3 #1
                else:
                    if randint(1,5)<=2:
                        textFactoryMode = 4 #%
                    else:
                        textFactoryMode = 5 #/s

                for iteration in range(0,randint(1,4)):
                    puzzle.append(textFactory(textFactoryMode,blacklist))
                    blacklist.append(puzzle[-1])
                puzzle.append(']')
                
            case True if matchNumRand in range(25,44):
                #[a-c]
                puzzle.append(integratedFactoryAndValidator())
                sectionLength += 1
            case True if matchNumRand in range(45,64):
                #[A-c]
                puzzle.append('[')
                if randint(1,2) == 1:
                    puzzle.append('^')
                puzzle.append(textFactory(2,blacklist))
                puzzle.append('-')
                puzzle.append(textFactory(1,blacklist))
                puzzle.append(']')
                sectionLength += 1
            case True if matchNumRand in range(65,100):
                #abc
                textFactoryMode = randint(0,100)
                if textFactoryMode in range(0,34):
                    textFactoryMode = 1 #a
                elif textFactoryMode in range(35,54):
                    textFactoryMode = 2 #A
                elif textFactoryMode in range(55,84):
                    textFactoryMode = 3 #1
                else:
                    textFactoryMode = 4 #/s
                match randint(1,2):
                    case 1:
                        #(abc)
                        puzzle.append('(')
                        if randint(1,2) == 1:
                            puzzle.append('^')
                        matchNumRand = randint(0,100) #watch out
                        if matchNumRand in range(0,23):
                            sectionLength = 1
                        elif matchNumRand in range(35,69):
                            sectionLength = 2
                        elif matchNumRand in range(70,84):
                            sectionLength = 3
                        elif matchNumRand in range(85,94):
                            sectionLength = 4
                        else: 
                            sectionLength = 5
                        for iterations in range(0,sectionLength):
                            puzzle.append(textFactory(textFactoryMode,blacklist))
                            blacklist.append(puzzle[-1])
                        puzzle.append(')')
                    case _:
                        #abc no brackets
                        matchNumRand = randint(0,100) #watch out
                        if matchNumRand in range(0,39):
                            sectionLength = 1
                        elif matchNumRand in range(40,74):
                            sectionLength = 2
                        elif matchNumRand in range(75,89):
                            sectionLength = 3
                        else:
                            sectionLength = 4
                        for iterations in range(0,sectionLength):
                            puzzle.append(textFactory(textFactoryMode,blacklist))
                            blacklist.append(puzzle[-1])

        

        totalLength += sectionLength
    return {'puzzle':puzzle, 'sectionLength':totalLength, 'totalLength':totalLength} #to maintain compatiablilty

def textFactory(mode,blacklist):
    ignition = True
    finalSolution = ''
    while (finalSolution in blacklist) or ignition:
        ignition = False
        match mode:
            case 1: # a-z
                textPos = randint(0,25)
                finalSolution = str(textTuple[textPos])
            case 2: # A-Z
                textPos = randint(0,25)
                finalSolution = str(textTuple[textPos].upper())
            case 3: # 0-9
                textPos = randint(0,9)
                finalSolution = str(numberTuple[textPos])
            case 4: # symbols
                textPos = randint(0,9)
                finalSolution = str(symbolTuple[textPos])
            case 5: # \s
                textPos = 0
                finalSolution = ' ' # NO BLACKLIST ON MODE 5
    return finalSolution

def listJoinery(rawList):
    joinedString = ''
    for element in rawList:
        joinedString = joinedString+str(element)
    return joinedString

def gameSession(numRepeats,numSections,maxAnsLen,maxTime):
    score = 0
    sessionCharsUsed = 0
    timeAnchorSession = time()
    for iteration in range(0,numRepeats):
        # creating puzzle...
        timeAnchorLocal = time()
        print('puzzle no.'+str(iteration+1))
        theExpression = regexSectionConstructor(numSections)
        theExpression['puzzle'] = listJoinery(theExpression['puzzle'])
        match maxAnsLen[0]:
            case 0:
                theExpression['sectionLength'] = int(theExpression['sectionLength']*3.5)-3
            case 1:
                theExpression['sectionLength'] = int(theExpression['sectionLength']*1.5)-1
            case 2:
                theExpression['sectionLength'] = int(theExpression['sectionLength']*1.2)+1
            case 3:
                theExpression['sectionLength'] += 1
        match maxTime[0]:
            case 0:
                timeGiven = 60+5*numSections #60s for each puzzle +5s for each section length
            case 1:
                timeGiven = 30+3*numSections #30s for each puzzle +3s for each section length
            case 2:
                timeGiven = 15+numSections #15s for each puzzle +1s for each section length
            case 3:
                timeGiven = 5+numSections #5s for each puzzle +1s for each section length
        print('In',timeGiven,'seconds,')
        print('Solve: /'+theExpression['puzzle']+'/ in',theExpression['sectionLength'],'charcters')
        answer = input('/i Your Answer >>>:' )
        
        # validating answer...
        score += 1
        sessionCharsUsed += len(answer)
        if re.match(theExpression['puzzle'],answer) != None:
            print('Match! Your answer satisfies the regex.')
        else:
            print('Your answer does not satisfy the regex.')
            print('a point has been deducted.')
            score -= 1
        if (len(answer) > theExpression['sectionLength']) and maxAnsLen[1]:
            print('Your answer was too long at',len(answer),'characters long.')
            print('It should be',theExpression['sectionLength'],'characters long.')
            print('a point has been deducted.')
            score -= 1
        if ((time()-timeAnchorLocal) > timeGiven) and maxTime[1]:
            print('You took too long to answer.')
            print('a point has been deducted.')
            score -= 1
        else:
            print(int(time()-timeAnchorLocal))
    # puzzle done
    sessionTime = time()-timeAnchorSession
    print(int(sessionTime))
    print("This session's final score:",str(score)+'/'+str(numRepeats))
    return {'score':score,'time':sessionTime,'chars':sessionCharsUsed}


# numrepeats, numsections, (maxanslen, demerit), (maxtime, demerit)
gameSession(1,5,(2,True),(3,True))