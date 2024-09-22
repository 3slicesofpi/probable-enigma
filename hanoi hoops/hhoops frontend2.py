import pygame
import pygame as pg
from time import time

class Colours:
    fullwhite = (255, 255, 255)
    fullblack = (0, 0, 0)
    fullred = (255, 0, 0)
    fullgreen = (0, 255, 0)
    fullblue = (0, 0, 255)
    fullyellow = (255, 255, 0)
    fullsky = (0, 255, 255)
    basicdarkgrey = (50, 50, 50)
    basicgrey = (100, 100, 100)
    basiclightgrey = (155, 155, 155)
    basicdarkwhite = (200, 200, 200)
    basicred = (200, 50, 50)
    basicgreen = (50, 200, 50)
    basicblue = (50, 50, 200)
    darkred = (105, 20, 20)
    darkgreen = (20, 105, 20)
    darkblue = (20, 20, 105)
    lightred = (200, 150, 150)
    lightblue = (150, 150, 200)
    lightgreen = (150, 200, 150)


class HoopInstance:
    def __init__(self, x_left, y_top, width, height, colour=Colours.basicblue):
        self.thickness = height
        self.width = width
        self.poleAddress = 0  # from left to right
        self.polePointer = None
        self.positAddress = 0  # start from bottom, count from 0
        self.hoopRect = pg.Rect(x_left, y_top, width, height)
        self.colour = colour

    def move(self, pos: [float, float]):
        self.hoopRect.x, self.hoopRect.y = pos

    def size(self) -> int:
        return self.width//self.thickness

    def render(self):
        pg.draw.rect(canvas, self.colour, self.hoopRect)


class CursorInstance:
    def __init__(self, x_left, y_top, width=50, height=20, colour=Colours.fullgreen):
        self.x = x_left
        self.y = y_top
        self.width = width
        self.height = height
        self.pointingat = 0
        self.content = None
        self.topsize = 256
        self.colour = colour

    def getpoints(self) -> [[float, float], [float, float], [float, float]]:
        return (self.x, self.y), (self.x + self.width / 2, self.y + self.height), (self.x + self.width, self.y)

    def moveattachedcontent(self):
        if self.content:
            self.content.move([sum(lis) for lis in zip((self.x, self.y), (self.width/2, -self.height*2), (-self.content.width/2, 0))])

    def addhoop(self, hInstance: HoopInstance):
        self.content = hInstance
        self.topsize = hInstance.size()
        hInstance.poleAddress = -1
        hInstance.positAddress = 0
        self.moveattachedcontent()
        redrawSurfaces()

    def removehoop(self) -> HoopInstance:
        hInstance = self.content
        self.content = None
        self.topsize = 256
        return hInstance

    def render(self):
        pg.draw.polygon(canvas, self.colour, self.getpoints())


class PoleInstance:
    def __init__(self, x_left, y_top, width, height, thickness=24, position=0, colour=Colours.basicred):
        self.x = x_left  # origin pos
        self.y = y_top
        self.colour = colour
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
        cur.moveattachedcontent()
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

    def render(self):
        pg.draw.rect(canvas, self.colour, self.poleRect)
        pg.draw.rect(canvas, self.colour, self.baseRect)


class Button(pg.Rect):
    def __init__(self, x_left, y_top, width, height, text: str, textCol=Colours.basicdarkwhite):
        super().__init__(x_left, y_top, width, height)
        self.textcontent = [font.render(i, True, textCol) for i in text.split('\n')]


class Slider:
    def __init__(self, x_left, y_top, width, height, thickness, text: str, limits: (int, int)):
        if (2*thickness >= width) or (2*thickness >= height):
            return
        self.backRect = pg.Rect(x_left, y_top, width, height)
        self.decreaseRect = pg.Rect(x_left-thickness/2, y_top+thickness/2, width/3-thickness, height)
        self.increaseRect = pg.Rect(x_left+width*2/3+1.5*thickness, y_top-thickness/2, width/3-thickness, height)
        self.textcontent = text
        self.updatetext(f"{text} {limits[0]}")
        self.value = limits[0]
        self.limit = limits

    def updatetext(self, newtext):
        self.text = font.render(newtext, True, Colours.basicdarkwhite)

    def pressdec(self):
        if self.value == self.limit[0]:
            pass
        else:
            self.value -= 1
            self.updatetext(f"{self.textcontent} {self.value}")

    def pressinc(self):
        if self.value == self.limit[1]:
            pass
        else:
            self.value += 1
            self.updatetext(f"{self.textcontent} {self.value}")


