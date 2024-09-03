import cmd
import time


class HoopInstance:
    def __init__(self):
        self.name = 'Empty'
        self.size = 256
        self.poleAddress = 0  # from left to right
        self.polePointer = None
        self.positAddress = 0  # start from bottom


class PoleInstance:

    def __init__(self):
        self.name = ''
        self.position = 0  # start from left
        self.content = []  # end of list (for some reason)
        self.topsize = 256  # if we make this zero stuff breaks

    def removehoop(self):
        hInstance = self.content[-1]
        self.content.pop(-1)
        if self.content:
            self.topsize = self.content[-1].size
        else:
            self.topsize = 256
        return hInstance

    def addhoop(self, hInstance):
        self.content.append(hInstance)
        self.topsize = hInstance.size
        hInstance.poleAddress = self.position
        hInstance.positAddress = len(self.content)


poleINFO = [PoleInstance()]
hoopINFO = [HoopInstance()]
userMovesMade = 0
userTimeStart = 0
userMoveHistory = [[0, 1]]


def startgame(hoopcount=4, polecount=3):  # incl. globals
    if (hoopcount < 2) or (polecount < 3):
        return
    global poleINFO
    poleINFO = []
    global hoopINFO
    hoopINFO = []
    for i in range(polecount):
        newInstance = PoleInstance()
        if polecount == 3:
            newInstance.name = ('Left', 'Middle', 'Right')[i]
        newInstance.position = i
        poleINFO.append(newInstance)

    count = 0
    for i in range(hoopcount):
        count += 1
        hInstance = HoopInstance()
        hInstance.name = 'Grey Shade No.' + str(50 - i)
        hInstance.size = hoopcount - i
        hInstance.poleAddress = 0
        hInstance.positAddress = count
        hInstance.polePointer = newInstance
        hoopINFO.append(hInstance)

    poleINFO[0].content = hoopINFO.copy()
    poleINFO[0].topsize = hoopINFO[-1].size
    global userTimeStart
    userTimeStart = time.time()
    global userMoveHistory
    userMoveHistory = []
    print('Game has started!')


def look():
    screen = [[0 for j in poleINFO] for i in hoopINFO]  # oh, this looks nice
    maxsize = len(hoopINFO)
    for i in hoopINFO:
        screen[i.positAddress-1][i.poleAddress] = i.size
    for i in screen[::-1]:
        for j in i:
            if j:
                print(' ' * (maxsize - j + 1), '#' * j, '||', '#' * j, ' ' * (maxsize - j + 1), sep='', end='')
            else:
                print(' ' * (maxsize + 1), '||', ' ' * (maxsize+1), sep='', end='')
        print('')
    print('', ('=' * (maxsize * 2 + 2) + '  ') * len(poleINFO))


def undo():
    global userMovesMade
    global userMoveHistory
    print(userMoveHistory)
    if not userMovesMade:
        print('No Moves Made!')
        return
    move(userMoveHistory[-1][1], userMoveHistory[-1][0])
    userMoveHistory.remove(userMoveHistory[-1])
    userMovesMade -= 1


def move(beginpos, endpos):
    if beginpos == endpos:
        return
    elif not poleINFO[beginpos].content:
        return
    elif poleINFO[beginpos].topsize >= poleINFO[endpos].topsize:
        return
    else:
        print('Success!')
        poleINFO[endpos].addhoop(poleINFO[beginpos].removehoop())
        poleINFO[endpos].content[-1].polePointer = poleINFO[endpos]
        global userMovesMade
        userMovesMade += 1
        global userMoveHistory
        userMoveHistory.append([beginpos, endpos])


def checkifcompleted():
    skippedFirst = False
    for i in poleINFO:
        if not skippedFirst:
            skippedFirst = True
            continue
        elif len(i.content) == len(hoopINFO):
            print(f"Game Completed {len(hoopINFO)} hoops, {len(poleINFO)} poles"
                  f"\nMoves: {userMovesMade} Time: {time.time()-userTimeStart:.1f}s")
    return False


class Mainprompt(cmd.Cmd):
    def do_move(self, arg):
        """Move a hoop from a pole [start pole position],[end pole position]"""
        if not arg:
            return
        if arg.replace(',', '').isnumeric:
            arg = [int(i) for i in arg.split(',')]
        move(arg[0], arg[1])
        if checkifcompleted():
            print('Completed!')

    def do_undo(self, arg):
        """Undo previous move"""
        undo()  # HOW WHY
        undo()  # HOW DOES IT WORK IF I DO IT TWICE

    def do_rset(self, arg):
        startgame(len(hoopINFO), len(poleINFO))

    def do_start(self, arg):
        """Start the game: [no. of hoops],[no. of poles] <-- Optional!"""
        if not arg:
            startgame()
        elif arg.replace(',', '').isnumeric:
            arg = [int(i) for i in arg.split(',')]
        else:
            print('Invalid Commands')
        if len(arg) == 2:
            startgame(arg[0], arg[1])
        elif len(arg) == 1:
            startgame(arg[0])

    def do_look(self, arg):
        look()

    def do_geth(self, arg):
        """Util"""
        if not arg:
            print(hoopINFO)
            return
        if not arg.isnumeric():
            return
        arg = int(arg)
        if arg >= len(hoopINFO):
            return

        targInstance = hoopINFO[int(arg)]
        print(targInstance.positAddress)
        print(targInstance.poleAddress)

    def do_getp(self, arg):
        """Util"""
        if not arg:
            print(poleINFO)
            return
        if not arg.isnumeric():
            return
        arg = int(arg)
        if arg >= len(hoopINFO):
            return

        targInstance = poleINFO[int(arg)]
        print(targInstance.content)

    def do_quit(self, arg):
        """End Program"""
        raise SystemExit


prompt = Mainprompt()
prompt.prompt = 'Input Command >>>:'
prompt.cmdloop('...')
