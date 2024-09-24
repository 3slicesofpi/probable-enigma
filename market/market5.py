import cmd


class CategoryClass:
    def __init__(self, id:str, name: str, longname: str=False):
        self.id = id
        self.name = name
        if longname:
            self.longname = longname
        else:
            self.longname = name
        self.description = None
        self.content = {}

    def get_information(self):
        return {'id': self.id,
                'name': self.name,
                'longname': self.longname,
                'description': self.description}


class ItemClassStatic:
    def __init__(self, id: str, name: str, cost: float, category: CategoryClass, longname: str=False):
        self.id = id
        category.content[id] = self
        self.category = category
        self.name = name
        if longname:
            self.longname = longname
        else:
            self.longname = name
        self.cost = cost
        self.description = None


    def add_ItemClassDynamic(self, dest, count: int=0):
        dest.dynamicContent[self.id] = ItemClassDynamic(self.id, self.name, count)

    def get_information(self) -> dict:
        return {'id': self.id,
                'name': self.name,
                'longname': self.longname,
                'description': self.description,
                'cost': self.cost,
                'category': self.category.name}



class ItemClassDynamic:
    def __init__(self, id: str, name: str, count: int=0):
        self.id = id
        self.name = name
        self.count = count
        self.discount = 0  # local discounts are numeric, global are percentage

    def get_information(self) -> dict:
        return {'count': self.count,
                'discount': self.discount}

    def copy(self, dest, count: int=0):
        if not count:
            count = self.count
        dest.dynamicContent[self.id] = ItemClassDynamic(self.id, count)

class CartClass:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.staticContent = {}
        self.dynamicContent = {}

    def add_item(self, infostatic: ItemClassStatic):
        self.staticContent[infostatic.id] = infostatic
        infostatic.add_ItemClassDynamic(self)

    def add_item_list(self, itemstatic_list: dict):
        for itemstatic in itemstatic_list.values():
            self.staticContent[itemstatic.id] = itemstatic
            itemstatic.add_ItemClassDynamic(self)

    def modify_count(self, target, count) -> None:
        self.dynamicContent[target].count += count

    def get_information(self, target) -> dict:
        newdict = {'value': self.get_value(target)}
        newdict.update(self.staticContent[target].get_information())
        newdict.update(self.dynamicContent[target].get_information())
        return newdict

    def get_value(self, target) -> float:
        return self.dynamicContent[target].count * self.staticContent[target].cost - self.dynamicContent[target].discount

    def get_value_list(self) -> list:
        return [dynamic.count * static.cost - dynamic.discount for static, dynamic in zip(self.staticContent.values(), self.dynamicContent.values())]

    def get_count_list(self) -> list:
        return [dynamic.count for dynamic in self.dynamicContent.values()]

    def set_count_list(self, count) -> None:
        for i, dynamic in zip(count, self.dynamicContent.values()):
            dynamic.count = i


def itemsearch_init(items):
    """Returns a list of possible user resp. Works (mostly) for cats too."""
    dict = {}
    for item in items.values():
        dict[item.id] = [item.id.lower(), item.name.lower(), item.longname.lower()]
    return dict


invCart = CartClass('INVB', 'invCart')
userCart = CartClass('USEB', 'userCart')

testCategory = CategoryClass('TESC', 'monty')

items = {'BE00': ItemClassStatic('BE00', 'beans', 1, testCategory),
         'EGG1': ItemClassStatic('EGG1', 'egg', 1, testCategory),
         'TOAD': ItemClassStatic('TOAD', 'toast', 100, testCategory),
         'SAM1': ItemClassStatic('SAM1', 'spam', 2, testCategory)}


itemsearch = itemsearch_init(items)

categories = {'TESC': testCategory}

categoriesearch = itemsearch_init(categories)

invCart.add_item_list(items)
userCart.add_item_list(items)

invCart.set_count_list((100, 120, 2931, 1))

