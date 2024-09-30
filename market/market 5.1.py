
import csv
import PySimpleGUI as sg

tax_constant = 0.09

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
                'category': self.category.id,
                'categoryname': self.category.name}

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
        if self.count > 0:
            return True
        else:
            return False


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

    def modify_count(self, target, count=0) -> int:
        dynamicObject = self.dynamic[target]
        if dynamicObject.count + count > 0:
            dynamicObject.count += count
            print(dynamicObject.count)
            return dynamicObject.count
        else:
            dynamicObject.count = 0
            return 0

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

    def get_target_info(self, target, unshow: bool=False):
        if unshow and not self.dynamic[target].get_self_exist():
            return None
        newdict = {'value': self.get_target_value(target)}
        newdict.update(self.data[target].get_self_info())
        newdict.update(self.dynamic[target].get_self_info())
        return newdict

    def get_all_list(self):
        return [self.get_target_info(i) for i in self.data.keys()]

    def get_exist_list(self):
        # print([self.get_target_info(i, True) for i in self.data.keys()])
        lis = []
        for i in self.data.keys():
            ap = self.get_target_info(i, True)
            if ap:
                lis.append(ap)
        return lis


    def get_numof_exist_items(self):
        return sum([int(i.get_self_exist()) for i in self.dynamic.values()])

    def gui_make_table_data(self):
        tabledata = ['']
        tabledata.extend([[ i['id'], i['count'], i['name'], f"${i['cost']:.2f}"]
                          for i in self.get_exist_list()])
        tabledata.pop(0)
        self.gui_tabledata = tabledata
        return tabledata

    def gui_make_table_head(self):
        heading = [' ID ', 'Qty', 'Item Name', 'Cost']
        self.gui_tablehead = heading
        return heading


# loadlayout = [[sg.Text('Loading your gloarious content!')],
#               [sg.Text('====={'),
#               sg.Text('|', key='-THROBR-'),
#               sg.Text('}=====')]]



def csvimport(itemsfile='market 0.5raw.csv',
              categoriesfile='market 0.5raw1.csv'):
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
invCart.set_count_list([10*i for i in range(len(invCart.data))])
userCart = Cart('USEB', 'userCart', items)

# items['PAM4'] = ItemData('PAM4', 'spam', 100, categories['TESC'], ', spam', 'and more spam')

digits = frozenset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
dis_info = {'-RADIO OPT A-': ['Members (15% off)', 0.15],
            '-RADIO OPT B-': ['Students (10% off)', 0.1],
            '-RADIO OPT C-': ['Senior Citizens (25% off)', 0.25]}


# ----------- thy GUI -----------
# javascript be laughing at dis rn
# NO NUMERICS IN KEY!!!!!

# ----------- Create the many layouts this Window will display -----------
layout1 = [[sg.Button('Browse Items', key='1-MENU SHOWINV-'),
            sg.Button('Checkout and Finish', key='1-MENU CHECKOUT-', disabled=True)]]

layout2 = [[sg.Table(values=invCart.gui_make_table_data()[:][:],
                     headings=invCart.gui_make_table_head(),
                     max_col_width=20, justification='center',
                     background_color='darkblue', alternating_row_color='blue',
                     auto_size_columns=True, display_row_numbers=False,
                     num_rows=14,
                     enable_events=True, key='2-TABLEINV-',
                     tooltip='Shop Inventory'),

            sg.Column([
            [sg.Button('Information', key='2-MENU ITEMINFO-', disabled=True)],
            [sg.Slider((0, 1), 1, disabled=True,
                      enable_events=True, key='2-QUAN TAKE-',
                      tooltip='Select the number of items you want. Slide bar back to return items.')],
            [sg.Button('Transfer', disabled=True, key='2-CONF TAKE-',
                      tooltip='Confirm that you want to take this item.')],
            [sg.Button('Return All', disabled=True, key='2-CONF RET-',
                      tooltip='Confirm that you want to return this item.')]]),

            sg.Table(values=userCart.gui_make_table_data()[:][:],
                     headings=userCart.gui_make_table_head(),
                     max_col_width=20, justification='center',
                     background_color='darkblue', alternating_row_color='blue',
                     auto_size_columns=True, display_row_numbers=False,
                     num_rows=14,
                     enable_events=True, key='2-TABLEUSER-',
                     tooltip='Items in cart')],

           [sg.Button('Main Menu', key='2-MENU MAIN-'),
            sg.Button('Proceed to Checkout', key='2-MENU CHECKOUT-', disabled=True)]]