def redrawSurfaces():
    global updateSurfacesFLAG
    if not updateSurfacesFLAG:
        print('Redrawing Surface Canvas...')
        updateSurfacesFLAG = True


def checkgamecompleted() -> bool:
    for i in poleINFO[1:]:
        if len(i.content) == len(hoopINFO):
            global showendFLAG, endtext
            showendFLAG = True
            endtext = [font.render(i, True, (255, 255, 255)) for i in (
                  f'Completed!'
                  f'\n{len(hoopINFO)} Hoops, {len(poleINFO)} Poles,'
                  f'\n{len(actionHistory)} Moves in {time() - startimeUser:.1f}s'
                  f'\n{undocountUSER} Undos'
                  f'\nBest Possible Move Count: {len(hoopINFO) ** 2 - 1}').split('\n')]
            return True
        else:
            print('Not Completed!')
    return False


def undoaction() -> bool:
    if cursor.content:
        poleINFO[actionHistory[-1][0]].addhoop(cursor.removehoop())
        actionHistory.pop(-1)
        return True
    elif len(actionHistory):
        global undocountUSER
        undocountUSER += 1
        poleINFO[actionHistory[-1][0]].addhoop(poleINFO[actionHistory[-1][1]].removehoop())
        actionHistory.pop(-1)
        return True
    else:
        print('Action not successful.')
        return False


def showmenu():
    global showmenuFLAG
    if not showmenuFLAG:
        print('Showing Menu...')
        showmenuFLAG = True


# initializing the pg import
pg.init()
font = pg.font.Font('freesansbold.ttf', 20)
canvasSize = (1000, 600)
canvas = pg.display.set_mode(canvasSize)
pg.display.set_caption('Prototype 2 -- hhoops 0.2.5 Alpha Release')
startimeUser = 0
# test
actionHistory = []
cursor = CursorInstance(0, 0)
poleINFO = [PoleInstance(0, 0, 100, 100)]
hoopINFO = [HoopInstance(0, 0, 100, 24)]
undocountUSER = 0

checkBUTTON = Button(canvasSize[0]-40, canvasSize[1]/2+100, 40, 180, 'C\nH\nE\nC\nK\n', Colours.darkgreen)
undoBUTTON = Button(canvasSize[0]-40, canvasSize[1]/2, 40, 60, 'U\nN\nD\nO\n', Colours.darkred)
menuBUTTON = Button(0, 24, 40, 72, 'M\nE\nN\nU\n', Colours.darkblue)

menuScreen = pg.Rect(canvasSize[0]/10, canvasSize[1]/10, canvasSize[0]*0.8, canvasSize[1]*0.8)
closemenuBUTTON = Button(menuScreen.x, menuScreen.y, 55, 20, 'X', Colours.fullwhite)
quitgameBUTTON = Button(menuScreen.x+menuScreen.width-105, menuScreen.y+menuScreen.height-29, 105, 35, 'QUIT')

numhoopsSLIDER = Slider(180, 100, menuScreen.width/3.5, 48, 12, 'Hoops:', (2, 64))
numpolesSLIDER = Slider(180, 200, menuScreen.width/3.5, 48, 12, 'Poles:', (3, 5))

newgameBUTTON = Button(menuScreen.x, menuScreen.y+menuScreen.height-29, menuScreen.width/2.5, 35, 'NEW GAME')

endtext = menuBUTTON.textcontent
runningFLAG = True
updateSurfacesFLAG = True
kPressedFLAG = False
showmenuFLAG = True
showendFLAG = False

