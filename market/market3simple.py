catalog = [{"product": "Black beans", "price": 5.98, "quantity": 4600}, {"product": "Kidney beans", "price": 4.98, "quantity": 9000}, {"product": "Chickpeas", "price": 6.58, "quantity": 13400}, {"product": "Chicken noodle soup", "price": 3.58, "quantity": 2400}, {"product": "Tomato soup", "price": 3.98, "quantity": 17800}, {"product": "Vegetable soup", "price": 4.58, "quantity": 6800}, {"product": "Tuna", "price": 2.98, "quantity": 11200}, {"product": "Canned salmon", "price": 7.98, "quantity": 15600}, {"product": "Canned sardines", "price": 5.58, "quantity": 18000}, {"product": "Canned vegetables (corn, peas, carrots)", "price": 5.38, "quantity": 24600}, {"product": "Canned peaches", "price": 5.98, "quantity": 11200}, {"product": "Canned pears", "price": 5.78, "quantity": 15600}, {"product": "Canned pineapple", "price": 6.98, "quantity": 9000}, {"product": "Spaghetti", "price": 2.58, "quantity": 6400}, {"product": "Penne", "price": 2.38, "quantity": 17800}, {"product": "White rice", "price": 4.98, "quantity": 4600}, {"product": "Brown rice", "price": 5.58, "quantity": 11200}, {"product": "Quinoa", "price": 9.98, "quantity": 15600}, {"product": "Oats", "price": 3.98, "quantity": 18000}, {"product": "Breakfast cereals", "price": 7.18, "quantity": 2400}, {"product": "Granola", "price": 7.58, "quantity": 6800}, {"product": "Lentils", "price": 4.78, "quantity": 9000}, {"product": "Split peas", "price": 4.38, "quantity": 13400}, {"product": "Pasta", "price": 2.98, "quantity": 4600}, {"product": "Rice", "price": 4.58, "quantity": 11200}, {"product": "Lentils", "price": 4.78, "quantity": 15600}, {"product": "Beans", "price": 4.58, "quantity": 18000}, {"product": "Crushed tomatoes", "price": 3.78, "quantity": 2400}, {"product": "Tomato sauce", "price": 2.98, "quantity": 9000}, {"product": "Tomato paste", "price": 2.58, "quantity": 13400}, {"product": "Flour", "price": 4.18, "quantity": 17800}, {"product": "Sugar", "price": 3.98, "quantity": 4600}, {"product": "Baking powder", "price": 3.58, "quantity": 11200}, {"product": "Baking soda", "price": 3.38, "quantity": 15600}, {"product": "Ketchup", "price": 4.98, "quantity": 18000}, {"product": "Mustard", "price": 3.58, "quantity": 2400}, {"product": "Mayonnaise", "price": 5.98, "quantity": 9000}, {"product": "Olive oil", "price": 8.98, "quantity": 13400}, {"product": "Vegetable oil", "price": 5.98, "quantity": 17800}, {"product": "Assorted Nuts", "price": 11.98, "quantity": 4600}, {"product": "Trail mix", "price": 7.78, "quantity": 11200}, {"product": "Crackers", "price": 4.58, "quantity": 15600}, {"product": "Popcorn", "price": 3.98, "quantity": 18000}, {"product": "Pasta sauce", "price": 4.78, "quantity": 2400}, {"product": "Salsa", "price": 5.18, "quantity": 9000}, {"product": "BBQ sauce", "price": 5.58, "quantity": 13400}, {"product": "Canned chicken", "price": 6.98, "quantity": 17800}, {"product": "Spam", "price": 5.98, "quantity": 4600}, {"product": "Corned beef", "price": 7.58, "quantity": 11200}]
cart = []


from math import ceil 
def listFormatter(theList): # this does well
    # frontend
    pageSelected = 0
    print("""
the PAGEVIEWER
press any of the following keys to continue:

'b'/'backpage': Go to the previous page.
'n'/'nextpage': Go to the next page.
'e'/'exitmenu': Return to the MAIN MENU

Alternatively, you can use the number keys to navigate through the pages.
""")
    while True:
        if (pageSelected*10+10)<len(theList)+1:
            pageMax = (pageSelected*10)+10
        else:
            pageMax = len(theList)
        for iteration in range(pageSelected*10,pageMax):
            print(str(iteration)+'.',theList[iteration]['quantity'],theList[iteration]['product'],'at $',theList[iteration]['price'],'each')
        print('you are at page:',(pageSelected+1), 'out of', (ceil(len(theList)/10)))
        clientInput = input('input a command >:::')
        try:
            if clientInput[0] == 'e':
                return
            elif clientInput[0] == 'n':
                pageSelected += 1
            elif clientInput[0] == 'b':
                pageSelected -= 1
            else:
                pageSelected = int(clientInput)-1
        except ValueError:
            print('caught error: ValueError: Write a valid command.')
        if (pageSelected < 0) or (pageSelected > ceil(len(theList)/10)-1):
                pageSelected = 0

def menuLookCart():
    listFormatter(cart)
    return
def menuCatalogs():
    listFormatter(catalog)
    return

def menuTakeItem():
    clientArgs = {'code':0,'quantity':0}
    print('please specify which item you want.')
    clientArgs['code'] = int(input('>>>:'))
    print('how many of',catalog[clientArgs['code']]['product'],'do you want?')
    clientArgs['quantity'] = int(input('>>>:'))
    if clientArgs['quantity'] > (catalog[clientArgs['code']]['quantity']):
        print('We do not have enough',catalog[clientArgs['code']]['product']+'.')
        print('We only have',str(catalog[clientArgs['code']]['quantity']),'in our shop.')
    else:
        cart.append(dict(catalog[clientArgs['code']]))
        cart[-1]['quantity'] = clientArgs['quantity']
        print(cart[-1]['quantity'])
        catalog[clientArgs['code']]['quantity'] -= clientArgs['quantity']
        print('You placed',cart[-1]['quantity'],cart[-1]['product'],'in your cart.')
    return

def menuMain(): #return to this after every cycle.
    # print("""
    # welcome to the MAIN MENU
    # To continue, press a command.

    # 'l'/'lookcart': Look into your cart. 
    # 'b'/'browsers': Browse our huge catalog.
    # 'c'/'checkout': Purchase the items in your cart.
    # 't'/'takeitem': Take a product from our catalog.
    # 'r'/'returnit': Return a product from your cart.
    # 'p'/'purgeall': Remove all items from your cart.
    # 'h'/'helpshop': Get help.
    # 'e'/'enditall': Exit the program.
          
    # Happy Shopping!
    # """)
    clientInput = input('Input a command >>>:')
    if clientInput == '':
        print('No command given. Try again')
    elif clientInput[0] == 'l':
        menuLookCart()
        return
    elif clientInput[0] == 'b':
        menuCatalogs()
        return
    elif clientInput[0] == 'c':
        return # unfinished
    elif clientInput[0] == 't':
        menuTakeItem()
    elif clientInput[0] == 'r':
        return
    elif clientInput[0] == 'p':
        cart = []
        print('your cart is now empty.')
        return
    elif (clientInput[0] == 'e') or (clientInput[0] == '&'):
        exit()
    else:
        print('Invalid Command. Try again.')
    return

while True:
    menuMain()