import pygame as pg
import sys

# Initialize pygame
pg.init()
basicfont = pg.font.Font(None,28)

def conv_rel(perc_x, perc_y):
    cS = list(canvasSize)
    cS[0] *= perc_x
    cS[1] *= perc_y
    return cS

# Constants
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

canvasSize = (800, 600)
FPS = 60  # Frames per second

# Create the screen (window)
canvas = pg.display.set_mode(canvasSize)

# Set the title of the window
pg.display.set_caption("pygame Interactives Framework 0.0.8 InDev")

# Clock to control the frame rate
clock = pg.time.Clock()

class Domain:
    def __init__(self):
        self.status = False
        self.ObjectContent = []
        self.ObjectRender = []
        self.ObjectDebug = []
        self.DetectHover = []
        self.DetectPress = []

    def render(self):
        if self.status:
            for i in self.ObjectRender:
                i.render()

    def render_debug(self, override=False):
        if self.status or override:
            for i in self.ObjectDebug:
                i.render_debug()

    def detect_hover(self, pos, override=False):
        if self.status or override:
            for i in self.DetectHover:
                i.detect_hover(pos)

    def detect_press(self, ispressed, override=False):
        if self.status or override:
            for i in self.DetectPress:
                i.detect_press(ispressed)


class Model:
    """May be split into Model and Hitbox class, where Hitbox -> Model -> ..."""
    def __init__(self, hitbox: pg.Rect, debugcol=Colours.fullsky):
        self.hitbox = hitbox
        self.debugcol = debugcol

        self.rectContent = []
        self.rectColour = []
        self.rectOffset = []

        self.textContent = []
        self.textRaw = []
        self.textColour = []
        self.textOffset = []

    def add_rect(self, rect: pg.Rect, rectcol=Colours.fullgreen, offset=(0, 0)):
        """Best Practice: Add Rects while Model is at 0, 0, autooffset will do the rest."""
        rect.x += offset[0]
        rect.y += offset[1]
        self.rectContent.append(rect)
        self.rectColour.append(rectcol)
        self.rectOffset.append([sum(i) for i in zip((self.hitbox.x, self.hitbox.y), (rect.x, rect.y), offset)])

    def add_text(self, text: str, textcol=Colours.fullblack, offset=(0, 0), font=basicfont):
        self.textColour.append(textcol)
        self.textOffset.append(offset)
        self.textRaw.append(text)
        self.textContent.append([font.render(i, True, textcol) for i in text.split('\n')])

    def move(self, newpos):
        self.hitbox.x, self.hitbox.y = (self.hitbox.x + newpos[0], self.hitbox.y + newpos[1])
        for content, offset in zip(self.rectContent, self.rectOffset):
            content.x, content.y = newpos[0] + offset[0], newpos[1] + offset[1]

    def render(self):
        for content, colour in zip(self.rectContent, self.rectColour):
            pg.draw.rect(canvas, colour, content)

        for content, offset in zip(self.textContent, self.textOffset):
            for textline, count in zip(content, range(len(content))):
                canvas.blit(textline, [sum(i) for i in zip((self.hitbox.x, self.hitbox.y), offset, (0, basicfont.get_height()*count))])

    def debug_render(self):
        pg.draw.rect(canvas, self.debugcol, self.hitbox, 1)


class GenericStatic:
    def __init__(self, domain: Domain, origin, basemodel: Model, baseoffset=(0, 0)):
        self.origin = origin
        self.ModelSelected = 'base'
        self.ModelContent = {'base': basemodel}
        self.ModelOffset = {'base': baseoffset}

        self.DomainContent = []
        self.add_domain(domain)

    def add_domain(self, *domain: Domain):
        self.DomainContent.extend(domain)

        for i in domain:
            i.ObjectContent.append(self)
            i.ObjectRender.append(self)
            i.ObjectDebug.append(self)

    def move(self, pos):
        for content, offset in zip(self.ModelContent.values(), self.ModelOffset.values()):
            content.move((pos[0] + offset[0], pos[1] + offset[1]))

    def render(self):
        self.ModelContent[self.ModelSelected].render()

    def render_debug(self):
        self.ModelContent[self.ModelSelected].debug_render()

    def debug_checkkeys(self, key):
        if key in self.ModelContent and key in self.ModelOffset:
            return True
        else:
            return False


