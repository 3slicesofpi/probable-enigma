# catalog = [{id:0,'product':'a','quantity':1000,'price':2},{id:1,'product':'b','quantity':250,'price':5}]

# for here in catalog:
#     if here['product'] == 'a':
#         catalog.remove(here)
# print(catalog)


cart = [
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

num = 0
for dict in cart:
    dict['position'] = num
    num+=1

print(cart)