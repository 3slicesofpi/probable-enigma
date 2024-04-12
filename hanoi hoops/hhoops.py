import pygame
pygame.init()
from random import randint as rnd

displaySize = (700,500) 
displaySurface = pygame.display.set_mode(displaySize)
displayColour = (35,35,30) #gray
numofHoops = 3 #temp
hoopHeight = 16
hoopLength = 80
class colours(): # shortened
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    black = (0, 0, 0) 
    red = (255, 0, 0)
    gray = (35,35,30)

class spriteConstructor():
    colourSelection = colours()
    colour = colourSelection.gray
    display = displaySurface
    x = 0
    y = 0

    def showOrigin(self):
        pygame.draw.circle(displaySurface,self.colourSelection.red,(self.x,self.y),2,2)
    
    def showOriginOverrideAll(self): #super scuffed. DONT USE IF YOU CAN
        run = True
        while run:
            pygame.draw.circle(displaySurface,self.colourSelection.red,(self.x,self.y),3,2)
            if (input('continue?') or True):
                run = False

class handConstructor(spriteConstructor):
    holding = None
    def showOrigin(self):
        return super().showOrigin()
    def showOriginOverrideAll(self):
        return super().showOriginOverrideAll()

class rectConstructor(spriteConstructor):
    rlength = 0
    rheight = 0
    def initMe(self,x,y,rlength,rheight):
        self.x = x
        self.y = y
        self.rlength = rlength
        self.rheight = rheight
        self.rx = x-(rlength/2)
        self.ry = y-(rheight/2)
    def showMe(self):
        pygame.draw.rect(displaySurface,self.colour,(self.rx,self.ry,self.rlength,self.rheight))
    def moveMe(self,newx,newy):
        self.x = newx
        self.y = newy
        self.rx = newx-(self.rlength/2)
        self.ry = newy-(self.rheight/2)
    def showOrigin(self):
        return super().showOrigin()
    def showOriginOverrideAll(self):
        return super().showOriginOverrideAll()

class poleConstructor(spriteConstructor):
    r1length = 0
    r1height = 0
    r2length = 0
    r2height = 0
    def initMe(self,x,y,r1length,r1height,r2length,r2height):
        self.x = x 
        self.y = y
        self.r1length = r1length # base
        self.r1height = r1height
        self.r1x = x-(r1length/2)
        self.r1y = y
        self.r2length = r2length # pole
        self.r2height = r2height
        self.r2x = x-(r2length/2)
        self.r2y = y-r2height
    def showMe(self):
        pygame.draw.rect(displaySurface,self.colourSelection.white,(self.r1x,self.r1y,self.r1length,self.r1height))
        pygame.draw.rect(displaySurface,self.colourSelection.white,(self.r2x,self.r2y,self.r2length,self.r2height))
    def createAnchors(self,numofAnchors):
        self.anchorPos = []
        for iterations in range(numofAnchors):
            self.anchorPos.append([self.x,self.y-(0.5+iterations)*(hoopHeight),None])
        
    def showOrigin(self):
        return super().showOrigin()
    def showOriginOverrideAll(self):
        return super().showOriginOverrideAll()


def initPoles(poleName,numofAnchors,posx,posy):
    poleName = poleConstructor()
    poleName.initMe(posx,posy,100,20,20,((hoopHeight)*(numofAnchors+1.2)))
    poleName.createAnchors(numofAnchors)
    return poleName

poleLeft = None
poleLeft = initPoles(poleLeft,numofHoops,displaySize[0]/4,(displaySize[1]/2)+(numofHoops*hoopHeight*2/3))
poleLeft.showMe()
poleCenter = None
poleCenter = initPoles(poleCenter,numofHoops,displaySize[0]/2,(displaySize[1]/2)+(numofHoops*hoopHeight*2/3))
poleCenter.showMe()
poleRight = None
poleRight = initPoles(poleRight,numofHoops,displaySize[0]*3/4,(displaySize[1]/2)+(numofHoops*hoopHeight*2/3))
poleRight.showMe()
poleContainer = [poleLeft,poleCenter,poleRight]


