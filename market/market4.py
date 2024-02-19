def menuNav(clientMenuPos): # simple position teller
    print('You are currently at:',clientMenuPos)
    return

def menuHelp(clientMenuPos):
# the cringe is nescessary to dissaude users from coming here.
    if clientMenuPos == 'menuMain':
        print('''
welcum to le moste gloriouse SHOPEZ of all tim
it has all the thingz you'll eva need
for you're.

Basic Commands:
     
'l'/'lookcart': Look into your cart. 
'b'/'browsers': Browse our huge catalog.
'c'/'checkout': Purchase the items in your cart.
't'/'takeitem': Take a product from our catalog.
'r'/'returnit': Return a product from your cart.
'p'/'purgeall': Remove all items from your cart.
'h'/'helpshop': Get help.
'e'/'enditall': Exit the program.
          
Happy Shopping!
''')
    elif clientMenuPos == 'menuListFormatter':
        print('''
welcum to le moste gloriouse PAGEVIEWER of all tim
it has advanced(tm) page system for advanced(tm) vieweing XPerience
for yor'ue
              
Pageviewer commands:

'b'/'backpage': Go to the previous page.
'n'/'nextpage': Go to the next page.
'e'/'exitmenu': Return to the MAIN MENU

Alternatively, you can use the number keys to navigate through the pages.
''')



def menuMain(): #return to this after every cycle.
    

    # input area
    clientInput = input('Press a command to continue or press "h" for help. >>>:')
    if clientInput == '':
        print('No command given. Try again')
    elif clientInput[0] == 'l':
        menuLookCart()
        return
    elif clientInput[0] == 'b':
        menuCatalogs()
        return
    elif clientInput[0] == 'c':
        menuCheckOut()
        return
    elif clientInput[0] == 't':
        menuTakeItem()
        return
    elif clientInput[0] == 'r':
        menuReturnItem() # the reverse of menuTakeItem(), mergetim TODD
        return
    elif clientInput[0] == 'p': 
        cartBecomesEmpty()
        return
    elif clientInput[0] == 'h':
        menuHelp('menuMain')
        return
    elif clientInput[0] == 'n':
        menuNav('menuMain')
        return
    elif (clientInput[0] == 'e') or (clientInput[0] == '&'):
        exit()
    else:
        print('Invalid Command. Try again or press "h" for help.')
        return
# TODD list
    # fill up the cart and catalog. cart is empty.
    # make all the menus again
    # populate menuHelp
    # make menuReturnItem and menuTakeItem merged
    # make advanced(tm) number taker
    # dealz und salez (admin?, rng?, prebuilt?)



# general working area
cart = []
catalog = []

# loop. Breaks on exit() for some reason
while True:
    menuMain()