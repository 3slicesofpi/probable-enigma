def menuListFormatter(listRaw,listName):
    # remove quan = 0
    newList = [None]
    for here in listRaw:
        if here['quantity'] == 0: #FIX!!!!!
            pass
        else:
            newList.append(here)   
    # when nothing in cart/catalog
    if len(newList) <= 1:
        newList[0] = {'name': 'There is nothing here... Press "e" to return or "h" for help.','category':'Empty:'}
    else:
        pass

    print(newList)

    \

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
        menuListFormatter(cart,'Cart')
        return
    elif clientInput[0] == 'b':
        menuListFormatter(catalog,'Catalog')
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
    # make all the menus again
    # populate menuHelp
    # make menuReturnItem and menuTakeItem merged
    # make advanced(tm) number taker
    # dealz und salez (admin?, rng?, prebuilt?)



# general working area
catalog = [
    {"name": "Chicken noodle soup", "price": 3.99, "quantity": 500, "category": "Canned Good"},
    {"name": "Tomato soup", "price": 2.49, "quantity": 700, "category": "Canned Good"},
    {"name": "Vegetable soup", "price": 2.79, "quantity": 600, "category": "Canned Good"},
    {"name": "Tuna", "price": 1.99, "quantity": 900, "category": "Canned Good"},
    {"name": "Canned salmon", "price": 4.99, "quantity": 300, "category": "Canned Good"},
    {"name": "Canned sardines", "price": 3.29, "quantity": 400, "category": "Canned Good"},
    {"name": "Canned vegetables", "price": 1.89, "quantity": 800, "category": "Canned Good"},
    {"name": "Canned peach", "price": 2.39, "quantity": 700, "category": "Canned Good"},
    {"name": "Canned pear", "price": 2.19, "quantity": 600, "category": "Canned Good"},
    {"name": "Canned pineapple", "price": 2.99, "quantity": 500, "category": "Canned Good"},
    {"name": "Canned corn", "price": 1.59, "quantity": 800, "category": "Canned Good"},
    {"name": "Canned green bean", "price": 1.79, "quantity": 700, "category": "Canned Good"},

    {"name": "Spaghetti", "price": 1.99, "quantity": 1000, "category": "Pasta and Grain"},
    {"name": "Penne", "price": 1.79, "quantity": 1100, "category": "Pasta and Grain"},
    {"name": "White rice", "price": 2.49, "quantity": 900, "category": "Pasta and Grain"},
    {"name": "Brown rice", "price": 2.69, "quantity": 800, "category": "Pasta and Grain"},
    {"name": "Quinoa", "price": 4.99, "quantity": 500, "category": "Pasta and Grain"},
    {"name": "Oats", "price": 1.89, "quantity": 1200, "category": "Pasta and Grain"},
    {"name": "Lentil", "price": 1.29, "quantity": 1300, "category": "Pasta and Grain"},
    {"name": "Split pea", "price": 1.39, "quantity": 1400, "category": "Pasta and Grain"},
    {"name": "Pasta", "price": 1.59, "quantity": 1100, "category": "Pasta and Grain"},
    {"name": "Rice", "price": 1.49, "quantity": 1200, "category": "Pasta and Grain"},
    {"name": "Beans", "price": 1.29, "quantity": 1300, "category": "Pasta and Grain"},
    {"name": "Barley", "price": 2.19, "quantity": 1000, "category": "Pasta and Grain"},
    {"name": "Couscous", "price": 2.29, "quantity": 900, "category": "Pasta and Grain"},
    {"name": "Farro", "price": 3.49, "quantity": 600, "category": "Pasta and Grain"},
    {"name": "Orzo", "price": 2.09, "quantity": 1100, "category": "Pasta and Grain"},

    {"name": "Flour", "price": 3.49, "quantity": 700, "category": "Baking Essential"},
    {"name": "Sugar", "price": 2.99, "quantity": 800, "category": "Baking Essential"},
    {"name": "Baking powder", "price": 1.79, "quantity": 900, "category": "Baking Essential"},
    {"name": "Baking soda", "price": 1.69, "quantity": 1000, "category": "Baking Essential"},
    {"name": "Cornstarch", "price": 2.29, "quantity": 800, "category": "Baking Essential"},
    {"name": "Cake mix", "price": 2.99, "quantity": 700, "category": "Baking Essential"},
    {"name": "Cocoa powder", "price": 3.79, "quantity": 600, "category": "Baking Essential"},
    {"name": "Vanilla extract", "price": 4.99, "quantity": 500, "category": "Baking Essential"},

    {"name": "Breakfast cereal", "price": 3.49, "quantity": 700, "category": "Breakfast Item"},
    {"name": "Granola", "price": 4.29, "quantity": 600, "category": "Breakfast Item"},
    {"name": "Instant noodles", "price": 1.99, "quantity": 1000, "category": "Breakfast Item"},
    {"name": "Macaroni and cheese", "price": 2.79, "quantity": 900, "category": "Breakfast Item"},
    {"name": "Instant soup cup", "price": 2.39, "quantity": 1100, "category": "Breakfast Item"},
    {"name": "Pancake mix", "price": 3.29, "quantity": 800, "category": "Breakfast Item"},
    {"name": "Muffin mix", "price": 2.99, "quantity": 700, "category": "Breakfast Item"},
    {"name": "Instant oatmeal", "price": 2.19, "quantity": 1200, "category": "Breakfast Item"},

    {"name": "Assorted Nut", "price": 5.49, "quantity": 500, "category": "Snack"},
    {"name": "Trail mix", "price": 4.99, "quantity": 600, "category": "Snack"},
    {"name": "Cracker", "price": 2.49, "quantity": 800, "category": "Snack"},
    {"name": "Popcorn", "price": 3.29, "quantity": 700, "category": "Snack"},
    {"name": "Nut bar", "price": 1.99, "quantity": 1000, "category": "Snack"},
    {"name": "Granola bar", "price": 2.29, "quantity": 900, "category": "Snack"},
    {"name": "Pretzel", "price": 1.79, "quantity": 1100, "category": "Snack"},
    {"name": "Rice cake", "price": 1.49, "quantity": 1200, "category": "Snack"},

    {"name": "Mustard", "price": 1.99, "quantity": 700, "category": "Condiment"},
    {"name": "Mayonnaise", "price": 3.49, "quantity": 800, "category": "Condiment"},
    {"name": "BBQ sauce", "price": 2.79, "quantity": 900, "category": "Condiment"},
    {"name": "Soy sauce", "price": 2.29, "quantity": 1000, "category": "Condiment"},
    {"name": "Worcestershire sauce", "price": 2.99, "quantity": 800, "category": "Condiment"},
    {"name": "Hot sauce", "price": 1.99, "quantity": 700, "category": "Condiment"},
    {"name": "Teriyaki sauce", "price": 3.29, "quantity": 600, "category": "Condiment"},
    {"name": "Fish sauce", "price": 2.49, "quantity": 500, "category": "Condiment"},

    {"name": "Olive oil", "price": 6.99, "quantity": 700, "category": "Cooking Oil and Sauce"},
    {"name": "Vegetable oil", "price": 4.49, "quantity": 800, "category": "Cooking Oil and Sauce"},
    {"name": "Pasta sauce", "price": 3.29, "quantity": 900, "category": "Cooking Oil and Sauce"},
    {"name": "Soybean oil", "price": 5.49, "quantity": 1000, "category": "Cooking Oil and Sauce"},
    {"name": "Canola oil", "price": 4.99, "quantity": 800, "category": "Cooking Oil and Sauce"},
    {"name": "Sesame oil", "price": 7.99, "quantity": 700, "category": "Cooking Oil and Sauce"},
    {"name": "Alfredo sauce", "price": 3.79, "quantity": 600, "category": "Cooking Oil and Sauce"},
    {"name": "Marinara sauce", "price": 3.49, "quantity": 500, "category": "Cooking Oil and Sauce"},

    {"name": "Salt", "price": 1.29, "quantity": 1000, "category": "Spice and Seasoning"},
    {"name": "Pepper", "price": 2.49, "quantity": 1100, "category": "Spice and Seasoning"},
    {"name": "Oregano", "price": 1.79, "quantity": 900, "category": "Spice and Seasoning"},
    {"name": "Cumin", "price": 2.99, "quantity": 800, "category": "Spice and Seasoning"},
    {"name": "Paprika", "price": 1.99, "quantity": 1200, "category": "Spice and Seasoning"},
    {"name": "Chili powder", "price": 2.29, "quantity": 1300, "category": "Spice and Seasoning"},
    {"name": "Cinnamon", "price": 1.59, "quantity": 1400, "category": "Spice and Seasoning"},
    {"name": "Garlic powder", "price": 2.79, "quantity": 1500, "category": "Spice and Seasoning"},

    {"name": "Coffee", "price": 6.99, "quantity": 800, "category": "Beverage"},
    {"name": "Tea", "price": 4.99, "quantity": 900, "category": "Beverage"},
    {"name": "Fruit juice", "price": 3.49, "quantity": 1000, "category": "Beverage"},
    {"name": "Powdered milk", "price": 5.99, "quantity": 1100, "category": "Beverage"},
    {"name": "Evaporated milk", "price": 2.49, "quantity": 900, "category": "Beverage"},
    {"name": "Hot chocolate mix", "price": 4.29, "quantity": 800, "category": "Beverage"},
    {"name": "Lemonade mix", "price": 3.79, "quantity": 700, "category": "Beverage"},
    {"name": "Energy drink", "price": 2.99, "quantity": 600, "category": "Beverage"},

    {"name": "Honey", "price": 7.99, "quantity": 700, "category": "Sweetener"},
    {"name": "Maple syrup", "price": 9.99, "quantity": 600, "category": "Sweetener"},
    {"name": "Sugar", "price": 2.99, "quantity": 800, "category": "Sweetener"},
    {"name": "Agave syrup", "price": 8.99, "quantity": 700, "category": "Sweetener"},
    {"name": "Stevia", "price": 6.99, "quantity": 1000, "category": "Sweetener"},
    {"name": "Artificial sweetener", "price": 4.99, "quantity": 1100, "category": "Sweetener"},
    {"name": "Molasses", "price": 5.49, "quantity": 1200, "category": "Sweetener"},
    {"name": "Brown sugar", "price": 3.49, "quantity": 1300, "category": "Sweetener"},

    {"name": "Taco seasoning mix", "price": 1.49, "quantity": 800, "category": "Sauce Mix"},
    {"name": "Chili seasoning mix", "price": 1.79, "quantity": 900, "category": "Sauce Mix"},
    {"name": "Fajita seasoning mix", "price": 1.99, "quantity": 1000, "category": "Sauce Mix"},
    {"name": "Curry seasoning mix", "price": 2.29, "quantity": 1100, "category": "Sauce Mix"},
    {"name": "Gravy mix", "price": 1.29, "quantity": 1200, "category": "Sauce Mix"},
    {"name": "Ranch dressing mix", "price": 2.49, "quantity": 1300, "category": "Sauce Mix"},
    {"name": "Sloppy Joe seasoning mix", "price": 1.69, "quantity": 1400, "category": "Sauce Mix"},
    {"name": "Stir-fry sauce mix", "price": 2.79, "quantity": 1500, "category": "Sauce Mix"}
]