hoop1 = rectConstructor()
hoop1.initMe(poleLeft.anchorPos[0][0],poleLeft.anchorPos[0][1],hoopLength,hoopHeight)
hoop1.colour = hoop1.colourSelection.red
poleLeft.anchorPos[0][2] = 0 # i do not like this, temp solution only
hoop1.showMe()
hoop2 = rectConstructor()
hoop2.initMe(poleLeft.anchorPos[1][0],poleLeft.anchorPos[1][1],hoopLength-15,hoopHeight)
hoop2.colour = hoop2.colourSelection.green
poleLeft.anchorPos[1][2] = 1
hoop2.showMe()
hoop3 = rectConstructor()
hoop3.initMe(poleLeft.anchorPos[2][0],poleLeft.anchorPos[2][1],hoopLength-30,hoopHeight)
hoop3.colour = hoop3.colourSelection.blue
poleLeft.anchorPos[2][2] = 2
hoop3.showMe()
hoopContainer = [hoop1,hoop2,hoop3] # id of hoop1 = 0

hand = handConstructor()
hand.x = poleContainer[0].x
hand.y = poleContainer[1].r2y-hoopHeight
hand.holding = None


globalRun = True
displayUpdate = True 
while globalRun:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                globalRun = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1:
                        # poleLeft
                        if hand.holding == None: #TAKE
                            print('take')
                            foundit = False
                            for iteration in list(reversed(range(numofHoops))):
                                hand.holding = poleLeft.anchorPos[iteration][2]
                                if hand.holding != None and not foundit:
                                    foundit = True
                                    hoopContainer[hand.holding].moveMe(hand.x,hand.y)
                                    poleLeft.anchorPos[iteration][2] = None
                                    displayUpdate = True
                                    fORCE_ID_ON_HAND = hand.holding
                                    

                        else: # INSERT
                            print('insert')
                            foundit = False
                            for iteration in list(reversed(range(numofHoops))):
                                if poleLeft.anchorPos[iteration][2] == None:
                                    foundit = True
                                    print(hand.holding)
                                    print(poleLeft.anchorPos[iteration][2])
                                    poleLeft.anchorPos[iteration][2] = hand.holding
                                    hoopContainer[hand.holding].moveMe(poleLeft.anchorPos[iteration][0],poleLeft.anchorPos[iteration][1])
                                    hand.holding = None
                                    fORCE_ID_ON_HAND = None
                                    displayUpdate = True

                        # the number disappears somehow???? why are my 2 becoming 0   
                        hand.holding = fORCE_ID_ON_HAND

                    case pygame.K_2:
                        # poleCenter
                        if hand.holding == None: #TAKE
                            print('take')
                            foundit = False
                            for iteration in list(reversed(range(numofHoops))):
                                hand.holding = poleCenter.anchorPos[iteration][2]
                                if hand.holding != None and not foundit:
                                    foundit = True
                                    hoopContainer[hand.holding].moveMe(hand.x,hand.y)
                                    poleCenter.anchorPos[iteration][2] = None
                                    displayUpdate = True
                                    fORCE_ID_ON_HAND = hand.holding
                                    

                        else: # INSERT
                            print('insert')
                            foundit = False
                            for iteration in list(reversed(range(numofHoops))):
                                if poleCenter.anchorPos[iteration][2] == None:
                                    foundit = True
                                    print(hand.holding)
                                    print(poleCenter.anchorPos[iteration][2])
                                    poleCenter.anchorPos[iteration][2] = hand.holding
                                    hoopContainer[hand.holding].moveMe(poleCenter.anchorPos[iteration][0],poleCenter.anchorPos[iteration][1])
                                    hand.holding = None
                                    fORCE_ID_ON_HAND = None
                                    displayUpdate = True

                        hand.holding = fORCE_ID_ON_HAND
                    case pygame.K_3:
                        # poleRight
                        if hand.holding == None:
                            print('ok')
                        
    if displayUpdate:
        displaySurface.fill(displayColour)
        for here in range(len(poleContainer)):
            poleContainer[here].showMe()
        for here in range(len(hoopContainer)):
            hoopContainer[here].showMe()

        pygame.display.update()
