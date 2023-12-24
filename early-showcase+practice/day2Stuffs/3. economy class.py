# economy class

class seats():
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def __str__(self):
        return f"{self.name}{self.position}"
    def frontEnd(self):
        if self.position[1] == 1:
            self.position[1] = 'A'
        elif self.position[1] == 2:
            self.position[1] = 'B'
        elif self.position[1] == 3:
            self.position[1] = 'C'
        elif self.position[1] == 4:
            self.position[1] = 'D'
        elif self.position[1] == 5:
            self.position[1] = 'E'
        elif self.position[1] == 6:
            self.position[1] = 'F'

        print("hello, " + str(self.name) + " you sit at row " + str(self.position[0]) + ", seat " + str(self.position[1]))


mySeat = seats('bob',[1,6])
mySeat.frontEnd()
        