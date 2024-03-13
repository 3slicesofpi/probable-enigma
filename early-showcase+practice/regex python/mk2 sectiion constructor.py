from random import randint as rnd
import re
def d2():
    num = rnd(1,2)
    if num == 1:
        return False
    else: return True

def bd2(TrueChance):
    num = rnd(0,100)
    if num <= TrueChance:
        return True
    else: return False
    

textTuple = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numberTuple = ('0','1','2','3','4','5','6','7','8','9')
symbolTuple = ('!','#','%',':',';','<','>','=','_','~') 
def textFactory(mode,blacklist):
    ignition = True
    finalSolution = ''
    while (finalSolution in blacklist) or ignition:
        ignition = False
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
    return finalSolution

def listJoinery(rawList):
    joinedString = ''
    for element in rawList:
        joinedString = joinedString+str(element)
    return joinedString

def integratedFactoryAndValidator():
    textFactoryMode = rnd(1,2)
    localValidation = 0
    while localValidation == 0:
        try:
            negatoryFlag = ''
            if rnd(1,2) == 1:
                negatoryFlag = '^'
            char2 = rnd(1,25)
            char1 = rnd(0,char2-1)
            if rnd(1,2) == 1:
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

def regexSectionConstructor(numofSections): #mk. II
    sectionTypeChance = (0,25,35,45,55,85,101)
    sectionTypeChance[-1] = 101 # just to make sure
    theEx = []
    totalLength = 0
    for sectionnum in range(1,numofSections+1):
        sectionLength = 0
        sectionTypeRand = rnd(0,100)
        if sectionTypeRand in range(sectionTypeChance[0],sectionTypeChance[1]-1): # {abc]
            theEx.append('[')
            sectionLength += 1
            blacklist = []
            if d2():
                negatoryFlag = True
            else:
                negatoryFlag = False
            if textFactoryMode in range(0,34):
                textFactoryMode = 1 #a
                if bd2(60) and negatoryFlag:
                    theEx.append('A-Z0-9') # TODO update to include symbols
            elif textFactoryMode in range(35,54):
                textFactoryMode = 2 #A
                if bd2(60) and negatoryFlag:
                    theEx.append('a-z0-9')
            elif textFactoryMode in range(55,84):
                textFactoryMode = 3 #1
                if bd2(60) and negatoryFlag:
                    theEx.append('A-z')
            else:
                if rnd(1,5)<=2:
                    textFactoryMode = 4 #%
                    if d2() and negatoryFlag:
                        theEx.append('A-z0-9') #remain as is
                else:
                    textFactoryMode = 5 #/s

            # there is a better way involving maths
            for char in range(1,rnd(1,4)+1):
                theEx.append(textFactory(textFactoryMode,blacklist))
                blacklist.append(theEx[-1])
            theEx.append(']')
        elif sectionTypeRand in range(sectionTypeChance[1],sectionTypeChance[2]-1): #[a-c]
            # blacklist = []
            sectionLength += 1
            negatoryFlag = d2()
            match rnd(1,5):
                case 1:
                    if d2():
                        theEx.append('[')
                        if negatoryFlag:
                            theEx.append('^')
                        theEx.append('a-')
                        theEx.append(textFactory(1,('a','z')))
                    else:
                        theEx.append('[')
                        if negatoryFlag:
                            theEx.append('^')
                        theEx.append('A-')
                        theEx.append(textFactory(2,('A','Z','a','z')))
                    theEx.append(']')
                case 2:
                    if d2():
                        theEx.append('[')
                        if negatoryFlag:
                            theEx.append('^')
                        theEx.append(textFactory(1,('z','a')))
                        theEx.append('-z]')
                    else:
                        theEx.append('[')
                        if negatoryFlag:
                            theEx.append('^')
                        theEx.append(textFactory(2,('Z','A','z','a')))
                        theEx.append('-Z]')
                case _:
                    theEx.append(integratedFactoryAndValidator())
        elif sectionTypeRand in range(sectionTypeChance[2],sectionTypeChance[3]-1): #[A-c]
            # blacklist = []
            sectionLength += 1
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
        elif sectionTypeRand in range(sectionTypeChance[3],sectionTypeChance[4]-1): #.
            # if a better way is found, use it from #[abc]
            for char in range(1,rnd(1,3)+1):
                sectionLength += 1
                theEx.append('.')
        elif sectionTypeRand in range(sectionTypeChance[4],sectionTypeChance[5]-1): #abc
            if d2():
                # random jumble of everything
                for char in range(1,rnd(1,3)+1):
                    sectionLength += 1
                    theEx.append(textFactory(rnd(1,5),()))
            else:
                # do as normal
                textFactoryMode = rnd(0,100)
                if textFactoryMode in range(0,34):
                    textFactoryMode = 1 #a
                elif textFactoryMode in range(35,54):
                    textFactoryMode = 2 #A
                elif textFactoryMode in range(55,84):
                    textFactoryMode = 3 #1
                else:
                    textFactoryMode = 4 #/s
                if d2():
                    #(abc)
                    theEx.append('(')
                    if d2():
                        theEx.append('^')
                    matchNumRand = rnd(0,100) #watch out
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
                        theEx.append(textFactory(textFactoryMode,blacklist))
                        blacklist.append(theEx[-1])
                    theEx.append(')')

                    #abc no brackets
                    matchNumRand = theEx(0,100) #watch out
                    if matchNumRand in range(0,39):
                        sectionLength = 1
                    elif matchNumRand in range(40,74):
                        sectionLength = 2
                    elif matchNumRand in range(75,89):
                        sectionLength = 3
                    else:
                        sectionLength = 4
                    for iterations in range(0,sectionLength):
                        theEx.append(textFactory(textFactoryMode,blacklist))
                        blacklist.append(theEx[-1])    

        elif sectionTypeRand in range(sectionTypeChance[5],sectionTypeChance[6]-1): #(abc)
            pass

    totalLength += sectionLength
    return {'puzzle':theEx, 'sectionLength':totalLength, 'totalLength':totalLength} #to maintain compatiablilty