def startgame(poles=3, hoops=5):
    if hoops > 255:
        print('At a rate of one action every millisecond,'
              'you will be solving this puzzle unto the heat death of the universe.')
        print('Try something simpler.')
        hoops = 254
    global poleINFO, hoopINFO, cursor, startimeUser, actionHistory, undocountUSER
    startimeUser = time()
    actionHistory = []
    undocountUSER = 0

    poleINFO = [PoleInstance((0.5+i)*(canvasSize[0]/(poles+1)), canvasSize[1]/2-(hoops+0.618)*10, 24*(hoops+2), (hoops+0.618)*24, 24, i) for i in range(poles)]
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

    # MOSTLY COLLISION DETECTION
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningFLAG = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if checkBUTTON.collidepoint(event.pos):
                checkgamecompleted()
            if undoBUTTON.collidepoint(event.pos):
                undoaction()
            if menuBUTTON.collidepoint(event.pos):
                showmenu()
            if showmenuFLAG:  # button interactions in menu
                if numhoopsSLIDER.increaseRect.collidepoint(event.pos):
                    numhoopsSLIDER.pressinc()
                if numhoopsSLIDER.decreaseRect.collidepoint(event.pos):
                    numhoopsSLIDER.pressdec()
                if numpolesSLIDER.increaseRect.collidepoint(event.pos):
                    numpolesSLIDER.pressinc()
                if numpolesSLIDER.decreaseRect.collidepoint(event.pos):
                    numpolesSLIDER.pressdec()
            if showendFLAG or showmenuFLAG:
                if newgameBUTTON.collidepoint(event.pos):
                    if showmenuFLAG:
                        showmenuFLAG = False
                        startgame(numpolesSLIDER.value, numhoopsSLIDER.value)
                    elif showendFLAG:
                        showendFLAG = False
                        showmenuFLAG = True
                if closemenuBUTTON.collidepoint(event.pos):
                    showendFLAG = False
                    showmenuFLAG = False
                if quitgameBUTTON.collidepoint(event.pos):
                    raise SystemExit
            else:
                for i in poleINFO:
                    if i.poleRect.collidepoint(event.pos) or i.baseRect.collidepoint(event.pos):
                        i.cursorhere(cursor)
                        if cursor.content and cursor.topsize < i.topsize:  # place
                            i.addhoop(cursor.removehoop())
                            if actionHistory[-1][0] == i.position:
                                actionHistory.pop(-1)
                            else:
                                actionHistory[-1][1] = i.position
                        elif i.content and not cursor.content:  # take
                            cursor.addhoop(i.removehoop())
                            actionHistory.append([i.position, 0])
            redrawSurfaces()

    keys = pg.key.get_pressed()
    # CONTROL

    if keys[pg.K_UP]:  # draw all objects' origins
        for i in poleINFO:
            pg.draw.circle(canvas, (255, 0, 0), (i.x, i.y), 10, 1)
            pg.draw.circle(canvas, (0, 255, 0), (i.poleRect.x, i.poleRect.y), 5, 1)
            pg.draw.circle(canvas, (0, 0, 255), (i.baseRect.x, i.baseRect.y), 5, 1)
        for i in hoopINFO:
            pg.draw.circle(canvas, (255, 0, 0), (i.hoopRect.x, i.hoopRect.y), 10, 1)
        pg.draw.circle(canvas, (255, 0, 0), cursor.getpoints()[0], 10, 1)
        pg.draw.circle(canvas, (255, 0, 0), (menuScreen.x, menuScreen.y), 10, 1)
        pg.display.update()
        print(actionHistory)
    ptat = cursor.pointingat
    if keys[pg.K_DOWN]:  # test pole mov
        if kPressedFLAG:
            if poleINFO[ptat].content and not cursor.content:  # take
                cursor.addhoop(poleINFO[ptat].removehoop())
                actionHistory.append([ptat, 0])
            elif cursor.content and cursor.topsize < poleINFO[ptat].topsize:  # place
                poleINFO[ptat].addhoop(cursor.removehoop())
                if actionHistory[-1][0] == ptat:
                    actionHistory.pop(-1)
                else:
                    actionHistory[-1][1] = ptat
            redrawSurfaces()
            # print(actionHistory)
        kPressedFLAG = False
    elif keys[pg.K_c]:
        if kPressedFLAG:
            checkgamecompleted()
            redrawSurfaces()
    elif keys[pg.K_u]:
        if kPressedFLAG:
            kPressedFLAG = False
            undoaction()
            redrawSurfaces()
        else:
            kPressedFLAG = False
    elif keys[pg.K_r]:
        if kPressedFLAG:  # just so I won't blow up the computer when startgame is called
            startgame(numpolesSLIDER.value, numhoopsSLIDER.value)
            showmenuFLAG = False
            redrawSurfaces()
        else:
            kPressedFLAG = False
    elif keys[pg.K_LEFT]:
        if kPressedFLAG:
            if ptat:
                poleINFO[ptat-1].cursorhere(cursor)
            else:
                poleINFO[-1].cursorhere(cursor)
            redrawSurfaces()
        kPressedFLAG = False
    elif keys[pg.K_RIGHT]:
        if kPressedFLAG:
            if ptat == len(poleINFO)-1:
                poleINFO[0].cursorhere(cursor)
            else:
                poleINFO[ptat+1].cursorhere(cursor)
            redrawSurfaces()
        kPressedFLAG = False
    else:
        kPressedFLAG = True

    if updateSurfacesFLAG:
        canvas.fill(Colours.basicdarkwhite)

        if showendFLAG or showmenuFLAG:
            pg.draw.rect(canvas, Colours.basiclightgrey, menuScreen)

            pg.draw.rect(canvas, Colours.basicblue, newgameBUTTON)
            canvas.blit(newgameBUTTON.textcontent[0], (newgameBUTTON.x+4, newgameBUTTON.center[1]))

            pg.draw.rect(canvas, Colours.basicred, closemenuBUTTON)
            canvas.blit(closemenuBUTTON.textcontent[0], (closemenuBUTTON.x+4, closemenuBUTTON.y-4))

            pg.draw.rect(canvas, Colours.basicred, quitgameBUTTON)
            canvas.blit(quitgameBUTTON.textcontent[0], (quitgameBUTTON.center[0], quitgameBUTTON.center[1]))

            if showmenuFLAG:
                canvas.blit(font.render('SELECT DIFFICULTY', True, Colours.fullblack), (menuScreen.center[0]-font.size('SELECT DIFFICULTY')[0]/2, menuScreen.y-4))

                pg.draw.rect(canvas, Colours.basicred, closemenuBUTTON)
                canvas.blit(closemenuBUTTON.textcontent[0], (closemenuBUTTON.x+4, closemenuBUTTON.y-4))

                pg.draw.rect(canvas, Colours.basicgrey, numhoopsSLIDER.backRect)
                pg.draw.rect(canvas, Colours.basicgreen, numhoopsSLIDER.increaseRect)
                pg.draw.rect(canvas, Colours.basicred, numhoopsSLIDER.decreaseRect)
                canvas.blit(numhoopsSLIDER.text, (numhoopsSLIDER.backRect.center[0]-numhoopsSLIDER.text.__sizeof__()/2-12, numhoopsSLIDER.backRect.center[1]-font.size('a')[1]/2))

                pg.draw.rect(canvas, Colours.basicgrey, numpolesSLIDER.backRect)
                pg.draw.rect(canvas, Colours.basicgreen, numpolesSLIDER.increaseRect)
                pg.draw.rect(canvas, Colours.basicred, numpolesSLIDER.decreaseRect)
                canvas.blit(numpolesSLIDER.text, (numpolesSLIDER.backRect.center[0]-numpolesSLIDER.text.__sizeof__()/2-12, numpolesSLIDER.backRect.center[1] - font.size('a')[1] / 2))


            if showendFLAG:
                canvas.blit(font.render('COMPLETE', True, Colours.fullblack), (menuScreen.center[0]-font.size('THE MENU')[0]/2, menuScreen.y-4))

                for i, count in zip(endtext, range(len(endtext))):
                    canvas.blit(i, (menuScreen.x+48, menuScreen.y+24+font.size('a')[1]*count))

        else:
            for i in poleINFO:
                i.render()
            for i in hoopINFO:
                i.render()
            cursor.render()

            pg.draw.rect(canvas, Colours.lightgreen, checkBUTTON)
            pg.draw.rect(canvas, Colours.lightred, undoBUTTON)
            pg.draw.rect(canvas, Colours.lightblue, menuBUTTON)

            for i, count in zip(undoBUTTON.textcontent, range(len(undoBUTTON.textcontent))):
                canvas.blit(i, (undoBUTTON.x+4, undoBUTTON.y+(count-1)*font.size('a')[1]-4))  # TEMPORARY!!! this sucks
            for i, count in zip(checkBUTTON.textcontent, range(len(checkBUTTON.textcontent))):
                canvas.blit(i, (checkBUTTON.x+4, checkBUTTON.y+(count-1)*font.size('a')[1]-4))
            for i, count in zip(menuBUTTON.textcontent, range(len(menuBUTTON.textcontent))):
                canvas.blit(i, (menuBUTTON.width-font.size('A')[0]-4, menuBUTTON.y+(count-1)*font.size('a')[1]-4))

        updateSurfacesFLAG = False
        pg.display.update()
