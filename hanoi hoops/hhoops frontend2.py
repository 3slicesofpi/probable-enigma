import pygame as pg

class HoopInstance:
    def __init__(self, x_left, y_top, width, height):
        self.thickness = height
        self.width = width
        self.poleAddress = 0  # from left to right
        self.polePointer = None
        self.positAddress = 0  # start from bottom, count from 0
        self.hoopRect = pg.Rect(x_left, y_top, width, height)

    def move(self, pos: [float, float]):
        self.hoopRect.x, self.hoopRect.y = pos

    def size(self) -> int:
        return self.width//self.thickness


class CursorInstance:
    def __init__(self, x_left, y_top, width=50, height=20):
        self.x = x_left
        self.y = y_top
        self.width = width
        self.height = height
        self.pointingat = 0
        self.content = None
        self.topsize = 256

    def getpoints(self) -> [[float, float], [float, float], [float, float]]:
        return (self.x, self.y), (self.x + self.width / 2, self.y + self.height), (self.x + self.width, self.y)

    def addhoop(self, hInstance: HoopInstance):
        self.content = hInstance
        self.topsize = hInstance.size()
        hInstance.poleAddress = -1
        hInstance.positAddress = 0
        hInstance.move([sum(lis) for lis in zip((self.x, self.y), (self.width/2, self.height*2))])

    def removehoop(self) -> HoopInstance:
        hInstance = self.content
        self.content = None
        self.topsize = 256
        return hInstance


class PoleInstance:
    def __init__(self, x_left, y_top, width, height, thickness=24, position=0):
        self.x = x_left  # origin pos
        self.y = y_top
        self.width = width
        self.height = height
        self.thickness = 24
        self.position = position  # start from left
        self.content = []  # end of list (for some reason)
        self.topsize = 256  # if we make it zero stuff breaks

        self.baseRectoffset = 0, +height
        self.poleRectoffset = (width-thickness+3)/2, 0
        self.poleRect = pg.Rect(x_left+width/2-thickness/2+1.5, y_top, thickness, height)
        self.baseRect = pg.Rect(x_left, y_top+height, width, thickness)

    def move(self, pos: [float, float]):
        self.x = pos[0]
        self.y = pos[1]
        self.poleRect.x, self.poleRect.y = [sum(lis) for lis in zip(pos, self.poleRectoffset)]
        self.baseRect.x, self.baseRect.y = [sum(lis) for lis in zip(pos, self.baseRectoffset)]
        self.cursorhere(cursor)
        for i in self.content:
            i.move([sum(lis) for lis in zip((self.x, self.y), self.baseRectoffset, (self.width/2-i.width/2, -(i.positAddress+1)*self.thickness))])

    def cursorhere(self, cur: CursorInstance):
        cur.x = self.poleRect.x+(self.thickness-cur.width)/2
        cur.y = self.y-canvasSize[1]/5
        if cur.content:
            cur.content.move((cur.x, cur.y))
        cur.pointingat = self.position

    def addhoop(self, hInstance: HoopInstance):
        self.content.append(hInstance)
        self.topsize = hInstance.size()
        hInstance.poleAddress = self.position
        hInstance.positAddress = len(self.content)-1
        hInstance.move([sum(lis) for lis in zip((self.x, self.y), self.baseRectoffset, (self.width/2-hInstance.width/2, -(hInstance.positAddress+1)*self.thickness))])

    def removehoop(self) -> HoopInstance:
        hInstance = self.content[-1]
        self.content.pop(-1)
        if self.content:
            self.topsize = self.content[-1].size()
        else:
            self.topsize = 256
        return hInstance


def redrawSurfaces():
    global updateSurfacesFLAG
    if not updateSurfacesFLAG:
        print('Redrawing Surface Canvas...')
        updateSurfacesFLAG = True


# initializing the pg import
pg.init()
canvasSize = (900, 500)
canvas = pg.display.set_mode(canvasSize)
pg.display.set_caption('hhoops 0.2.0b InDev')


