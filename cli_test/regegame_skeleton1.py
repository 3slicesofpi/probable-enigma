import cmd
from random import randint
import re
import csv

def await_input(text):
    if text:
        return input(text)
    else:
        return input('Press {ENTER} to continue. (this is not a prompt) >>>:')

filename = 'puzzleDataFile.csv'
numRetryInformation = (256, 5, 5, 3, 2)  # temporary !!!
puzzleSkipCodes = ('food for thought', 'medieval man', 'black sheep wall', 'modify the phase variance', 'mercy mercy oh have mercy')  # I play starcraft one how do you know?
puzzlePassCodes = 'pass'
puzzleData = {}
puzzleList = {}

class expressionClass():  # no more dicts
    def __init__(self, data):
        self.identifier = data[0]
        self.title = data[1]
        self.expression = data[2]
        self.difficulty = int(data[3])
        self.description = data[4]
        self.solution = data[5]
        self.charlimit = int(data[6])
        # this is awful but i don't want to touch the csv jank
        self.searchterms = list(data[7].removeprefix('[\'').removesuffix('\']').split('\', \''))
        self.searchterms.append(data[0].lower())
        for i in data[1].split(' '):
            self.searchterms.append(i.removesuffix('s').lower())
        self.userSolution = []

# TODO: put puzzleData in puzzleClass
class puzzleClass():  # group of expressions
    def __init__(self):
        self.puzzleData = []
        self.lastscore = 0
        self.highscore = 0
        self.difficulty = 0

    def setPuzzleData(self, puzzle):
        """Overrides self.puzzledata. Takes in a list of class instances"""
        if len(puzzle) < 1:
            return False
        self.puzzleData = puzzle
        self.setDifficulty()
        self.highscore = 0
        self.lastscore = 0

    def extendPuzzleData(self, puzzle):
        """Extends self.puzzledata. Takes in a list of class instances"""
        if len(puzzle) < 1:
            return False
        for i in puzzle:
            if not i in self.puzzleData:
                self.puzzleData.append(i)
                continue
        self.setDifficulty()


    def setDifficulty(self):
        if len(puzzleData) < 1:
            return False
        self.difficulty = 0
        for i in puzzleData.values():
            self.difficulty += i.difficulty
        self.difficulty = self.difficulty/len(puzzleData)
        self.highscore = 0
        self.lastscore = 0


with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        puzzleData[str(row[0])] = expressionClass(row)

def searchMultiplePuzzles(expressionList, searchWords, ifSelectedMessage=False):  # returns a list of instances
    found= []
    searchp = '(' + searchWords.removesuffix(' ').removeprefix(' ').replace(' ', '|') + ')'
    for key, value in expressionList.items():
        for j in value.searchterms:
            if re.findall(searchp, j) and not (value in found):
                found.append(value)
                if ifSelectedMessage:
                    print(f"{value.identifier}-{value.title} {ifSelectedMessage}")
    return found

puzzleList['tutorial'] = puzzleClass()
puzzleList['tutorial'].setPuzzleData(searchMultiplePuzzles(puzzleData, 'uniq:00Ehk'))
puzzleList['example'] = puzzleClass()
puzzleList['example'].setPuzzleData(searchMultiplePuzzles(puzzleData, 'uniq:00Fla'))

def playPuzzle(expressionClass):
    numRetries = numRetryInformation[expressionClass.difficulty]  # TEMPORARY
    while numRetries > 0:
        print(f"Puzzle {expressionClass.identifier}-{expressionClass.title}, Difficulty: {expressionClass.difficulty}"
              f"\nGive valid matches for {expressionClass.expression} with {expressionClass.charlimit} characters"
              f"\n{expressionClass.description}"
              f"\n")
        answer = input('Type in your answer here...')
        countMatches = check_expression_answer(expressionClass.expression, answer)
        if answer == puzzleSkipCodes[expressionClass.difficulty]:
            expressionClass.userSolution.append(answer)
            return {'answer': answer, 'countMatches': 1, 'score': 0}
        elif answer == puzzlePassCodes:
            return {'answer': '', 'countMatches': 0, 'score': 0}
        elif countMatches == 0:
            numRetries -= 1
            print(f"Incorrect Answer. {numRetries} tries left.")
        else:
            print(f"Your answer was correct! {countMatches} vaild matches found!")
            charexceed = len(answer) - expressionClass.charlimit
            scorededuct = 0
            if charexceed > 0:
                scorededuct = charexceed//(5-expressionClass.difficulty)
                print(f"However, you exceeded the character limit by {charexceed}."
                      f"\n{scorededuct} score was deducted.")

            if not answer in expressionClass.userSolution:
                expressionClass.userSolution.append(answer)

            return {'answer': answer, 'countMatches': countMatches, 'score': countMatches - scorededuct}

    print('You have run out of retries. Better luck next time.')
    return {'answer': '', 'countMatches': 0, 'score': 0}


def check_expression_answer(expression, answer):
    return len(re.findall(expression, answer))

def playMultiplePuzzles(puzzlegroupClass):
    count = 0
    score = 0
    completedcount = 0
    for i in puzzlegroupClass.puzzleData:
        count += 1
        print(f"{count}:\n")
        result = playPuzzle(i)
        if result['countMatches'] > 0:
            score += result['score']
            completedcount += 1
    puzzlegroupClass.lastscore = score
    if score > puzzlegroupClass.highscore:
        puzzlegroupClass.highscore = score
    print(f'You completed {completedcount} of {len(puzzlegroupClass.puzzleData)} regex puzzles.'
          f'Your final score is {score}')


