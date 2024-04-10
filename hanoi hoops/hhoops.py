import pygame
pygame.init()
from random import randint as rnd

displaySize = (700,500) 
displaySurface = pygame.display.set_mode(displaySize)
displayColour = (35,35,30) #gray

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
        pygame.draw.circle(displaySurface,self.colourSelection.red,(self.x,self.y),10,2)
    
    def showOriginOverrideAll(self): #super scuffed. DONT USE IF YOU CAN
        run = True
        while run:
            pygame.draw.circle(displaySurface,self.colourSelection.red,(self.x,self.y),3,2)
            if (input('continue?') or True):
                run = False

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
        pygame.draw.rect(displaySurface,self.colourSelection.blue,(self.rx,self.ry,self.rlength,self.rheight))
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
        self.r1length = r1length
        self.r1height = r1height
        self.r1x = x-(r1length/2)
        self.r1y = y
        self.r2length = r2length
        self.r2height = r2height
        self.r2x = x-(r2length/2)
        self.r2y = y-r2height
    def showMe(self):
        pygame.draw.rect(displaySurface,self.colourSelection.blue,(self.r1x,self.r1y,self.r1length,self.r1height))
        pygame.draw.rect(displaySurface,self.colourSelection.green,(self.r2x,self.r2y,self.r2length,self.r2height))
    def showOrigin(self):
        return super().showOrigin()
    def showOriginOverrideAll(self):
        return super().showOriginOverrideAll()



poland = poleConstructor()
poland.initMe(200,200,100,20,20,100)
poland.showMe()
poland.showOrigin()

globalRun = True
num = 1
while globalRun:
    num += 1

    pygame.display.update()
    if num == 5000:
        globalRun = False