layout3 = [[sg.Text('err- name not found', key='3-TEXT ITEMNAME-',
                    tooltip='item id, longname, cost')],
           [sg.Text('count to TREE(3)', key='3-TEXT ITEMCOUNT-',
                    tooltip='item count, value')],
           [sg.Text('cate', key='3-TEXT ITEMCATE-',
                    tooltip='item category')],
           [sg.Text('insert joke here', key='3-TEXT ITEMDESC-',
                    tooltip='item desc')],

           [sg.Button('Go Back', key='3-GOBACK-'),
           sg.Button('Main Menu', key='3-MENU MAIN-')]]

layout5 = [
           [sg.Text('sub-total', key='5-TEXT SUBTOTAL-')],
           [sg.Text('+$0.00', key='5-TEXT DISINFO-'),
            sg.Button('Apply Discount', key='5-MENU DISCOUNT-', disabled=False)],
           [sg.Text('yoshi commits tax fraud', key='5-TEXT TAX-')],
           [sg.Text('final destination no items fox only', key='5-TEXT FINTOTAL-')],
           [sg.Button('Go Back', key='5-GOBACK-'),
            sg.Button('Purchase More', key='5-MENU SHOWINV-'),
            sg.Button('Main Menu', key='5-MENU MAIN-')
            ]]

layout6 = [[sg.Text('Apply Discounts', key='6-TEXT M HEADER-')],
           [sg.Text('sub-total part 2 electric boogaloo', key='6-TEXT SUBTOTAL-')],
           [sg.Radio(value[0], enable_events=True, tooltip='Select a Discount',
                     key=f"{key}", group_id='6-RADIO DIS INFO-')
            for key, value in zip(tuple(dis_info.keys()), tuple(dis_info.values()))],
           [sg.Button('Reset Selection', key='6-RESET DIS INFO-',
                      tooltip='Deselect Current Discount Selection')],
           [sg.Button('Return', key='6-MENU CHECKOUT-')]]

# ----------- Create actual layout using Columns and a row of Buttons
layoutmain = [[sg.Text('Market 0.5.2 InD3v', key='-TEXT HEADER-')],
              [sg.Column(layout1, key='-MENU MAIN-'),
               sg.Column(layout2, visible=False, key='-MENU SHOWINV-'),
               sg.Column(layout3, visible=False, key='-MENU ITEMINFO-'),
               sg.Column(layout5, visible=False, key='-MENU CHECKOUT-'),
               sg.Column(layout6, visible=False, key='-MENU DISCOUNT-'),
               ],
              [sg.Text('Welcome to Market!', key='-TEXT GLOBAL-')],
              [sg.Button('Exit')]]

window = sg.Window('Market 0.5.3', layoutmain)

