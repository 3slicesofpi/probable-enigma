from math import ceil
def listFormatter(theList):
    # remove quan = 0
    newList = [None]
    for here in theList:
        if here['quantity'] == 0:
            pass
        else:
            newList.append(here)
    # frontend
    pageSelected = 0
    while True:
        if (pageSelected*10+10)<len(newList)+1:
            pageMax = (pageSelected*10)+10
        else:
            pageMax = len(newList)
        for iteration in range(pageSelected*10,pageMax):
            print(newList[iteration])
        print('you are at page:',(pageSelected+1), 'of', (ceil(len(newList)/10)))
        clientInput = input('input a command >:::')
        if clientInput == 'e':
            exit()
        elif clientInput == 'n':
            pageSelected += 1
        elif clientInput == 'b':
            pageSelected -= 1
        else:
            pageSelected = int(clientInput)-1
        if (pageSelected < 0) or (pageSelected > ceil(len(newList)/10)-1):
            pageSelected = 0
    

catalog = [{"product": "Black beans", "price": 5.98, "quantity": 0}, {"product": "Kidney beans", "price": 4.98, "quantity": 0}, {"product": "Chickpeas", "price": 6.58, "quantity": 0}, {"product": "Chicken noodle soup", "price": 3.58, "quantity": 2400}, {"product": "Tomato soup", "price": 3.98, "quantity": 17800}, {"product": "Vegetable soup", "price": 4.58, "quantity": 6800}, {"product": "Tuna", "price": 2.98, "quantity": 11200}, {"product": "Canned salmon", "price": 7.98, "quantity": 15600}, {"product": "Canned sardines", "price": 5.58, "quantity": 18000}, {"product": "Canned vegetables (corn, peas, carrots)", "price": 5.38, "quantity": 24600}, {"product": "Canned peaches", "price": 5.98, "quantity": 11200}, {"product": "Canned pears", "price": 5.78, "quantity": 15600}, {"product": "Canned pineapple", "price": 6.98, "quantity": 9000}, {"product": "Spaghetti", "price": 2.58, "quantity": 6400}, {"product": "Penne", "price": 2.38, "quantity": 17800}, {"product": "White rice", "price": 4.98, "quantity": 4600}, {"product": "Brown rice", "price": 5.58, "quantity": 11200}, {"product": "Quinoa", "price": 9.98, "quantity": 15600}, {"product": "Oats", "price": 3.98, "quantity": 18000}, {"product": "Breakfast cereals", "price": 7.18, "quantity": 2400}, {"product": "Granola", "price": 7.58, "quantity": 6800}, {"product": "Lentils", "price": 4.78, "quantity": 9000}, {"product": "Split peas", "price": 4.38, "quantity": 13400}, {"product": "Pasta", "price": 2.98, "quantity": 4600}, {"product": "Rice", "price": 4.58, "quantity": 11200}, {"product": "Lentils", "price": 4.78, "quantity": 15600}, {"product": "Beans", "price": 4.58, "quantity": 18000}, {"product": "Crushed tomatoes", "price": 3.78, "quantity": 2400}, {"product": "Tomato sauce", "price": 2.98, "quantity": 9000}, {"product": "Tomato paste", "price": 2.58, "quantity": 13400}, {"product": "Flour", "price": 4.18, "quantity": 17800}, {"product": "Sugar", "price": 3.98, "quantity": 4600}, {"product": "Baking powder", "price": 3.58, "quantity": 11200}, {"product": "Baking soda", "price": 3.38, "quantity": 15600}, {"product": "Ketchup", "price": 4.98, "quantity": 18000}, {"product": "Mustard", "price": 3.58, "quantity": 2400}, {"product": "Mayonnaise", "price": 5.98, "quantity": 9000}, {"product": "Olive oil", "price": 8.98, "quantity": 13400}, {"product": "Vegetable oil", "price": 5.98, "quantity": 17800}, {"product": "Assorted Nuts", "price": 11.98, "quantity": 4600}, {"product": "Trail mix", "price": 7.78, "quantity": 11200}, {"product": "Crackers", "price": 4.58, "quantity": 15600}, {"product": "Popcorn", "price": 3.98, "quantity": 18000}, {"product": "Pasta sauce", "price": 4.78, "quantity": 2400}, {"product": "Salsa", "price": 5.18, "quantity": 9000}, {"product": "BBQ sauce", "price": 5.58, "quantity": 13400}, {"product": "Canned chicken", "price": 6.98, "quantity": 17800}, {"product": "Spam", "price": 5.98, "quantity": 4600}, {"product": "Corned beef", "price": 7.58, "quantity": 11200}]
listFormatter(catalog)