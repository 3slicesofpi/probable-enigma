from random import randint as rnd
from random import getrandbits
import re
def d2(): #fastest fingers in the west
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

def regexRndChooser(numofSections):
    sectionTypeChance = (0,25,35,45,55,65,75,95,101) # plh
    textFactoryChance = (0,35,55,80,90,101)
    sectionLengthChance = (0,30,55,80,95,101)
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
    #     capGrpPosStart = 3 # rnd(0,len(quota)-1)
    #     quota.insert(capGrpPosStart,'(')
    #     capGrpPosEnd = 6 # rnd(capGrpPosStart+1,len(quota))
    #     quota.insert(capGrpPosEnd,')')
    #     for numQuota in quota[capGrpPosStart:capGrpPosEnd]:
    #         print(numQuota)
    return quota


def regexSectionConstructor(numofSections): #mk. IIA
    theEx = []
    totalLength = 0
    theQuota = regexRndChooser(numofSections)
    for numQuota in theQuota:
        sectionLength = 0
        match numQuota['type']:  
            case 1: # [abc]
                theEx.append('[')
                sectionLength += 1
                blacklist = []

                if d2():
                    negatoryFlag = True
                    theEx.append('^')
                else:
                    negatoryFlag = False
                match numQuota['textFactoryMode']:
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
                for char in range(1,rnd(1,4)+1):
                    theEx.append(textFactory(numQuota['textFactoryMode'],blacklist))
                    blacklist.append(theEx[-1])
                theEx.append(']')
            case 2: # [A-Z]/[a-z]

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
            case 3: # [A-z]
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
            case 4: # .
                for char in range(0,numQuota['sectionLength']):
                    sectionLength += 1
                    theEx.append('.')
            case 5: # .\.\*\s
                for char in range(0,numQuota['sectionLength']):
                    sectionLength += 1
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
                for char in range(0,numQuota['sectionLength']):
                    sectionLength += 1
                    theEx.append(textFactory(rnd(1,5),()))
            case 7: # (abc)                
                blacklist = []
                if numQuota['textFactoryMode'] == 4:
                    numQuota['textFactoryMode'] = rnd(1,3) # !!!!!!!!!!!! quotalist - NOT UPDATED ---- FIX!!!!!!!!!!

                if d2():
                    #(abc)
                    theEx.append('(')
                    # if d2(): # this breaks the game i dont know why
                    #     theEx.append('^')
                    for iterations in range(0,numQuota['sectionLength']):
                        theEx.append(textFactory(numQuota['textFactoryMode'],blacklist))
                        blacklist.append(theEx[-1])
                    theEx.append(')')

                    #abc no brackets
                    for iterations in range(0,numQuota['sectionLength']):
                        theEx.append(textFactory(numQuota['textFactoryMode'],blacklist))
                        blacklist.append(theEx[-1])    
            case 8:
                print('eh') # plh

    totalLength += sectionLength
    return {'puzzle':theEx, 'sectionLength':totalLength, 'totalLength':totalLength} #to maintain compatiablilty

print(listJoinery(regexSectionConstructor(3)['puzzle']))