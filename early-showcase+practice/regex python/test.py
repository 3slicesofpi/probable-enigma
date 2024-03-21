import re
from random import randint as rnd
from random import getrandbits
prevMenuVisited = 'menuStart'

def clientInput(raw):
    match raw[0].lower():
        case 'h':
            return 'menuHelp'
        case 'r':
            return prevMenuVisited
        case 'e':
            return 'menuStart'
        case 'd': # dont print
            return 'menuDirect'
        case 's': # dont print
            return 'menuSessionSetup'
        case 'q':
            return 'menuQuit'
        case _:
            return raw

    
def menuStart():
    print('''''')
    command = clientInput(input('>>>:'))
    if command.isnumeric():
        match int(command):
            case 1:
                return 'menuClassic'
            case 2:
                return 'menuCustom'
            case 3: 
                return 'menuTutorial'
            case 4:
                return 'menuScenario'
            case _:
                print('Invaild Input: Command out of range. Try again.')
                return prevMenuVisited
    else:
        return command
    
print(menuStart())