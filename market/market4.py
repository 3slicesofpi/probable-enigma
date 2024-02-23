

def cartBecomesEmpty(): # fast and efficient, unlike menuMoveItem(lF,lT,None,None)
    for here in range(0,len(cart)):
        catalog[here]['quantity'] = cart[here]['quantity']
        cart[here]['quantity'] = 0
    return

def menuMoveItem(listFrom, listTo, clientArgCode, clientArgQuantity): # is improvable
    # clientArgCode and clientArgQuantity set to None if no args given.
    # moving client args to clientArgs dict.
    clientArgs = {'code':0 ,'quantity':0}
    if clientArgCode != None:
        clientArgs['code'] = int(clientArgCode)
    else:
        clientArgs['code'] = int(input('Type the code of the item you want to transfer >>>:'))-1
    # we're using the dict, not the entire list.
    dictFrom = listFrom[clientArgs['code']] # listFrom, listTo still exists in mem btw!
    dictTo = listTo[clientArgs['code']] # this is bad, but is the best we can do
    if clientArgQuantity != None:
        clientArgs['quantity'] = int(clientArgQuantity)
    else:
        print('There are',dictFrom['quantity'],dictFrom['name'])
        print('Type the number of',dictFrom['name'],'you want to transfer.')
        clientArgs['quantity'] = int(input('>>>:'))
    if clientArgs['quantity'] > (dictFrom['quantity']):
        print('We do not have enough',dictFrom['product']+'.')
        print('We only have',str(dictFrom['quantity']),'in our shop.')
    else:
        dictFrom['quantity'] -= clientArgs['quantity']
        dictTo['quantity'] += clientArgs['quantity'] 
        print('Transfer successful. Returning you to MAIN MENU .')
    return (dictFrom, dictTo)


from math import ceil
def menuListFormatter(listRaw,listName):
    # remove quan = 0 elements
    newList = [None]
    for here in listRaw:
        if here['quantity'] != 0:
            newList.append(here)
    # when nothing in cart/catalog
    if len(newList) <= 1:
        newList[0] = {'name': 'There is nothing here... Press "e" to return or "h" for help.','category':'Empty:'}
    else:
        newList.remove(None)
    
    # pageviewer
    pageviewMode = 0
    pageSelected = 0
    while True:
        pageList = [] # contains things shown to client. emptied after use.
        if pageSelected < 0:
            pageSelected = ceil(len(newList)/10)-1
        elif pageSelected > ceil(len(newList)/10)-1:
            pageSelected = 0
        
        if pageviewMode == 0:
            maxPage = (pageSelected*10)+10
            if maxPage > len(newList):
                maxPage = len(newList)
            else:
                pass
            for here in range(pageSelected*10,maxPage):
                pageList.append(newList[here])
            print('You are currently on page',(pageSelected+1),'of',(ceil(len(newList)/10)))
        elif pageviewMode == 1:
            if pageSelected < 0:
                pageSelected = len(categoryList)-1
                print(pageSelected) # FIXME (minor pronlem)
                # small problem with page not returning to max properly.
            elif pageSelected > len(categoryList)-1:
                pageSelected = 0

            for elements in newList: # temporary fix
                if elements['category'] == categoryList[pageSelected]:
                    pageList.append(elements)
            print('You are now viewing the category',categoryList[pageSelected])
        

        # now the client can touch the data
        print(pageList)
        for items in pageList:
            print(str(items['position'])+':',items['quantity'],items['name']+'(s) at',items['price'],'each')
        clientInput = input('Press a command to continue or press "h" for help. >>>:')
        if clientInput[0] == 'h':
            menuHelp('menuListFormatter')
        elif clientInput[0] == 'v':
            menuNav(str('menuListFormatter, viewing',listName))
        elif clientInput[0] == 'e':
            return
        elif clientInput[0] == 'b':
            pageSelected -= 1
        elif clientInput[0] == 'n':
            pageSelected += 1
        elif clientInput[0] == 'm':
            pageviewMode += 1
            pageSelected = 0
        else:
            try:
                pageSelected = int(clientInput)-1
            except ValueError:
                print('Invalid Input! Returning you to the MAIN MENU')
                return
            except:
                print('An error has occurred. Returning you to the MAIN MENU .')
                return
        if pageviewMode > 1: 
            pageviewMode = 0

