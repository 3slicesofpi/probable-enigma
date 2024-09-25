
import csv
import PySimpleGUI as sg

class Category:
    def __init__(self, id: str, name: str, longname: str=False, desc: str=''):
        self.id = id
        self.name = name
        if longname:
            self.longname = longname
        else:
            self.longname = name
        self.description = desc
        self.content = {}

    def get_self_info(self) -> dict:
        return {'id': self.id,
                'name': self.name,
                'longname': self.longname,
                'description': self.description,
                'contentkeys': self.content.keys()}

    def get_self_size(self) -> int:
        return len(self.content)

    def get_content_info(self, target) -> dict:
        return self.content[target].get_self_info()


class ItemData:
    """Contains Shared Data"""
    def __init__(self, id: str, name: str, cost: float, category: Category, longname: str = False, desc: str = ''):
        self.id = id
        category.content[id] = self
        self.category = category
        self.name = name
        if longname:
            self.longname = longname
        else:
            self.longname = name
        self.cost = cost
        self.description = desc

    def get_self_info(self) -> dict:
        return {'id': self.id,
                'name': self.name,
                'longname': self.longname,
                'description': self.description,
                'cost': self.cost,
                'category': self.category.name}

    def create_dynamic_instance(self, count=0):
        return ItemDataDynamic(self, count)


class ItemDataDynamic:
    def __init__(self, itemdata: ItemData, count=0):
        self.id = itemdata.id
        self.name = itemdata.name
        self.count = count
        self.discount = 0

    def get_self_info(self) -> dict:
        return {'count': self.count,
                'discount': self.discount}

    def get_self_exist(self) -> bool:
        return bool(self.count)


class Cart:

    def __init__(self, id, name, itemdata: {str: ItemData}):
        self.id = id
        self.name = name

        self.data = itemdata
        self.dynamic = {id: content.create_dynamic_instance() for id, content in zip(itemdata.keys(), itemdata.values())}

    def update_dynamic(self, count=0):
        for i in self.data.keys():
            if i not in self.dynamic.keys():
                self.dynamic[i] = self.data[i].create_dynamic_instance(count)

    def modify_count(self, target, count=0):
        self.dynamic[target].count += count

    def modify_count_list(self, countlist: list):
        for count, dynamic in zip(countlist, self.dynamic.values()):
            dynamic.count += count

    def get_target_value(self, target):
        return self.dynamic[target].count * self.data[target].cost - self.dynamic[target].discount

    def get_category_value(self, targetc):
        return [(dynamic.count * data.cost - dynamic.discount) * data.category == targetc
                for data, dynamic in zip(self.data.values(), self.dynamic.values())]

    def get_value_list(self) -> list:
        return [dynamic.count * data.cost - dynamic.discount
                for data, dynamic in zip(self.data.values(), self.dynamic.values())]

    def get_value_total(self):
        return sum(self.get_value_list())

    def get_count_target(self, target):
        return self.dynamic[target].count

    def get_count_category(self, targetc):
        return [dynamic.count * targetc == data.category
                for data, dynamic in zip(self.data, self.dynamic.values())]

    def get_count_list(self):
        return [dynamic.count for dynamic in self.dynamic.values()]

    def get_count_total(self):
        return sum(self.get_count_list())

    def set_count_target(self, target, new=0):
        self.dynamic[target].count = new

    def set_count_list(self, newlist: list):
        for new, dynamic in zip(newlist, self.dynamic.values()):
            dynamic.count = new

    def get_target_info(self, target) -> dict:
        newdict = {'value': self.get_target_value(target)}
        newdict.update(self.data[target].get_self_info())
        newdict.update(self.dynamic[target].get_self_info())
        return newdict

    def get_all_list(self):
        return [self.get_target_info(i) for i in self.data.keys()]




def csvimport(itemsfile = 'market 0.5raw.csv', categoriesfile = 'market 0.5raw1.csv'):
    # creating a csv reader object
    with open(categoriesfile, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        categories = {}
        for row in csvreader:
            categories[row[0]] = Category(row[0], row[1], row[2], row[3])

    with open(itemsfile, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        items = {}
        for row in csvreader:
            items[row[0]] = ItemData(row[0], row[1], float(row[4]), categories[row[3]], row[2], row[5])

    return items, categories


items, categories = csvimport()

invCart = Cart('INVB', 'invCart', items)
userCart = Cart('USEB', 'userCart', items)

# items['PAM4'] = ItemData('PAM4', 'spam', 100, categories['TESC'], ', spam', 'and more spam')

digits = frozenset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})

# ----------- thy GUI -----------
# javascript be laughing rn

layout1 = [[sg.Text('Main Menu')],
           [sg.Button('Next Menu')]]

layout2 = [[sg.Text('Next Menu')],
           *[[sg.Text(str(i))] for i in invCart.get_all_list()],
           [sg.Button('Last Menu')]]

layout3 = [[sg.Text('This is layout Last Menu - It is all Radio Buttons')],
           *[[sg.R(f'Radio {i}', 1)] for i in range(3)],
           [sg.Button('Main Menu')],
           [sg.Button('Next Menu')],
           [sg.Button('Last Menu')]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-Main Menu-'),
           sg.Column(layout2, visible=False, key='-Next Menu-'),
           sg.Column(layout3, visible=False, key='-Last Menu-')],
           [sg.Button('Exit')]]

window = sg.Window('Swapping the contents of a window', layout)

layoutSelected = 'Main Menu'  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    elif event:
        window[f'-{layoutSelected}-'].update(visible=False)
        layoutSelected = ''.join(c for c in event if c not in digits)
        window[f'-{layoutSelected}-'].update(visible=True)
window.close()