cart =[
    {"name": "Chicken noodle soup", "price": 3.99, "quantity": 0, "category": "Canned Good"},
    {"name": "Tomato soup", "price": 2.49, "quantity": 0, "category": "Canned Good"},
    {"name": "Vegetable soup", "price": 2.79, "quantity": 0, "category": "Canned Good"},
    {"name": "Tuna", "price": 1.99, "quantity": 0, "category": "Canned Good"},
    {"name": "Canned salmon", "price": 4.99, "quantity": 0, "category": "Canned Good"},
    {"name": "Canned sardines", "price": 3.29, "quantity": 0, "category": "Canned Good"},
    {"name": "Canned vegetables", "price": 1.89, "quantity": 0, "category": "Canned Good"},
    {"name": "Canned peach", "price": 2.39, "quantity": 0, "category": "Canned Good"},
    {"name": "Canned pear", "price": 2.19, "quantity": 0, "category": "Canned Good"},
    {"name": "Canned pineapple", "price": 2.99, "quantity": 0, "category": "Canned Good"},
    {"name": "Canned corn", "price": 1.59, "quantity": 0, "category": "Canned Good"},
    {"name": "Canned green bean", "price": 1.79, "quantity": 0, "category": "Canned Good"},

    {"name": "Spaghetti", "price": 1.99, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Penne", "price": 1.79, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "White rice", "price": 2.49, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Brown rice", "price": 2.69, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Quinoa", "price": 4.99, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Oats", "price": 1.89, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Lentil", "price": 1.29, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Split pea", "price": 1.39, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Pasta", "price": 1.59, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Rice", "price": 1.49, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Beans", "price": 1.29, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Barley", "price": 2.19, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Couscous", "price": 2.29, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Farro", "price": 3.49, "quantity": 0, "category": "Pasta and Grain"},
    {"name": "Orzo", "price": 2.09, "quantity": 0, "category": "Pasta and Grain"},

    {"name": "Flour", "price": 3.49, "quantity": 0, "category": "Baking Essential"},
    {"name": "Sugar", "price": 2.99, "quantity": 0, "category": "Baking Essential"},
    {"name": "Baking powder", "price": 1.79, "quantity": 0, "category": "Baking Essential"},
    {"name": "Baking soda", "price": 1.69, "quantity": 0, "category": "Baking Essential"},
    {"name": "Cornstarch", "price": 2.29, "quantity": 0, "category": "Baking Essential"},
    {"name": "Cake mix", "price": 2.99, "quantity": 0, "category": "Baking Essential"},
    {"name": "Cocoa powder", "price": 3.79, "quantity": 0, "category": "Baking Essential"},
    {"name": "Vanilla extract", "price": 4.99, "quantity": 0, "category": "Baking Essential"},

    {"name": "Breakfast cereal", "price": 3.49, "quantity": 0, "category": "Breakfast Item"},
    {"name": "Granola", "price": 4.29, "quantity": 0, "category": "Breakfast Item"},
    {"name": "Instant noodles", "price": 1.99, "quantity": 0, "category": "Breakfast Item"},
    {"name": "Macaroni and cheese", "price": 2.79, "quantity": 0, "category": "Breakfast Item"},
    {"name": "Instant soup cup", "price": 2.39, "quantity": 0, "category": "Breakfast Item"},
    {"name": "Pancake mix", "price": 3.29, "quantity": 0, "category": "Breakfast Item"},
    {"name": "Muffin mix", "price": 2.99, "quantity": 0, "category": "Breakfast Item"},
    {"name": "Instant oatmeal", "price": 2.19, "quantity": 0, "category": "Breakfast Item"},

    {"name": "Assorted Nut", "price": 5.49, "quantity": 0, "category": "Snack"},
    {"name": "Trail mix", "price": 4.99, "quantity": 0, "category": "Snack"},
    {"name": "Cracker", "price": 2.49, "quantity": 0, "category": "Snack"},
    {"name": "Popcorn", "price": 3.29, "quantity": 0, "category": "Snack"},
    {"name": "Nut bar", "price": 1.99, "quantity": 0, "category": "Snack"},
    {"name": "Granola bar", "price": 2.29, "quantity": 0, "category": "Snack"},
    {"name": "Pretzel", "price": 1.79, "quantity": 0, "category": "Snack"},
    {"name": "Rice cake", "price": 1.49, "quantity": 0, "category": "Snack"},

    {"name": "Mustard", "price": 1.99, "quantity": 0, "category": "Condiment"},
    {"name": "Mayonnaise", "price": 3.49, "quantity": 0, "category": "Condiment"},
    {"name": "BBQ sauce", "price": 2.79, "quantity": 0, "category": "Condiment"},
    {"name": "Soy sauce", "price": 2.29, "quantity": 0, "category": "Condiment"},
    {"name": "Worcestershire sauce", "price": 2.99, "quantity": 0, "category": "Condiment"},
    {"name": "Hot sauce", "price": 1.99, "quantity": 0, "category": "Condiment"},
    {"name": "Teriyaki sauce", "price": 3.29, "quantity": 0, "category": "Condiment"},
    {"name": "Fish sauce", "price": 2.49, "quantity": 0, "category": "Condiment"},

    {"name": "Olive oil", "price": 6.99, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Vegetable oil", "price": 4.49, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Pasta sauce", "price": 3.29, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Soybean oil", "price": 5.49, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Canola oil", "price": 4.99, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Sesame oil", "price": 7.99, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Alfredo sauce", "price": 3.79, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Marinara sauce", "price": 3.49, "quantity": 0, "category": "Cooking Oil and Sauce"},

    {"name": "Salt", "price": 1.29, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Pepper", "price": 2.49, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Oregano", "price": 1.79, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Cumin", "price": 2.99, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Paprika", "price": 1.99, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Chili powder", "price": 2.29, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Cinnamon", "price": 1.59, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Garlic powder", "price": 2.79, "quantity": 0, "category": "Spice and Seasoning"},

    {"name": "Coffee", "price": 6.99, "quantity": 0, "category": "Beverage"},
    {"name": "Tea", "price": 4.99, "quantity": 0, "category": "Beverage"},
    {"name": "Fruit juice", "price": 3.49, "quantity": 0, "category": "Beverage"},
    {"name": "Powdered milk", "price": 5.99, "quantity": 0, "category": "Beverage"},
    {"name": "Evaporated milk", "price": 2.49, "quantity": 0, "category": "Beverage"},
    {"name": "Hot chocolate mix", "price": 4.29, "quantity": 0, "category": "Beverage"},
    {"name": "Lemonade mix", "price": 3.79, "quantity": 0, "category": "Beverage"},
    {"name": "Energy drink", "price": 2.99, "quantity": 0, "category": "Beverage"},

    {"name": "Mustard", "price": 1.99, "quantity": 0, "category": "Condiment"},
    {"name": "Mayonnaise", "price": 3.49, "quantity": 0, "category": "Condiment"},
    {"name": "BBQ sauce", "price": 2.79, "quantity": 0, "category": "Condiment"},
    {"name": "Soy sauce", "price": 2.29, "quantity": 0, "category": "Condiment"},
    {"name": "Worcestershire sauce", "price": 2.99, "quantity": 0, "category": "Condiment"},
    {"name": "Hot sauce", "price": 1.99, "quantity": 0, "category": "Condiment"},
    {"name": "Teriyaki sauce", "price": 3.29, "quantity": 0, "category": "Condiment"},
    {"name": "Fish sauce", "price": 2.49, "quantity": 0, "category": "Condiment"},

    {"name": "Olive oil", "price": 6.99, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Vegetable oil", "price": 4.49, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Pasta sauce", "price": 3.29, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Soybean oil", "price": 5.49, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Canola oil", "price": 4.99, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Sesame oil", "price": 7.99, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Alfredo sauce", "price": 3.79, "quantity": 0, "category": "Cooking Oil and Sauce"},
    {"name": "Marinara sauce", "price": 3.49, "quantity": 0, "category": "Cooking Oil and Sauce"},

    {"name": "Salt", "price": 1.29, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Pepper", "price": 2.49, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Oregano", "price": 1.79, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Cumin", "price": 2.99, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Paprika", "price": 1.99, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Chili powder", "price": 2.29, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Cinnamon", "price": 1.59, "quantity": 0, "category": "Spice and Seasoning"},
    {"name": "Garlic powder", "price": 2.79, "quantity": 0, "category": "Spice and Seasoning"}
]

# loop. Breaks on exit().
while True:
    menuMain()