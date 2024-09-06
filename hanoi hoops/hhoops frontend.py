import pygame as pg
import time
import cmd  # used for overrides and manual data get

pg.init()

canvasSize = (900, 700)
canvasName = "hhoops 0.2.0 Development"
# CREATING CANVAS
canvas = pg.display.set_mode(canvasSize)
updateSurfaces = True

class Cursor:
    def __init__(self, x=0.0, y=0.0, width=100.0, height=100.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pointingat = 0
        self.contentat = None

    def getpoints(self):
        return (self.x + self.width / 2, self.y), (self.x, self.y + self.height), (self.x - self.width / 2, self.y)

    def moveHere(self, newPos):
        self.x = newPos[0]
        if newPos[1]:
            self.y = newPos[1]
        redrawSurfaces()

    def movePole(self, poleAddress):
        self.moveHere((poleINFO[poleAddress].x + poleINFO[poleAddress].baseRect.width/2, 0))
        self.contentat = poleINFO[poleAddress]
        self.pointingat = poleAddress
        print(poleAddress)


class HoopInstance(pg.Rect):
    def __init__(self, *args):
        super().__init__(*args)
        self.unitsize = 256
        self.poleAddress = 0  # from left to right
        self.polePointer = None
        self.positAddress = 0  # posit on pole, iter from bottom

    def moveHere(self, newPos):
        self.x = newPos[0]
        self.y = newPos[1]
        redrawSurfaces()


class PoleInstance:
    def __init__(self, xpos, ypos, width, height):
        self.x = xpos
        self.y = ypos
        self.headRect = pg.Rect(xpos-width/2, ypos, 20, height)
        self.baseRect = pg.Rect(xpos, ypos, width, 20)
        self.poleAddress = 0  # from left to right
        self.content = []  # end of list (for some reason)
        self.topsize = 256  # if we make this zero stuff breaks
        self.calibratepos()

    def calibratepos(self):
        self.headRect.x = self.x+(self.baseRect.width-self.headRect.width)/2
        self.headRect.y = self.y
        self.baseRect.x = self.x
        self.baseRect.y = self.y+self.headRect.height

    def moveHere(self, newPos):
        self.x, self.y = newPos
        self.calibratepos()
        redrawSurfaces()

def startgame(hoopcount=4, polecount=3):  # incl. globals
    """This is very slow"""
    if (hoopcount < 2) or (polecount < 3):
        return
    global hoopCount
    hoopCount = hoopcount
    global poleCount
    poleCount = polecount
    global poleINFO
    poleINFO = []
    global hoopINFO
    hoopINFO = []
    global cursor
    polewidth = (hoopcount+0.45)*25
    # Creating the PoleInstance
    # the first one will be very important... save it for later!
    for i in reversed(range(polecount)):
        newInstance = PoleInstance((i+1)*canvasSize[0]/hoopcount-polewidth/2, canvasSize[1]/3, polewidth, (hoopcount+1.75)*25)
        newInstance.poleAddress = i
        poleINFO.append(newInstance)
    try:
        newInstance = newInstance
    except:
        return

    # Creating the HoopInstance...
    for i in reversed(range(hoopcount)):
        hInstance = HoopInstance(0, newInstance.baseRect.y-25-i*25, (hoopcount - i) * 25, 25)
        hInstance.unitsize = hoopcount - i
        hInstance.x = newInstance.x+newInstance.baseRect.width/2-(hoopcount - i) * 12.5 + 1
        hInstance.poleAddress = 0
        hInstance.polePointer = newInstance
        hoopINFO.append(hInstance)

    # creating the CursorInstance...
    cursor = Cursor(newInstance.x + newInstance.baseRect.width/2, canvasSize[1]/5, canvasSize[0]/24, canvasSize[0]/40)
    cursor.contentat = newInstance


cursor = Cursor(0, 0, 0, 0)
hoopINFO = [HoopInstance(100, 10, 100, 10)]
hoopCount = 1  # length of hoopInfo
poleINFO = [PoleInstance(200, 200, 100, 100)]
poleCount = 1  # length of poleInfo

startgame()
for i in poleINFO:
    print(i.poleAddress)

def redrawSurfaces():
    global updateSurfaces
    if not updateSurfaces:
        print('Redrawing Surface Canvas...')
        updateSurfaces = True


# TITLE OF CANVAS
pg.display.set_caption(canvasName)
exitFLAG = False

# STARTING LOOP
redrawSurfaces()
kpressedFLAG = 0
while not exitFLAG:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exitFLAG = True

    keys = pg.key.get_pressed()
    if keys[pg.K_DOWN]:
        redrawSurfaces()
    if keys[pg.K_UP]:
        hoopINFO[0].moveHere((200, 200))
    if keys[pg.K_RIGHT]:
        if not kpressedFLAG:
            cursor.pointingat -= 1
            if cursor.pointingat < 0:
                cursor.pointingat = poleCount-1
            cursor.movePole(cursor.pointingat)
        kpressedFLAG += 1
    elif keys[pg.K_LEFT]:
        if not kpressedFLAG:
            cursor.pointingat += 1
            if cursor.pointingat > poleCount-1:
                cursor.pointingat = 0
            cursor.movePole(cursor.pointingat)
        kpressedFLAG += 1
    else:
        kpressedFLAG = 0

    if updateSurfaces:
        pg.display.update()
        canvas.fill((10, 10, 10))
        print(cursor.pointingat)
        for i in poleINFO:
            pg.draw.rect(canvas, (0, 0, 255), i.headRect)
            pg.draw.rect(canvas,(0, 0, 255), i.baseRect)
        for i in hoopINFO:
            pg.draw.rect(canvas, (255, 0, 0), i)
        pg.draw.polygon(canvas, (0, 255, 0), cursor.getpoints())
        updateSurfaces = False