class GenericButton(GenericStatic):
    def __init__(self, domain: Domain, origin, basemodel: Model, baseoffset=(0, 0)):
        super().__init__(domain, origin, basemodel, baseoffset)

        self.mouseHoverState = False
        self.mousePressState = False

    def add_domain(self, *domain: Domain):
        self.DomainContent.extend(domain)
        haspress = False
        if self.debug_checkkeys('press'):
            haspress = True

        for i in domain:
            i.ObjectContent.append(self)
            i.ObjectRender.append(self)
            i.ObjectDebug.append(self)
            i.DetectHover.append(self)
            if haspress:
                i.DetectPress.append(self)

    def add_model(self, model: Model, modelname='base'):
        if modelname == 'press':
            for i in self.DomainContent:
                i.DetectPress.append(self)
        self.ModelContent[modelname] = model
        self.ModelOffset[modelname] = (self.origin[0] - model.hitbox.x, self.origin[1] - model.hitbox.y)

    def detect_hover(self, pos):
        """Activates on mouse move. Requires 'hover' keys."""

        # GAHHHH!!!! MULTIPLE HITBOXES!!!!!
        if self.debug_checkkeys('hover'):
            if self.ModelContent['hover'].hitbox.collidepoint(pos) or self.ModelContent['base'].hitbox.collidepoint(pos):
                self.mouseHoverState = True
                self.ModelSelected = 'hover'
                return
        else:
            if self.ModelContent['base'].hitbox.collidepoint(pos):
                self.mouseHoverState = True
                return
        self.mouseHoverState = False
        self.mousePressState = False
        self.ModelSelected = 'base'
        return

    def detect_press(self, ispressed: bool):
        """Activates when mouse click"""
        if self.mouseHoverState:
            if ispressed:
                self.mousePressState = True
                self.ModelSelected = 'press'
            else:
                self.mousePressState = False
                if self.debug_checkkeys('hover'):
                    self.ModelSelected = 'hover'
                else:
                    self.ModelSelected = 'base'


testDomain = Domain()
testDomain.status = True

# testModelInstance = Model(pg.Rect(0, 0, 100, 50))
# testModelInstance.add_rect(pg.Rect(0, 0, 100, 50), Colours.basicgrey)
# testModelInstance.add_rect(pg.Rect(10, 10, 80, 30))
# testButton = GenericButton(testDomain, (0, 0), testModelInstance)
# testModelInstance1 = Model(pg.Rect(100, 0, 100, 50))
# testModelInstance1.add_text('wor\nks', Colours.basicred, (20, 5))
# testModelInstance1.add_rect(pg.Rect(0, 0, 100, 50), Colours.basicgrey)
# testModelInstance1.add_rect(pg.Rect(10, 10, 80, 30), Colours.basicred)
# testButton.add_model(testModelInstance1, 'press')
# testModelInstance2 = Model(pg.Rect(100, 100, 100, 50))
# testButton.add_model(testModelInstance2, 'hover')

menuDomain = Domain()
menuDomain.status = True

baseMenuModel = Model(pg.Rect((0, 0), conv_rel(0.64, 1)))
baseMenuModel.add_rect(pg.Rect(conv_rel(-0.05, 0.08), conv_rel(0.74, 0.86)), (190, 190, 190))
baseMenuModel.add_rect(pg.Rect(conv_rel(-0.025, 0.04), conv_rel(0.69, 0.94)), (182, 182, 182))
baseMenuModel.add_rect(baseMenuModel.hitbox, (174, 174, 174))
baseMenuStatic = GenericStatic(menuDomain, (0, 0), baseMenuModel)
baseMenuStatic.move((canvasSize[0]*0.18, -2))

closeMenuButton_base = Model(pg.Rect(0, 0, 80, 30))
closeMenuButton_base.add_rect(pg.Rect(44, 0, 10, 28), Colours.basicred)
closeMenuButton_base.add_text('X', Colours.darkred, (40, 5))
closeMenuButton_hover = Model(pg.Rect(0, 0, 100, 30))
closeMenuButton_hover.add_rect(pg.Rect(4, 0, 50, 28), Colours.basicred)
closeMenuButton_hover.add_text('X', Colours.darkred, (40, 5))
closeMenuButton = GenericButton(menuDomain, (0, 0), closeMenuButton_base)
closeMenuButton.add_model(closeMenuButton_hover, 'hover')
closeMenuButton.add_model(Model(pg.Rect(0, 0, 0, 0)), 'press')
closeMenuButton.move(conv_rel(0.113, 0.1))

continueMenuButton_base = Model(pg.Rect(0, 0, 160, 45))
continueMenuButton_base.add_rect(continueMenuButton_base.hitbox, (91, 125, 235))
continueMenuButton = GenericButton(menuDomain, (0, 0), continueMenuButton_base)
continueMenuButton.add_model(Model(pg.Rect(0, 0, 0, 0)), 'press')
continueMenuButton.move(conv_rel(0.78, 0.8))

domainREGISTRY = [testDomain, menuDomain]


mousePosition = pg.mouse.get_pos()
mouseButton = (False, False, False)


def renderloop():
    canvas.fill(Colours.basicdarkwhite)
    for i in domainREGISTRY:
        i.render()
        i.detect_hover(mousePosition)
        i.detect_press(mouseButton[0])
    pg.display.flip()


# Main game loop
def main():
    global mousePosition, mouseButton  # it's in main() so it's ok
    running = True
    while running:
        # Event handling loop
        if pg.mouse.get_focused():
            mousePosition = pg.mouse.get_pos()
            mouseButton = pg.mouse.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Game logic (update section)
        if closeMenuButton.mousePressState:
            closeMenuButton.mousePressState = False
            menuDomain.status = False
        if continueMenuButton.mousePressState:
            continueMenuButton.mousePressState = False
            menuDomain.status = False

        # Rendering (draw section)
        renderloop()
        clock.tick(FPS)

    # Quit pygame
    pg.quit()
    sys.exit()


main()