class MainMenu(cmd.Cmd):
    def do_view(self, arg):
        """See everything in shop."""
        for i in items.keys():
            info = invCart.get_information(i)
            print(f"{info['count']}x | {info['name']} | {info['cost']} | {info['id']}")

    def do_start(self, arg):
        typ = None
        if arg.upper() in categoriesearch.keys():
            arg = arg.upper()
            typ = 'category'
        else:
            for i in categoriesearch.keys():
                if arg in categoriesearch[i]:
                    arg = i
                    typ = 'category'
                    continue
        if arg.upper() in itemsearch.keys():
            arg.upper()
            typ = 'item'
        elif not typ:
            for i in itemsearch.keys():
                if arg.lower() in itemsearch[i]:
                    arg = i
                    typ = 'item'
                    continue
        if typ == 'category':
            info = categories[arg].get_information()
            print(f"{info['id']} | {info['longname']} | {info['description']}")
            for i in categories[arg].content.keys():
                contentinfo = invCart.get_information(i)
                print(f"{contentinfo['count']}x | "
                      f"{contentinfo['id']} - {contentinfo['longname'].capitalize()} | "
                      f"${contentinfo['cost']} | "
                      f"{contentinfo['description']}")
        elif typ == 'item':
            info = invCart.get_information(arg)
            print(f"{info['count']} | {info['id']} - {info['longname']} | {info['cost']} | {info['category']}")
            if info['description']:
                print(info['description'])
        else:
            for i in categories.values():
                info = i.get_information()
                print(f"{info['id']} - {info['longname']} | ", end='')
                if info['description']:
                    print(info['description'])
                else:
                    print('')

    def do_move(self, arg):
        try:
            target, number = [str(s) for s in arg.split(',')]
            if target.upper() in itemsearch.keys():
                target.upper()
            else:
                for i in itemsearch.keys():
                    if target.lower() in itemsearch[i]:
                        target = i
                        continue
            number = int(number)
        except:
            print('Invalid Argument!')
            return
        if number > 0 and invCart.get_information(target)['count'] >= number:
            userCart.modify_count(target, number)
            invCart.modify_count(target, -number)
            print('Moved', number, items[target].name, 'to cart')
        elif number < 0 and userCart.get_information(target)['count'] >= -number:
            userCart.modify_count(target, number)
            invCart.modify_count(target, -number)
            print('Returned', number, items[target].name, 'from cart')

    def do_return(self, arg):
        try:
            target, number = [str(s) for s in arg.split(',')]
            if target.upper() in itemsearch.keys():
                target = target.upper()
            else:
                for i in itemsearch.keys():
                    if target.lower() in itemsearch[i]:
                        target = i
                        continue
            number = int(number)
        except:
            print('Invalid Argument!')
            return
        if number > 0 and invCart.get_information(target)['count'] >= number:
            userCart.modify_count(target, -number)
            invCart.modify_count(target, number)
            print('Returned', number, items[target].name, 'from cart')
        elif number < 0 and userCart.get_information(target)['count'] >= -number:
            userCart.modify_count(target, -number)
            invCart.modify_count(target, number)
            print('Moved', number, items[target].name, 'to cart')


    def do_empty(self, arg):
        if arg:
            pass
        else:
            if not input('Are you sure you want to empty your cart?\nPress any key to confirm'
                     '\nPress [ENTER] to cancel\nInput Argument >>:'):
                return
        newlist = [sum(i) for i in zip(invCart.get_count_list(), userCart.get_count_list())]
        invCart.set_count_list(newlist)
        userCart.set_count_list([0 for i in range(len(newlist))])
        print(invCart.get_count_list())
        print(userCart.get_count_list())

    def do_quit(self, arg):
        if arg:
            raise SystemExit
        else:
            if input('Are you sure you want to quit?\nPress any key to exit'
                     '\nPress [ENTER] to cancel\nInput Argument >>:'):
                raise SystemExit


prompt = MainMenu()
prompt.prompt = 'Input Command >>:'
prompt.cmdloop('...')
