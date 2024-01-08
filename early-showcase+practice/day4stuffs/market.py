def uc(num):
    print('uc'+str(num))

catalog = {'A1':['beans',5],'A2':['big beans',9],'A3':['coconut',3],'A4':['paper',29],'B1':['chocolate',2]}

clientCat = {}

def clientMenuSelect():
    insert = str(input('> '))
    if insert == 'dir':
        dir()
    elif insert == 'cat':
        cat()
    elif insert == 'cart':
        cart()
    elif insert == 'exit':
        exit()
    elif insert == 'take':
        take()
    elif insert == 'checkout':
        checkout()
    else:
        help()

def catFormatter(theDict):
    theList = list(theDict)
    for iteration in theDict:
        print(theDict[iteration][0]+' at $'+str(theDict[iteration][1]))

def dir():
    uc(1)
    clientMenuSelect()

def cat():
    print(catalog)
    clientMenuSelect()

def take():
    clientCat[len(list(clientCat))+1] = catalog[input('enter the code: > ')]
    clientMenuSelect()

def cart():
    catFormatter(clientCat)
    clientMenuSelect()

def checkout():
    print('your cart:')
    print(clientCat)
    print('total: ')
    total = 0
    for iteration in list(clientCat):
        print(list(clientCat))
        total += clientCat[iteration][1]
    print(int(total))
clientMenuSelect()