def menuCheckOut():
    numofItems = 0
    totalPrice = 0
    for here in cart:
        if here['quantity'] != 0:
            print(here['quantity'],here['name'],'at',(here['quantity']*here['price']))
            numofItems += here['quantity']
            totalPrice += (here['price']*here['quantity'])
    print('')
    print('There are',numofItems,'in your cart with a combined value of',totalPrice)
    totalPrice = float(totalPrice*(9/100))
    print('After 9% Tax, you will pay',str(totalPrice))
    if input('Proceed with payment?')[0] == 'y':
        print('Thank you for shopping with us!')
        exit()
    else:
        print('checkout process cancelled, returning to MAIN MENU .')
        return

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
's'/'searchit': Find the code for a product.
'h'/'helpshop': Get help.
'e'/'enditall': Exit the program.
          
Tip : use 'v' to know where you are at all times! 
    Available only in menus.
              
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
'e'/'exitmenu': Return to the MAIN MENU .
'm'/'modemenu': Change the pageviewer mode.

Alternatively, you can use the number keys to navigate through the pages.
              
Each item has a 'code' that you must type in takeitem/returnit to transfer items.
''')
    return


import re
def menuMain(): #return to this after every cycle.
    
    # input area
    clientRaw = input('Press a command to continue or press "h" for help. >>>:')
    clientInput = re.split(',',clientRaw)
    if len(clientInput) == 1:
        clientInput.append(None)
        clientInput.append(None)
    elif len(clientInput) == 2:
        clientInput.append(None)
    else:
        pass
    if clientInput == '':
        print('No command given. Try again')
    elif clientInput[0][0] == 'l':
        menuListFormatter(cart,'Cart')
        return
    elif clientInput[0][0] == 'b':
        menuListFormatter(catalog,'Catalog')
        return
    elif clientInput[0][0] == 'c':
        menuCheckOut()
        return
    elif clientInput[0][0] == 't':
        menuMoveItem(catalog,cart,clientInput[1],clientInput[2])
        return
    elif clientInput[0][0] == 'r':
        menuMoveItem(cart,catalog,clientInput[1],clientInput[2])
        return
    elif clientInput[0][0] == 'p': 
        cartBecomesEmpty()
        return
    elif clientInput[0][0] == 'h':
        menuHelp('menuMain')
        return
    elif clientInput[0][0] == 'v':
        menuNav('menuMain')
        return
    elif clientInput[0][0] == 's':
        menuSearchCode()
    elif (clientInput[0][0] == 'e') or (clientInput[0][0] == '&'):
        exit()
    else:
        print('Invalid Command. Try again or press "h" for help.')
        return
# TODO list
    # search by name (searchit) look for products and catagory
    # make advanced(tm) number taker
    # dealz und salez (admin?, rng?, prebuilt?)



# general working area
catalog = [
    {'name': 'Tomato soup', 'price': 2.49, 'quantity': 700, 'category': 'Canned Good', 'position': 1}, {'name': 'Vegetable soup', 'price': 2.79, 'quantity': 600, 'category': 'Canned Good', 'position': 2}, {'name': 'Tuna', 'price': 1.99, 'quantity': 900, 'category': 'Canned Good', 'position': 3}, {'name': 'Canned salmon', 'price': 4.99, 'quantity': 300, 'category': 'Canned Good', 'position': 4}, {'name': 'Canned sardines', 'price': 3.29, 'quantity': 400, 'category': 'Canned Good', 'position': 5}, {'name': 'Canned vegetables', 'price': 1.89, 'quantity': 800, 'category': 'Canned Good', 'position': 6}, {'name': 'Canned peach', 'price': 2.39, 'quantity': 700, 'category': 'Canned Good', 'position': 7}, {'name': 'Canned pear', 'price': 2.19, 'quantity': 600, 'category': 'Canned Good', 'position': 8}, {'name': 'Canned pineapple', 'price': 2.99, 'quantity': 500, 'category': 'Canned Good', 'position': 9}, {'name': 'Canned corn', 'price': 1.59, 'quantity': 800, 'category': 'Canned Good', 'position': 10}, {'name': 'Canned green bean', 'price': 1.79, 'quantity': 700, 'category': 'Canned Good', 'position': 11}, {'name': 'Spaghetti', 'price': 1.99, 'quantity': 1000, 'category': 'Pasta and Grain', 'position': 12}, {'name': 'Penne', 'price': 1.79, 'quantity': 1100, 'category': 'Pasta and Grain', 'position': 13}, {'name': 'White rice', 'price': 2.49, 'quantity': 900, 'category': 'Pasta and Grain', 'position': 14}, {'name': 'Brown rice', 'price': 2.69, 'quantity': 800, 'category': 'Pasta and Grain', 'position': 15}, {'name': 'Quinoa', 'price': 4.99, 'quantity': 500, 'category': 'Pasta and Grain', 'position': 16}, {'name': 'Oats', 'price': 1.89, 'quantity': 1200, 'category': 'Pasta and Grain', 'position': 17}, {'name': 'Lentil', 'price': 1.29, 'quantity': 1300, 'category': 'Pasta and Grain', 'position': 18}, {'name': 'Split pea', 'price': 1.39, 'quantity': 1400, 'category': 'Pasta and Grain', 'position': 19}, {'name': 'Pasta', 'price': 1.59, 'quantity': 1100, 'category': 'Pasta and Grain', 'position': 20}, {'name': 'Rice', 'price': 1.49, 'quantity': 1200, 'category': 'Pasta and Grain', 'position': 21}, {'name': 'Beans', 'price': 1.29, 'quantity': 1300, 'category': 'Pasta and Grain', 'position': 22}, {'name': 'Barley', 'price': 2.19, 'quantity': 1000, 'category': 'Pasta and Grain', 'position': 23}, {'name': 'Couscous', 'price': 2.29, 'quantity': 900, 'category': 'Pasta and Grain', 'position': 24}, {'name': 'Farro', 'price': 3.49, 'quantity': 600, 'category': 'Pasta and Grain', 'position': 25}, {'name': 'Orzo', 'price': 2.09, 'quantity': 1100, 'category': 'Pasta and Grain', 'position': 26}, {'name': 'Flour', 'price': 3.49, 'quantity': 700, 'category': 'Baking Essential', 'position': 27}, {'name': 'Sugar', 'price': 2.99, 'quantity': 800, 'category': 'Baking Essential', 'position': 28}, {'name': 'Baking powder', 'price': 1.79, 'quantity': 900, 'category': 'Baking Essential', 'position': 29}, {'name': 'Baking soda', 'price': 1.69, 'quantity': 1000, 'category': 'Baking Essential', 'position': 30}, {'name': 'Cornstarch', 'price': 2.29, 'quantity': 800, 'category': 'Baking Essential', 'position': 31}, {'name': 'Cake mix', 'price': 2.99, 'quantity': 700, 'category': 'Baking Essential', 'position': 32}, {'name': 'Cocoa powder', 'price': 3.79, 'quantity': 600, 'category': 'Baking Essential', 'position': 33}, {'name': 'Vanilla extract', 'price': 4.99, 'quantity': 500, 'category': 'Baking Essential', 'position': 34}, {'name': 'Breakfast cereal', 'price': 3.49, 'quantity': 700, 'category': 'Breakfast Item', 'position': 35}, {'name': 'Granola', 'price': 4.29, 'quantity': 600, 'category': 'Breakfast Item', 'position': 36}, {'name': 'Instant noodles', 'price': 1.99, 'quantity': 1000, 'category': 'Breakfast Item', 'position': 37}, {'name': 'Macaroni and cheese', 'price': 2.79, 'quantity': 900, 'category': 'Breakfast Item', 'position': 38}, {'name': 'Instant soup cup', 'price': 2.39, 'quantity': 1100, 'category': 'Breakfast Item', 'position': 39}, {'name': 'Pancake mix', 'price': 3.29, 'quantity': 800, 'category': 'Breakfast Item', 'position': 40}, {'name': 'Muffin mix', 'price': 2.99, 'quantity': 700, 'category': 'Breakfast Item', 'position': 41}, {'name': 'Instant oatmeal', 'price': 2.19, 'quantity': 1200, 'category': 'Breakfast Item', 'position': 42}, {'name': 'Assorted Nut', 'price': 5.49, 'quantity': 500, 'category': 'Snack', 'position': 43}, {'name': 'Trail mix', 'price': 4.99, 'quantity': 600, 'category': 'Snack', 'position': 44}, {'name': 'Cracker', 'price': 2.49, 'quantity': 800, 'category': 'Snack', 'position': 45}, {'name': 'Popcorn', 'price': 3.29, 'quantity': 700, 'category': 'Snack', 'position': 46}, {'name': 'Nut bar', 'price': 1.99, 'quantity': 1000, 'category': 'Snack', 'position': 47}, {'name': 'Granola bar', 'price': 2.29, 'quantity': 900, 'category': 'Snack', 'position': 48}, {'name': 'Pretzel', 'price': 1.79, 'quantity': 1100, 'category': 'Snack', 'position': 49}, {'name': 'Rice cake', 'price': 1.49, 'quantity': 1200, 'category': 'Snack', 'position': 50}, {'name': 'Mustard', 'price': 1.99, 'quantity': 700, 'category': 'Condiment', 'position': 51}, {'name': 'Mayonnaise', 'price': 3.49, 'quantity': 800, 'category': 'Condiment', 'position': 52}, {'name': 'BBQ sauce', 'price': 2.79, 'quantity': 900, 'category': 'Condiment', 'position': 53}, {'name': 'Soy sauce', 'price': 2.29, 'quantity': 1000, 'category': 'Condiment', 'position': 54}, {'name': 'Worcestershire sauce', 'price': 2.99, 'quantity': 800, 'category': 'Condiment', 'position': 55}, {'name': 'Hot sauce', 'price': 1.99, 'quantity': 700, 'category': 'Condiment', 'position': 56}, {'name': 'Teriyaki sauce', 'price': 3.29, 'quantity': 600, 'category': 'Condiment', 'position': 57}, {'name': 'Fish sauce', 'price': 2.49, 'quantity': 500, 'category': 'Condiment', 'position': 58}, {'name': 'Olive oil', 'price': 6.99, 'quantity': 700, 'category': 'Cooking Oil and Sauce', 'position': 59}, {'name': 'Vegetable oil', 'price': 4.49, 'quantity': 800, 'category': 'Cooking Oil and Sauce', 'position': 60}, {'name': 'Pasta sauce', 'price': 3.29, 'quantity': 900, 'category': 'Cooking Oil and Sauce', 'position': 61}, {'name': 'Soybean oil', 'price': 5.49, 'quantity': 1000, 'category': 'Cooking Oil and Sauce', 'position': 62}, {'name': 'Canola oil', 'price': 4.99, 'quantity': 800, 'category': 'Cooking Oil and Sauce', 'position': 63}, {'name': 'Sesame oil', 'price': 7.99, 'quantity': 700, 'category': 'Cooking Oil and Sauce', 'position': 64}, {'name': 'Alfredo sauce', 'price': 3.79, 'quantity': 600, 'category': 'Cooking Oil and Sauce', 'position': 65}, {'name': 'Marinara sauce', 'price': 3.49, 'quantity': 500, 'category': 'Cooking Oil and Sauce', 'position': 66}, {'name': 'Salt', 'price': 1.29, 'quantity': 1000, 'category': 'Spice and Seasoning', 'position': 67}, {'name': 'Pepper', 'price': 2.49, 'quantity': 1100, 'category': 'Spice and Seasoning', 'position': 68}, {'name': 'Oregano', 'price': 1.79, 'quantity': 900, 'category': 'Spice and Seasoning', 'position': 69}, {'name': 'Cumin', 'price': 2.99, 'quantity': 800, 'category': 'Spice and Seasoning', 'position': 70}, {'name': 'Paprika', 'price': 1.99, 'quantity': 1200, 'category': 'Spice and Seasoning', 'position': 71}, {'name': 'Chili powder', 'price': 2.29, 'quantity': 1300, 'category': 'Spice and Seasoning', 'position': 72}, {'name': 'Cinnamon', 'price': 1.59, 'quantity': 1400, 'category': 'Spice and Seasoning', 'position': 73}, {'name': 'Garlic powder', 'price': 2.79, 'quantity': 1500, 'category': 'Spice and Seasoning', 'position': 74}, {'name': 'Coffee', 'price': 6.99, 'quantity': 800, 'category': 'Beverage', 'position': 75}, {'name': 'Tea', 'price': 4.99, 'quantity': 900, 'category': 'Beverage', 'position': 76}, {'name': 'Fruit juice', 'price': 3.49, 'quantity': 1000, 'category': 'Beverage', 'position': 77}, {'name': 'Powdered milk', 'price': 5.99, 'quantity': 1100, 'category': 'Beverage', 'position': 78}, {'name': 'Evaporated milk', 'price': 2.49, 'quantity': 900, 'category': 'Beverage', 'position': 79}, {'name': 'Hot chocolate mix', 'price': 4.29, 'quantity': 800, 'category': 'Beverage', 'position': 80}, {'name': 'Lemonade mix', 'price': 3.79, 'quantity': 700, 'category': 'Beverage', 'position': 81}, {'name': 'Energy drink', 'price': 2.99, 'quantity': 600, 'category': 'Beverage', 'position': 82}, {'name': 'Honey', 'price': 7.99, 'quantity': 700, 'category': 'Sweetener', 'position': 83}, {'name': 'Maple syrup', 'price': 9.99, 'quantity': 600, 'category': 'Sweetener', 'position': 84}, {'name': 'Sugar', 'price': 2.99, 'quantity': 800, 'category': 'Sweetener', 'position': 85}, {'name': 'Agave syrup', 'price': 8.99, 'quantity': 700, 'category': 'Sweetener', 'position': 86}, {'name': 'Stevia', 'price': 6.99, 'quantity': 1000, 'category': 'Sweetener', 'position': 87}, {'name': 'Artificial sweetener', 'price': 4.99, 'quantity': 1100, 'category': 'Sweetener', 'position': 88}, {'name': 'Molasses', 'price': 5.49, 'quantity': 1200, 'category': 'Sweetener', 'position': 89}, {'name': 'Brown sugar', 'price': 3.49, 'quantity': 1300, 'category': 'Sweetener', 'position': 90}, {'name': 'Taco seasoning mix', 'price': 1.49, 'quantity': 800, 'category': 'Sauce Mix', 'position': 91}, {'name': 'Chili seasoning mix', 'price': 1.79, 'quantity': 900, 'category': 'Sauce Mix', 'position': 92}, {'name': 'Fajita seasoning mix', 'price': 1.99, 'quantity': 1000, 'category': 'Sauce Mix', 'position': 93}, {'name': 'Curry seasoning mix', 'price': 2.29, 'quantity': 1100, 'category': 'Sauce Mix', 'position': 94}, {'name': 'Gravy mix', 'price': 1.29, 'quantity': 1200, 'category': 'Sauce Mix', 'position': 95}, {'name': 'Ranch dressing mix', 'price': 2.49, 'quantity': 1300, 'category': 'Sauce Mix', 'position': 96}, {'name': 'Sloppy Joe seasoning mix', 'price': 1.69, 'quantity': 1400, 'category': 'Sauce Mix', 'position': 97}, {'name': 'Stir-fry sauce mix', 'price': 2.79, 'quantity': 1500, 'category': 'Sauce Mix', 'position': 98},{'name': 'Salt', 'price': 1.29, 'quantity': 2000, 'category': 'Spice and Seasoning', 'position': 99}, {'name': 'Pepper', 'price': 2.49, 'quantity': 2000, 'category': 'Spice and Seasoning', 'position': 100}, {'name': 'Oregano', 'price': 1.79, 'quantity': 350, 'category': 'Spice and Seasoning', 'position': 101}, {'name': 'Cumin', 'price': 2.99, 'quantity': 350, 'category': 'Spice and Seasoning', 'position': 102}, {'name': 'Paprika', 'price': 1.99, 'quantity': 100, 'category': 'Spice and Seasoning', 'position': 103}, {'name': 'Chili powder', 'price': 2.29, 'quantity': 1050, 'category': 'Spice and Seasoning', 'position': 104}, {'name': 'Cinnamon', 'price': 1.59, 'quantity': 110, 'category': 'Spice and Seasoning', 'position': 105}, {'name': 'Garlic powder', 'price': 2.79, 'quantity': 120, 'category': 'Spice and Seasoning', 'position': 106}]

cart =[
    {'name': 'Tomato soup', 'price': 2.49, 'quantity': 0, 'category': 'Canned Good', 'position': 1}, {'name': 'Vegetable soup', 'price': 2.79, 'quantity': 0, 'category': 'Canned Good', 'position': 2}, {'name': 'Tuna', 'price': 1.99, 'quantity': 0, 'category': 'Canned Good', 'position': 3}, {'name': 'Canned salmon', 'price': 4.99, 'quantity': 0, 'category': 'Canned Good', 'position': 4}, {'name': 'Canned sardines', 'price': 3.29, 'quantity': 0, 'category': 'Canned Good', 'position': 5}, {'name': 'Canned vegetables', 'price': 1.89, 'quantity': 0, 'category': 'Canned Good', 'position': 6}, {'name': 'Canned peach', 'price': 2.39, 'quantity': 0, 'category': 'Canned Good', 'position': 7}, {'name': 'Canned pear', 'price': 2.19, 'quantity': 0, 'category': 'Canned Good', 'position': 8}, {'name': 'Canned pineapple', 'price': 2.99, 'quantity': 0, 'category': 'Canned Good', 'position': 9}, {'name': 'Canned corn', 'price': 1.59, 'quantity': 0, 'category': 'Canned Good', 'position': 10}, {'name': 'Canned green bean', 'price': 1.79, 'quantity': 0, 'category': 'Canned Good', 'position': 11}, {'name': 'Spaghetti', 'price': 1.99, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 12}, {'name': 'Penne', 'price': 1.79, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 13}, {'name': 'White rice', 'price': 2.49, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 14}, {'name': 'Brown rice', 'price': 2.69, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 15}, {'name': 'Quinoa', 'price': 4.99, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 16}, {'name': 'Oats', 'price': 1.89, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 17}, {'name': 'Lentil', 'price': 1.29, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 18}, {'name': 'Split pea', 'price': 1.39, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 19}, {'name': 'Pasta', 'price': 1.59, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 20}, {'name': 'Rice', 'price': 1.49, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 21}, {'name': 'Beans', 'price': 1.29, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 22}, {'name': 'Barley', 'price': 2.19, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 23}, {'name': 'Couscous', 'price': 2.29, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 24}, {'name': 'Farro', 'price': 3.49, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 25}, {'name': 'Orzo', 'price': 2.09, 'quantity': 0, 'category': 'Pasta and Grain', 'position': 26}, {'name': 'Flour', 'price': 3.49, 'quantity': 0, 'category': 'Baking Essential', 'position': 27}, {'name': 'Sugar', 'price': 2.99, 'quantity': 0, 'category': 'Baking Essential', 'position': 28}, {'name': 'Baking powder', 'price': 1.79, 'quantity': 0, 'category': 'Baking Essential', 'position': 29}, {'name': 'Baking soda', 'price': 1.69, 'quantity': 0, 'category': 'Baking Essential', 'position': 30}, {'name': 'Cornstarch', 'price': 2.29, 'quantity': 0, 'category': 'Baking Essential', 'position': 31}, {'name': 'Cake mix', 'price': 2.99, 'quantity': 0, 'category': 'Baking Essential', 'position': 32}, {'name': 'Cocoa powder', 'price': 3.79, 'quantity': 0, 'category': 'Baking Essential', 'position': 33}, {'name': 'Vanilla extract', 'price': 4.99, 'quantity': 0, 'category': 'Baking Essential', 'position': 34}, {'name': 'Breakfast cereal', 'price': 3.49, 'quantity': 0, 'category': 'Breakfast Item', 'position': 35}, {'name': 'Granola', 'price': 4.29, 'quantity': 0, 'category': 'Breakfast Item', 'position': 36}, {'name': 'Instant noodles', 'price': 1.99, 'quantity': 0, 'category': 'Breakfast Item', 'position': 37}, {'name': 'Macaroni and cheese', 'price': 2.79, 'quantity': 0, 'category': 'Breakfast Item', 'position': 38}, {'name': 'Instant soup cup', 'price': 2.39, 'quantity': 0, 'category': 'Breakfast Item', 'position': 39}, {'name': 'Pancake mix', 'price': 3.29, 'quantity': 0, 'category': 'Breakfast Item', 'position': 40}, {'name': 'Muffin mix', 'price': 2.99, 'quantity': 0, 'category': 'Breakfast Item', 'position': 41}, {'name': 'Instant oatmeal', 'price': 2.19, 'quantity': 0, 'category': 'Breakfast Item', 'position': 42}, {'name': 'Assorted Nut', 'price': 5.49, 'quantity': 0, 'category': 'Snack', 'position': 43}, {'name': 'Trail mix', 'price': 4.99, 'quantity': 0, 'category': 'Snack', 'position': 44}, {'name': 'Cracker', 'price': 2.49, 'quantity': 0, 'category': 'Snack', 'position': 45}, {'name': 'Popcorn', 'price': 3.29, 'quantity': 0, 'category': 'Snack', 'position': 46}, {'name': 'Nut bar', 'price': 1.99, 'quantity': 0, 'category': 'Snack', 'position': 47}, {'name': 'Granola bar', 'price': 2.29, 'quantity': 0, 'category': 'Snack', 'position': 48}, {'name': 'Pretzel', 'price': 1.79, 'quantity': 0, 'category': 'Snack', 'position': 49}, {'name': 'Rice cake', 'price': 1.49, 'quantity': 0, 'category': 'Snack', 'position': 50}, {'name': 'Mustard', 'price': 1.99, 'quantity': 0, 'category': 'Condiment', 'position': 51}, {'name': 'Mayonnaise', 'price': 3.49, 'quantity': 0, 'category': 'Condiment', 'position': 52}, {'name': 'BBQ sauce', 'price': 2.79, 'quantity': 0, 'category': 'Condiment', 'position': 53}, {'name': 'Soy sauce', 'price': 2.29, 'quantity': 0, 'category': 'Condiment', 'position': 54}, {'name': 'Worcestershire sauce', 'price': 2.99, 'quantity': 0, 'category': 'Condiment', 'position': 55}, {'name': 'Hot sauce', 'price': 1.99, 'quantity': 0, 'category': 'Condiment', 'position': 56}, {'name': 'Teriyaki sauce', 'price': 3.29, 'quantity': 0, 'category': 'Condiment', 'position': 57}, {'name': 'Fish sauce', 'price': 2.49, 'quantity': 0, 'category': 'Condiment', 'position': 58}, {'name': 'Olive oil', 'price': 6.99, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 59}, {'name': 'Vegetable oil', 'price': 4.49, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 60}, {'name': 'Pasta sauce', 'price': 3.29, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 61}, {'name': 'Soybean oil', 'price': 5.49, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 62}, {'name': 'Canola oil', 'price': 4.99, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 63}, {'name': 'Sesame oil', 'price': 7.99, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 64}, {'name': 'Alfredo sauce', 'price': 3.79, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 65}, {'name': 'Marinara sauce', 'price': 3.49, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 66}, {'name': 'Salt', 'price': 1.29, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 67}, {'name': 'Pepper', 'price': 2.49, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 68}, {'name': 'Oregano', 'price': 1.79, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 69}, {'name': 'Cumin', 'price': 2.99, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 70}, {'name': 'Paprika', 'price': 1.99, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 71}, {'name': 'Chili powder', 'price': 2.29, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 72}, {'name': 'Cinnamon', 'price': 1.59, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 73}, {'name': 'Garlic powder', 'price': 2.79, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 74}, {'name': 'Coffee', 'price': 6.99, 'quantity': 0, 'category': 'Beverage', 'position': 75}, {'name': 'Tea', 'price': 4.99, 'quantity': 0, 'category': 'Beverage', 'position': 76}, {'name': 'Fruit juice', 'price': 3.49, 'quantity': 0, 'category': 'Beverage', 'position': 77}, {'name': 'Powdered milk', 'price': 5.99, 'quantity': 0, 'category': 'Beverage', 'position': 78}, {'name': 'Evaporated milk', 'price': 2.49, 'quantity': 0, 'category': 'Beverage', 'position': 79}, {'name': 'Hot chocolate mix', 'price': 4.29, 'quantity': 0, 'category': 'Beverage', 'position': 80}, {'name': 'Lemonade mix', 'price': 3.79, 'quantity': 0, 'category': 'Beverage', 'position': 81}, {'name': 'Energy drink', 'price': 2.99, 'quantity': 0, 'category': 'Beverage', 'position': 82}, {'name': 'Mustard', 'price': 1.99, 'quantity': 0, 'category': 'Condiment', 'position': 83}, {'name': 'Mayonnaise', 'price': 3.49, 'quantity': 0, 'category': 'Condiment', 'position': 84}, {'name': 'BBQ sauce', 'price': 2.79, 'quantity': 0, 'category': 'Condiment', 'position': 85}, {'name': 'Soy sauce', 'price': 2.29, 'quantity': 0, 'category': 'Condiment', 'position': 86}, {'name': 'Worcestershire sauce', 'price': 2.99, 'quantity': 0, 'category': 'Condiment', 'position': 87}, {'name': 'Hot sauce', 'price': 1.99, 'quantity': 0, 'category': 'Condiment', 'position': 88}, {'name': 'Teriyaki sauce', 'price': 3.29, 'quantity': 0, 'category': 'Condiment', 'position': 89}, {'name': 'Fish sauce', 'price': 2.49, 'quantity': 0, 'category': 'Condiment', 'position': 90}, {'name': 'Olive oil', 'price': 6.99, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 91}, {'name': 'Vegetable oil', 'price': 4.49, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 92}, {'name': 'Pasta sauce', 'price': 3.29, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 93}, {'name': 'Soybean oil', 'price': 5.49, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 94}, {'name': 'Canola oil', 'price': 4.99, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 95}, {'name': 'Sesame oil', 'price': 7.99, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 96}, {'name': 'Alfredo sauce', 'price': 3.79, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 97}, {'name': 'Marinara sauce', 'price': 3.49, 'quantity': 0, 'category': 'Cooking Oil and Sauce', 'position': 98}, {'name': 'Salt', 'price': 1.29, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 99}, {'name': 'Pepper', 'price': 2.49, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 100}, {'name': 'Oregano', 'price': 1.79, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 101}, {'name': 'Cumin', 'price': 2.99, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 102}, {'name': 'Paprika', 'price': 1.99, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 103}, {'name': 'Chili powder', 'price': 2.29, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 104}, {'name': 'Cinnamon', 'price': 1.59, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 105}, {'name': 'Garlic powder', 'price': 2.79, 'quantity': 0, 'category': 'Spice and Seasoning', 'position': 106}]

categoryList = ('Canned Good','Pasta and Grain','Baking Essential','Breakfast Item','Snack','Condiment','Cooking Oil and Sauce','Spice and Seasoning')
# loop. Stops on exit().
while True:
    menuMain()