# test
actionHistory = []
cursor = CursorInstance(0, 0)
poleINFO = [PoleInstance(0, 0, 100, 100)]
hoopINFO = [HoopInstance(0, 0, 100, 24)]
# poleINFO = [PoleInstance(50, 250, 100, 100), PoleInstance(175, 250, 100, 100), PoleInstance(300, 250, 100, 100)]
# poleINFO = [PoleInstance((0.5+i)*(canvasSize[0]/(3+1)), canvasSize[1] / 2, 24*(4+2), 100) for i in range(3)]
# hoopINFO = [HoopInstance(100, 100, 100, 24), HoopInstance(100, 100, 80, 24), HoopInstance(100, 100, 60, 24)]
# poleINFO[0].addhoop(hoopINFO[0])
# poleINFO[0].addhoop(hoopINFO[1])
# poleINFO[0].addhoop(hoopINFO[2])
# poleINFO[0].cursorhere(cursor)

runningFLAG = True
updateSurfacesFLAG = True
kPressedFLAG = False

def startgame(poles=3, hoops=5):
    if (poles < 2) or (hoops < 3):
        return
    if hoops > 255:
        print('At a rate of one action every millisecond, you will be solving this puzzle unto the heat death of the universe.')
        print('Try something simpler.')
        hoops = 254
    global poleINFO, hoopINFO, cursor

    poleINFO = [PoleInstance((0.5+i)*(canvasSize[0]/(poles+1)), canvasSize[1]/2, 24*(hoops+2), (hoops+0.618)*24, 24, i) for i in range(poles)]
    pInstance = poleINFO[0]  # the first

    hoopINFO = []
    for i in range(hoops):
        hoopINFO.append(HoopInstance(0, 0, (hoops-i+1)*24, 24))
        pInstance.addhoop(hoopINFO[-1])

    cursor = CursorInstance(0, 0, canvasSize[0]//16, canvasSize[1]//30)
    pInstance.cursorhere(cursor)

startgame()

# Game loop
while runningFLAG:
    # Check for event if user has pushed
    # any event in queue
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningFLAG = False

    keys = pg.key.get_pressed()

    if keys[pg.K_UP]:  # draw all objects' origins
        for i in poleINFO:
            pg.draw.circle(canvas, (255, 0, 0), (i.x, i.y), 10, 1)
            pg.draw.circle(canvas, (0, 255, 0), (i.poleRect.x, i.poleRect.y), 5, 1)
            pg.draw.circle(canvas, (0, 0, 255), (i.baseRect.x, i.baseRect.y), 5, 1)
        for i in hoopINFO:
            pg.draw.circle(canvas, (255, 0, 0), (i.hoopRect.x, i.hoopRect.y), 10, 1)
        pg.draw.circle(canvas, (255, 0, 0), cursor.getpoints()[0], 10, 1)

    ptat = cursor.pointingat
    if keys[pg.K_DOWN]:  # test pole mov
        if kPressedFLAG:
            print(actionHistory)
            if poleINFO[ptat].content and not cursor.content:  # take
                cursor.addhoop(poleINFO[ptat].removehoop())
                actionHistory.append([ptat, 0])
            elif cursor.content and cursor.topsize < poleINFO[ptat].topsize:  # place
                poleINFO[ptat].addhoop(cursor.removehoop())
                if actionHistory[-1][0] == ptat:
                    actionHistory.pop(-1)
                else:
                    actionHistory[-1][1] = ptat
        kPressedFLAG = False
    elif keys[pg.K_LEFT]:
        if kPressedFLAG:
            if ptat:
                poleINFO[ptat-1].cursorhere(cursor)
            else:
                poleINFO[-1].cursorhere(cursor)
        kPressedFLAG = False
    elif keys[pg.K_RIGHT]:
        if kPressedFLAG:
            if ptat == len(poleINFO)-1:
                poleINFO[0].cursorhere(cursor)
            else:
                poleINFO[ptat+1].cursorhere(cursor)
        kPressedFLAG = False
    else:
        kPressedFLAG = True

    if updateSurfacesFLAG:
        pg.display.update()
        canvas.fill((10, 10, 10))
        for i in poleINFO:
            pg.draw.rect(canvas, (255, 0, 0), i.poleRect, 1)
            pg.draw.rect(canvas, (255, 0, 0), i.baseRect, 1)
        for i in hoopINFO:
            pg.draw.rect(canvas, (0, 255, 0), i.hoopRect, 1)
        pg.draw.polygon(canvas, (0, 255, 0), cursor.getpoints())



