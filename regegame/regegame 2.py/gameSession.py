

def regexSectionConstructor(numofSections):
    return {'puzzle':'[a-z]','totalSections':1}

argDict = { 
    'penCorrect':True,'givenScore':0,
    'givenTime':0,'randTime':0,'penTime':True,'randModeTime':0,
    'givenChars':1,'randChars':0,'penChars':True,'randModeChars':1,
    'numSections':3,'randSections':0,'randModeSections':2,
    'numPuzzles':5,'sectionTime':2
    }
modeDict = {'gamemode':'classic','deathmode':'scoredown'}

from time import time
from random import randint as rnd
import re



def gameSession():
    timeAnchorSession = time()
    stats = []
    #time, chars, sections
    randNamesFloor = [0,0,0]
    randNamesCeil = [0,0,0]
    randNamesMode = (argDict['randModeTime'],argDict['randModeChars'],argDict['randModeSections'])
    randNamesQuantity = (argDict['randTime'],argDict['randChars'],argDict['randSections'])
    for randSelected in range(3):
        if randNamesQuantity[randSelected]>0:
            match randNamesMode[randSelected]:
                case 0: # default
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]
                case 1: # addonly
                    # randNamesFloor[randSelected] = 0
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]
                case 2: # minusonly
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    # randNamesFloor[randSelected] = 0
                case 3: # reduced minus
                    randNamesFloor[randSelected] = 1-randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]
                case 4: # additional add
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = 1+randNamesQuantity[randSelected]
                case 5: # reduced add
                    randNamesFloor[randSelected] = -randNamesQuantity[randSelected]
                    randNamesCeil[randSelected] = randNamesQuantity[randSelected]-1
    puzzleNum = 0
    if modeDict['gamemode'] == 'endless':
        totalScore = 10
        argDict['numPuzzles'] = 18446744073709551615
    else:
        totalScore = 0
    killswitch = False
    while (puzzleNum < argDict['numPuzzles']):  #or killswitch):
        if killswitch: # i guess python hates non-pythonic code?
            # use this to ensure killswitch kills gameSession
            return stats
        puzzleNum += 1
        print('puzzle no.:',puzzleNum)
        # compute totals
        totalSections = argDict['numSections']+rnd(randNamesFloor[2],randNamesCeil[2])
        totalTime = argDict['givenTime']+rnd(randNamesFloor[0],randNamesCeil[0])+totalSections*argDict['sectionTime']
        match modeDict['gamemode']:
            case _:
                theEx = regexSectionConstructor(totalSections)
        totalChars = argDict['givenChars']+rnd(randNamesFloor[1],randNamesCeil[1])+theEx['totalSections']
        if argDict['penTime']:
            print('In',totalTime,'seconds,')
        print('Solve /'+theEx['puzzle']+'/')
        if argDict['penChars']:
            print('using',totalChars,'characters')
        timeAnchorLocal = time()
        theAns = input('>>>:')

        # count penalties and tally stats
        localStats = {'score':argDict['givenScore']+1,'ansCorrect': True,'theAns':theAns,'theEx':theEx['puzzle'],'ansTime':time()-timeAnchorLocal,'totalTime':totalTime,'totalChars':totalChars}
        if re.match(theEx['puzzle'],theAns) == None: #wrong
            print('Incorrect Answer.')
            localStats['ansCorrect'] = False
            if argDict['penCorrect']:
                localStats['score']-=2
        if argDict['penTime']:
            if localStats['ansTime']>=totalTime:
                localStats['score']-=1
                print('Exceeded Time Limit of',totalTime,'; You took',localStats['ansTime'],'seconds')
        if argDict['penChars']:
            if len(theAns)>totalChars:
                localStats['score']-=1
                print('Exceeded character Limit of',totalChars,'; Your answer was',len(theAns),'long.')
        totalScore += localStats['score']
        stats.append(localStats)

        # check whether to end the game
        match modeDict['deathmode']:
            case 'none':
                pass
            case 'scoredown':
                if totalScore <=0:
                    print('Out of Score!')
                    killswitch = True
                elif totalScore <=3:
                    print('You only have',totalScore,'score left.')
            case 'timedown':
                timeAnchorSession += totalTime
                if time()>timeAnchorSession:
                    print('Out of time!')
                    killswitch = True
                else:
                    print('Total time Left (Estimated):'-int(time()-timeAnchorSession)+argDict['givenTime']+(argDict['numSections']*argDict['sectionTime']))
        
    return stats
        

print(gameSession())