itemSelected = tuple(items.keys())[0]  # temp, replace with first item's id when prod
lastMenu = '-MENU MAIN-'
selMenu = '-MENU MAIN-'  # The currently visible layout
selDiscount = 0
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    else:
        event = ''.join(c for c in event if c not in digits)

    if 'MENU' in event:
        window[selMenu].update(visible=False)
        selMenu = event
        window[selMenu].update(visible=True)

        if selMenu in ['-MENU SHOWINV-', '-MENU SHOWUSER-']:
            lastMenu = selMenu
            window['-TEXT HEADER-'].update("Contents of Shop Inventory / Your Cart")
        elif selMenu == '-MENU CHECKOUT-':
            tmp = userCart.get_value_total()
            window['-TEXT HEADER-'].update(f"Checkout - Purchasing {userCart.get_count_total()} items")
            window['5-TEXT SUBTOTAL-'].update(f"+${tmp:<10.2f} - Subtotal for {userCart.get_count_total()} item(s).")
            window['5-TEXT TAX-'].update(f"+${tmp*tax_constant:<10.2f} - {tax_constant*100:.0f}% tax")
            tmp *= (1-selDiscount)
            tmp *= (1+tax_constant)
            window['5-TEXT FINTOTAL-'].update(f"+${tmp:<10.2f} - Final Total")
        # when menu is changed, disable all disableable buttons,
        # also do the one below
        window['2-QUAN TAKE-'].update(range=(0, 1), value=1, disabled=True)
        window['2-CONF TAKE-'].update(disabled=False)

        window['2-CONF RET-'].update(disabled=True)

        window['2-MENU ITEMINFO-'].update(disabled=True)

    if 'GOBACK' in event:
        window['-TEXT HEADER-'].update('Returned you to previous menu.')
        window[selMenu].update(visible=False)
        window[lastMenu].update(visible=True)
        selMenu = lastMenu

        # when menu is changed, disable all disableable buttons
        # don't forget to modify the one above!
        window['2-QUAN TAKE-'].update(range=(0, 1), value=1, disabled=True)
        window['2-CONF TAKE-'].update(disabled=False)

        window['2-CONF RET-'].update(disabled=True)

        window['2-MENU ITEMINFO-'].update(disabled=True)

    if 'TABLE' in event:
        # idk what is happening here
        selTable = str({'-MENU MAIN-': '1', '-MENU SHOWINV-': '2'}[selMenu])+event

        if values[selTable]:
            # this is a stupid, stupid solution!
            # the problem came too early, identified too late.
            # this will do. will cause problems later.
            # as long as we don't a) add more Carts, b) do weird stuff to values dict, c) explode.
            if selTable == '2-TABLEINV-':  # ensure using the correct carts
                itemSelected = invCart.gui_tabledata[values[selTable][0]][0]

            else:
                itemSelected = userCart.gui_tabledata[values[selTable][0]][0]

        # when table is clicked, enable all related enableable buttons
        window['2-QUAN TAKE-'].update(range=(-userCart.get_count_target(itemSelected), invCart.get_count_target(itemSelected)), disabled=False)


        window['2-MENU ITEMINFO-'].update(disabled=False)

    if 'ITEMINFO' in event:
        tmp = userCart.get_target_info(itemSelected)
        window['-TEXT HEADER-'].update(f"Viewing Product Information: {tmp['name']}")
        window['3-TEXT ITEMNAME-'].update(f"Selected Item: {tmp['longname'].capitalize()} ({tmp['id']}) Price: ${tmp['cost']}")
        if tmp['count'] == 1:
            window['3-TEXT ITEMCOUNT-'].update(
                f"You have one {tmp['name']} in your cart, costing {tmp['value']} in total.")
        elif tmp['count']:
            window['3-TEXT ITEMCOUNT-'].update(
                f"You have {tmp['count']} {tmp['name']}s in your cart, costing {tmp['value']:.2f} in total.")
        else:
            window['3-TEXT ITEMCOUNT-'].update(
                f"You have no {tmp['name']} in your cart.")
        window['3-TEXT ITEMDESC-'].update(tmp['description'])
        window['3-TEXT ITEMCATE-'].update(f"Category: {tmp['categoryname']} ({tmp['category']})")

    if 'QUAN TAKE' in event:
        if values['2-QUAN TAKE-']:
            window['2-CONF TAKE-'].update(disabled=False)
        else:
            window['2-CONF TAKE-'].update(disabled=True)

    if 'CONF TAKE' in event:
        # never trust tmp, use ist sparingly and always initialize it

        window['-TEXT HEADER-'].update(f"Transferred {invCart.data[itemSelected].name}!")
        invCart.modify_count(itemSelected, -int(values['2-QUAN TAKE-']))
        if userCart.modify_count(itemSelected, +int(values['2-QUAN TAKE-'])):
            window['2-CONF RET-'].update(disabled=False)
        else:
            window['2-CONF RET-'].update(disabled=True)

        window['2-QUAN TAKE-'].update(
        range=(-userCart.get_count_target(itemSelected), invCart.get_count_target(itemSelected)))


        if invCart.get_count_total():
            window['2-TABLEINV-'].update(values=invCart.gui_make_table_data(), visible=True)
        else:  # if nothing in inv...
            window['2-TABLEINV-'].update(values=[['No items in Inventory'].extend(['' for i in range(len(invCart.gui_tablehead)-1)])])
            window['2-MENU ITEMINFO-'].update(disabled=True)

            for i in ('1', '5'):
                window[str(i+'-MENU SHOWINV-')].update(disabled=True)

        for i in ('1', '2'):
            window[str(i+'-MENU CHECKOUT-')].update(disabled=False)

        for i in ('2'):
            window[str(i+'-TABLEUSER-')].update(values=userCart.gui_make_table_data(), visible=True)

    if 'RESET' in event:
        selDiscount = 0
        window['-RADIO OPT A-'].reset_group()
        window['5-MENU DISCOUNT-'].update('Apply Discount')
        window['5-TEXT DISINFO-'].update('-$0.00')

    if 'RADIO' in event:
        selDiscount = dis_info[event][1]
        window['5-MENU DISCOUNT-'].update('Change Discount')
        window['5-TEXT DISINFO-'].update(f"-${userCart.get_value_total()*dis_info[event][1]:.2f}: {dis_info[event][0]}", visible=True)

    if 'CONF RET' in event:
        invCart.modify_count(itemSelected, +userCart.get_count_target(itemSelected))
        userCart.modify_count(itemSelected, -userCart.get_count_target(itemSelected))

        window['2-TABLEINV-'].update(values=invCart.gui_make_table_data())
        for i in ('1', '5'):
            window[str(i+'-MENU SHOWINV-')].update(disabled=False)

        if userCart.get_count_total():  # anything left in usercart?
            window['2-TABLEUSER-'].update(values=userCart.gui_make_table_data(), visible=True)
        else:
            window['2-MENU CHECKOUT-'].update(disabled=True)

            window['2-TABLEUSER-'].update(values=[['Cart is Empty!'].extend(['' for _ in range(len(userCart.gui_tablehead)-1)])])
            window['2-CONF RET-'].update(disabled=True)

window.close()
