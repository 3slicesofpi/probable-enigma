shopCat = {'1': ['Tomatoes', 57], '2': ['Corn', 53], '3': ['Green Beans', 14], '4': ['Peas', 7], '5': ['Carrots', 61], '6': ['Chickpeas', 9], '7': ['Black Beans', 1], '8': ['Kidney Beans', 17], '9': ['Baked Beans', 81], '10': ['Lentils', 100], '11': ['Tuna', 53], '12': ['Salmon', 78], '13': ['Sardines', 53], '14': ['Chicken', 39]}
clientCat = {}
def clientCatFormatter(clientCat):
    for iteration in clientCat:
        print(str(iteration)+'.',clientCat[iteration][0],'at $'+str(clientCat[iteration][1]))
    return
def clientTakeFormatter(clientInput):
    clientCat[len(clientCat)+1] = shopCat[clientInput[5:]]
    print('you have taken a',shopCat[clientInput[5:]][0])
    if clientInput[(len(clientInput)-1):] == ',':
        clientArgs = input('>: ')
        


def help():
    print('''
instructions:
Hello! type in a command to continue.

commands:
help:   <--- you are here!
    see the full list of commands.
catalog:
    see our huge catalog of 14 items!
take:
    place an item from our catalog and into your cart.
cart:
    view the contents of your cart.
checkout:
    purchase what you have taken.
              ''')
    clientMenuSelect()
    return

def clientMenuSelect():
    try:
        
        clientInput = input('>: ')
        if clientInput[2] == 't': # catalog
            print('we have:') 
            clientCatFormatter(shopCat)
            print('press >:"take", followed by the product number of the thing you want to take.')
            clientMenuSelect()
        elif clientInput[2] == 'k': #take
            clientTakeFormatter()
            clientMenuSelect()
        elif clientInput[2] == 'r': #cart
            print('the things in your cart are:')
            clientCatFormatter(clientCat)
            clientMenuSelect()
        elif clientInput[2] == 'e': #checkout
            clientCatFormatter(clientCat)
            print('your total is:')
            total = 0
            for iteration in clientCat:
                total += clientCat[iteration][1]
            print(total)
                 
    except TypeError:
        print('Invalid input, try again')
        help()
    except KeyError:
        print('Invalid input, try again')
        help()


help()