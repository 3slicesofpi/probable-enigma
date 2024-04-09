
class colours(): # with a u
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    black = (0, 0, 0) 
    red = (255, 0, 0)
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
            case 'beige':
                self.beige = (223, 207, 190)
            case 'orange':
                self.orange = (225, 93, 68)
            case 'purple':
                self.purple = (91, 94, 166)
            case 'pink':
                self.pink = (247, 202, 201)
            case 'forest':
                self.forest = (2, 50, 32)
            case 'sky': # light blue
                self.sky = (146, 168, 209)
            case 'marsala': # red
                self.marsala = (149, 82, 81)
            case 'burgundy': # red
                self.burgundy = (128, 0, 32)
            case 'orchid': # pink
                self.orchid = (181, 101, 167)
            case 'turqoise': # light blue
                self.turqoise = (68, 184, 172)
            case 'lime': # green
                self.lime = (136, 176, 75)


magenta = colours()
magenta.newColour('magenta',(20,70,0))
print(magenta.custom['magenta'])