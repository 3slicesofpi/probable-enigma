catalog = {0: ["Black beans", 5.98, ""], 1: ["Kidney beans", 4.98, ""], 2: ["Chickpeas", 6.58, ""], 3: ["Chicken noodle soup", 3.58, ""], 4: ["Tomato soup", 3.98, ""], 5: ["Vegetable soup", 4.58, ""], 6: ["Tuna", 2.98, ""], 7: ["Canned salmon", 7.98, ""], 8: ["Canned sardines", 5.58, ""], 9: ["Canned vegetables (corn, peas, carrots)", 5.38, ""], 10: ["Canned peaches", 5.98, ""], 11: ["Canned pears", 5.78, ""], 12: ["Canned pineapple", 6.98, ""], 13: ["Spaghetti", 2.58, ""], 14: ["Penne", 2.38, ""], 15: ["White rice", 4.98, ""], 16: ["Brown rice", 5.58, ""], 17: ["Quinoa", 9.98, ""], 18: ["Oats", 3.98, ""], 19: ["Breakfast cereals", 7.18, ""], 20: ["Granola", 7.58, ""], 21: ["Lentils", 4.78, ""], 22: ["Split peas", 4.38, ""], 23: ["Pasta", 2.98, ""], 24: ["Rice", 4.58, ""], 25: ["Lentils", 4.78, ""], 26: ["Beans", 4.58, ""], 27: ["Crushed tomatoes", 3.78, ""], 28: ["Tomato sauce", 2.98, ""], 29: ["Tomato paste", 2.58, ""], 30: ["Flour", 4.18, ""], 31: ["Sugar", 3.98, ""], 32: ["Baking powder", 3.58, ""], 33: ["Baking soda", 3.38, ""], 34: ["Ketchup", 4.98, ""], 35: ["Mustard", 3.58, ""], 36: ["Mayonnaise", 5.98, ""], 37: ["Olive oil", 8.98, ""], 38: ["Vegetable oil", 5.98, ""], 39: ["Assorted Nuts", 11.98, ""], 40: ["Trail mix", 7.78, ""], 41: ["Crackers", 4.58, ""], 42: ["Popcorn", 3.98, ""], 43: ["Pasta sauce", 4.78, ""], 44: ["Salsa", 5.18, ""], 45: ["BBQ sauce", 5.58, ""], 46: ["Canned chicken", 6.98, ""], 47: ["Spam", 5.98, ""], 48: ["Corned beef", 7.58, ""], 49: ["Raisins", 4.58, ""], 50: ["Apricots", 6.98, ""], 51: ["Cranberries", 5.98, ""], 52: ["Salt", 2.38, ""], 53: ["Pepper", 2.58, ""], 54: ["Oregano", 2.78, ""], 55: ["Cumin", 3.18, ""], 56: ["Instant noodles", 2.18, ""], 57: ["Macaroni and cheese", 3.58, ""], 58: ["Instant soup cups", 4.58, ""], 59: ["Coffee", 9.98, ""], 60: ["Tea", 4.98, ""], 61: ["Fruit juices", 6.58, ""], 62: ["Honey", 7.98, ""], 63: ["Maple syrup", 8.98, ""], 64: ["Sugar", 3.98, ""], 65: ["Alfredo sauce mix", 4.38, ""], 66: ["Pesto pasta mix", 5.18, ""], 67: ["Powdered milk", 6.58, ""], 68: ["Evaporated milk", 3.78, ""], 69: ["Nut bars", 5.98, ""], 70: ["Granola bars", 5.58, ""]}
cart = {}

def exit(): # if this is removed everything breaks
    print('press f again')
    # stupid unpruned trees
    return

def dictFormatter(theDict):
    totalCost = 0
    for iteration in theDict:
        print(str(iteration)+'.',theDict[iteration][2],theDict[iteration][0],'at $'+str(theDict[iteration][1]),'each')
    for here in cart:
        totalCost += cart[here][1]*cart[here][2]
    return totalCost

def menuCatalog(catalog):
    print('Our catalogue of items:')
    dictFormatter(catalog)
    menuSelect()

def menuCart(cart):
    print('your cart contains:')
    totalCost = dictFormatter(cart)
    print('total price of your goods is:',str(totalCost))
    menuSelect()

def menuTakeItem(clientArgs):
    try:
        sortedArgs = [0,0] # c,n
        positions = {'c':0,'n':0}
        for iteration in range(0,len(clientArgs)):
            if clientArgs[iteration] == 'c':
                positions['c'] = iteration
            elif clientArgs[iteration] == 'n':
                positions['n'] = iteration
        print(positions['c'],positions['n'])
        if positions['c']<positions['n']: # !!!!!broken!!!!!
            # theres a better way but it involves lambdas. 
            # And three more temp lists. i Suggest using function.
            sortedArgs[0] = int(clientArgs[(positions["c"]+1):(positions["n"]-1)])
            sortedArgs[1] = int(clientArgs[(positions["n"]+1):])
        elif positions['n']<positions['c']:
            sortedArgs[1] = int(clientArgs[(positions["n"]+1):(positions["c"]-1)])
            sortedArgs[0] = int(clientArgs[(positions["c"]+1):])
         # bug patch to remove duplicates
        for iteration in cart:
            if cart[iteration][0] == catalog[sortedArgs[0]][0]:
                cart[iteration] = [catalog[sortedArgs[0]][0],catalog[sortedArgs[0]][1],(sortedArgs[1]+cart[iteration][2])]
                menuSelect() # deliberate obfuscation
        cart[len(cart)+1] = [catalog[sortedArgs[0]][0],catalog[sortedArgs[0]][1],sortedArgs[1]]
        print(cart)
        menuSelect() # for market3: actually end the function instead of making trees
        
    except:
        print('arguments required:')
        print('ITEMCODE,NUMBEROF,')
        print('example: t,c23,n820 for 820 pastas.')
        menuSelect()

def menuCheckout(cart):
    print('you bought the following:')
    totalCost = dictFormatter(cart)
    print('at a cost of',str(totalCost),'pay up')

def clientInput():
    rawInput = input('>>>: ').replace(' ','')
    firstComma = False
    # example command: take,c23,n820
    # example command: dir
    clientCommand = rawInput
    clientArgs = ''
    for iteration in range(0,len(rawInput)):
        if (rawInput[iteration] == ',') and (firstComma == False):
            firstComma = True
            clientCommand = rawInput[:iteration]
            clientArgs = rawInput[(iteration+1):]
    return [clientCommand,clientArgs]

def menuSelect():
    input = clientInput()
    if input[0][0] == 's': # shoplist, catalogue of items
        menuCatalog(catalog)
    elif input[0][0] == 't': # takeitem
        menuTakeItem(input[1])
    elif input[0][0] == 'p': # peekcart
        menuCart(cart)
    elif input[0][0] == 'c': # checkout, cashier
        menuCheckout(cart)
    elif input[0][0] == 'f': # finalsay/finallye
        exit()
    else:
        print('not a valid command. press help for a list of commands.')
        menuSelect()

menuSelect() # initalization ritual-