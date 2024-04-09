import pygame
pygame.init()
from random import randint as rnd

displaySize = (700,500) 
displaySurface = pygame.display.set_mode(displaySize)

class colours(): # with a u
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    black = (0, 0, 0) 
    red = (255, 0, 0)
    gray = (35,35,30)
    custom = {}
    def customColour(self,name,nums):
        try:
            int(nums[0]) == 0
            int(nums[1]) == 0
            int(nums[2]) == 0
        except:
            print('a tuple with 3 integers is needed.')
        self.custom[name] = nums
    def getColour(self,name):
        match name:
            case 'yellow':
                self.yellow = (239, 192, 80)
                return (239, 192, 80)
            case 'beige':
                self.beige = (223, 207, 190)
                return (223, 207, 190)
            case 'orange':
                self.orange = (225, 93, 68)
                return (225, 93, 68)
            case 'purple':
                self.purple = (91, 94, 166)
                return (91, 94, 166)
            case 'pink':
                self.pink = (247, 202, 201)
                return (247, 202, 201)
            case 'forest': 
                self.forest = (2, 50, 32)
                return (2, 50, 32)
            case 'sky': # light blue
                self.sky = (146, 168, 209)
                return (146, 168, 209)
            case 'marsala': # red
                self.marsala = (149, 82, 81)
                return (149, 82, 81)
            case 'burgundy': # red
                self.burgundy = (128, 0, 32)
                return (128, 0, 32)
            case 'orchid': # pink
                self.orchid = (181, 101, 167)
                return (181, 101, 167)
            case 'turqoise': # light blue
                self.turqoise = (68, 184, 172)
                return (68, 184, 172)
            case 'lime': # green
                self.lime = (136, 176, 75)
                return (136, 176, 75)
class spriteConstructor():
    colour = colours().gray
    display = displaySurface
    x = 0
    y = 0

class rectConstructor(spriteConstructor):
    width = 10
    height = 10

class poleConstructor(spriteConstructor):
    Awidth = 100
    Aheight = 10
    Ax = 100
    Ay = 100
    Awidth = 100
    Aheight = 10
    Bwidth = 20
    Bheight = 100
    Bx = Ax+(Awidth-Bwidth)/2
    By = Ay-Awidth
    height = 0
    anchorPos = []

    def updatePos(self):
        # update my position. VERY IMPORTANT
        self.Ax = self.x-(self.Awidth/2)
        self.Bx = self.x-(self.Bwidth/2)
        self.Ay = self.y
        self.By = self.y-self.Bheight
        self.Bheight = (32+15*self.height)
        anchorPos = []
        for iter in range(self.height):
            self.anchorPos.append([self.x,self.y-self.Aheight-iter*15])
            # pygame.draw.rect(self.display,self.colour,(self.x,self.y-self.Aheight-iter*15,10,10))

    def modifyHeight(self,height):
        self.height = height
        self.updatePos()




pygame.display.set_caption('hanoiHoops.py')
displaySurface.fill(colours().gray)


running = True
pole1 = poleConstructor()
(pole1.x,pole1.y) = ((displaySize[0])/4,displaySize[1]/1.7)
pole1.colour = colours().red
pole1.modifyHeight(1)
pole2 = poleConstructor()
(pole2.x,pole2.y) = ((displaySize[0])/2,displaySize[1]/1.7)
pole2.colour = colours().blue
pole2.modifyHeight(2)
pole3 = poleConstructor()
(pole3.x,pole3.y) = ((displaySize[0])*3/4,displaySize[1]/1.7)
pole3.colour = colours().green
pole3.modifyHeight(3)

rect1 = rectConstructor()
(rect1.x,rect1.y) = pole3.anchorPos[0]
rect1.colour = colours().gray
rect2 = rectConstructor()
print(pole1.anchorPos)
(rect2.x,rect2.y) = pole1.anchorPos[2]
rect2.colour = colours().gray

displayUpdate = True
while running:
    if displayUpdate:
        # draw poles
        for iter in (pole1,pole2,pole3):
            
            pygame.draw.rect(iter.display,iter.colour,(iter.Ax, iter.Ay, iter.Awidth, iter.Aheight))
            pygame.draw.rect(iter.display,iter.colour,(iter.Bx, iter.By, iter.Bwidth, iter.Bheight))

            iter.updatePos()

        # draw rects
        for iter in (rect1,rect2):

            pygame.draw.rect(iter.display,iter.colour,(iter.x,iter.y,iter.width,iter.height))
        pygame.display.update()
        displayUpdate = False
    else:
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_0]:
        displaySurface.fill(colours().gray)
        displayUpdate = True
    if keys[pygame.K_1]:
        for iter in (pole1,pole2,pole3):
            iter.colour = colours().white
        displayUpdate = True
    if keys[pygame.K_2]:
        for iter in (pole1,pole2,pole3):
            iter.colour = colours().blue
        displayUpdate = True
    if keys[pygame.K_3]:
        rect1.colour = (rnd(0,254),rnd(0,254),rnd(0,254))
        displayUpdate = True
    if keys[pygame.K_4]:
        rect2.colour = (rnd(0,254),rnd(0,254),rnd(0,254))
        displayUpdate = True
    
    