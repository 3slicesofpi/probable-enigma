from random import randint
import re
class puzzleFactory():
    level = 0
    maxlen = 0
    question = ''

currentPuzzle = puzzleFactory()
currentPuzzle.maxlen = 1000
match int(input('difficulty: ')):
    case 1:
        match randint(1,5):
            case 1:
                currentPuzzle.question = '\sij+.[c-e]'
            case 2:
                currentPuzzle.question = '[Xi]+\s{2}'
            case 3:
                currentPuzzle.question = '[1-3k]+.t$'
            case 4:
                currentPuzzle.question = '[2-3].[k-i]+'
            case 5:
                currentPuzzle.question = 'd[0-5].[5-7]'
    case 2:
        match randint(1,5):
            case 1:
                currentPuzzle.question = r'\bain'
            case 2:
                currentPuzzle.question = 'r[lki]\Z'
            case 3:
                currentPuzzle.question = '[^a-k].+'
            case 4:
                currentPuzzle.question = '[^268]{5}\s'
            case 5:
                currentPuzzle.question = '[c-j]{6}\S'

print(currentPuzzle.question)
clientInput = input('answer: ')
if re.search(currentPuzzle.question,clientInput) != None:
    print('yay')
else:
    print('no')