class mainmenu(cmd.Cmd):
    def do_play(self, arg):
        """Type in one puzzle id to try one puzzle. play [puzzleid]"""
        if arg:
            arg = [str(i) for i in arg.split(',')]
        else:
            arg = input(f"argument required: expression identifer"
                        f"Please type in the id for the puzzle you wish to attempt.")
            arg = [str(i) for i in arg.split(',')]
        argList = []  # prevent duplicates
        for i in arg:
            if (i.upper() in puzzleData.keys()) or (i.upper() in argList):
                argList.append(i)
        if not argList:
            print('Invaild arguments given, try again.')
            return
        else:
            for j in argList:
                playPuzzle(puzzleData[j.upper()])
            return


    def do_tutorial(self, arg):
        """Learn the basics of matching regex."""
        playMultiplePuzzles(puzzleList['tutorial'])
        return

    def do_learnmore(self, arg):
        """Provide links to online learning resources."""
        print(f"More about Regex -- Online Learning Resources"
              f"\nLearning Resources"
              f"\nRegexOne: A beginner-friendly, interactive tutorial site that teaches regex through simple examples and exercises."
              f"\nhttps://regexone.com"
              f"\nRegular-Expressions.info: A comprehensive resource covering everything from the basics to advanced topics in regex."
              f"\nhttps://www.regular-expressions.info"
              f"\n\nTest Your Regex Expressions"
              f"\nRegex101: An interactive tool that lets you test your regex patterns in real-time. It supports multiple flavors of regex and provides detailed explanations of your regex."
              f"\nhttps://regex101.com"
              f"\nRegExr: Another interactive online regex testing tool that is beginner-friendly and has a library of community-contributed regex patterns."
              f"\nhttps://regexr.com"
              f"\n\nCreation Tools"
              f"\nRegexBuilder: A Windows-based tool for building and testing regex patterns with a simple user interface."
              f"\nhttps://regexbuilder.net"
              f"\nPatternize: A straightforward tool for creating and testing regex patterns with the ability to save and share patterns."
              f"\nhttps://patternize.com")
        await_input(False)
        print('boy oh boy i hope thar these links work')  # boy oh boy i hope these things work
        return

    def do_quit(self, arg):
        """Exits the program"""
        if arg:
            raise SystemExit
        else:
            if input('Are you sure you want to exit?\nPress [Y] to confirm') in ('y', 'Y'):
                raise SystemExit
            else:
                print('Returning to Main Menu...')
                return

    def do_look(self, arg):
        arg = [str(i.lower()) for i in arg.split(',')]
        if arg[0] in puzzleList.keys():
            puzzleSelected = puzzleList[arg]
            print(f"PuzzleGroup Name: {arg} Difficulty: {puzzleSelected.difficulty} Highest Score: {puzzleSelected.highscore}")
            for i in puzzleSelected.puzzleData:
                print(f"Name: {i.identifier}-{i.title} Difficulty: {i.difficulty} Completion: {bool(i.userSolution)}")
            return
        else:
            for i in arg:
                if i in puzzleData.keys():
                    puzzleSelected = puzzleData[i]
                    print(f'Name: {puzzleSelected.identifier}-{puzzleSelected.title} Difficulty: {puzzleSelected.difficulty} Completion: {bool(puzzleSelected.userSolution)}')





    def do_puzzleadd(self, arg):
        """Add expressions. [target puzzlegroup],[expression code]/[new puzzlegroup]"""
        if len(arg) > 1:
            arg = [str(i) for i in arg.split(',')]
        else:
            arg = input(f"More arguments required: Given {len(arg)} of 2"
                        f"Please type in the target puzzlegroup, expression code/new puzzlegroup."
                        "Press {E} to return to main menu")
            if arg in ('e', 'E'):
                return
            arg = [str(i) for i in arg.split(',')]

        if not arg[0] in puzzleList.keys():
            print('Invaild target!')
            return
        if arg[1] in puzzleList.keys():
            puzzleList[arg[0]].extendPuzzleData(puzzleList[arg[1]].puzzleData)
        else:
            target = []
            for i in arg[1:]:
                if i.upper() in puzzleData.keys():
                    target.append(puzzleData[i.upper()])
            puzzleList[arg[0]].extendPuzzleData(target)

    def do_puzzledel(self, arg):
        """Remove Expressions"""
        if len(arg) > 1:
            arg = [str(i) for i in arg.split(',')]
        else:
            arg = input(f"More arguments required: Given {len(arg)} of 2"
                        f"Please type in the target puzzlegroup, expression code/new puzzlegroup."
                        "Press {E} to return to main menu")
            if arg in ('e', 'E'):
                return
            arg = [str(i) for i in arg.split(',')]

        if not arg[0] in puzzleList.keys():
            print('Invaild target!')
            return
        else:
            target = puzzleList[arg[0]].puzzleData
        for i in arg[1:]:
            remove = puzzleData[i.upper()]
            if remove in target:
                puzzleList[arg[0]].puzzleData.remove(remove)


    def do_search(self, arg):
        expressionList = searchMultiplePuzzles(puzzleData, arg, 'found!')


mainMenu = mainmenu()
mainMenu.prompt = '\n\nType in command and argument >>>:'
mainMenu.cmdloop('...')



