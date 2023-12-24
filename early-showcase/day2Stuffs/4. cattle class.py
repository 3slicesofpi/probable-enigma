# cattle class


# def allTheNumbers(len):
#     resultantList = [0]
#     for x in range(1,len+1):
#         resultantList.append(x)
        
#     return resultantList

# print(allTheNumbers(16))

class foolsBar():
    def __init__(self,raw):
        self.raw = raw
    def __str__(self) -> str:
        pass
    def Too(self):
        if self.raw % 2 == 0:
            return 'Too'
        else:
            return ''
    def Foo(self):
        if self.raw % 3 == 0:
            return 'Foo'
        else:
            return ''
    def Qua(self):
        if self.raw % 4 == 0:
            return 'Qua'
        else:
            return ''
    def Bar(self):
        if self.raw % 5 == 0:
            return 'Bar'
        else:
            return ''

len = 16
for x in range(1,len+1):
    test = foolsBar(x)
    print(str(x) + test.Too() + test.Foo() + test.Qua() + test.Bar())