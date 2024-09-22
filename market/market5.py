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
        category.content[name] = self
        self.category = category
        self.name = name
        if longname:
            self.longname = longname
        else:
            self.longname = name
        self.cost = cost
        self.description = None


    def add_ItemClassDynamic(self, dest, count: int=0):
        dest.dynamicContent[self.id] = ItemClassDynamic(self.id, count)

    def get_information(self) -> dict:
        return {'id': self.id,
                'name': self.name,
                'longname': self.longname,
                'description': self.description,
                'cost': self.cost,
                'category': self.category.name}



class ItemClassDynamic:
    def __init__(self,id: str, name: str, count: int=0):
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

    def set_count_list(self, *count):
        for count, dynamic in zip(count, self.dynamicContent.values()):
            dynamic.count = count

invCart = CartClass('INVB','invCart')
userCart = CartClass('USEB','userCart')

testCategory = CategoryClass('TESC','monty')

items = {'BE00': ItemClassStatic('BE00', 'beans', 1, testCategory),
         'EGG1': ItemClassStatic('EGG1', 'egg', 1, testCategory),
         'TOAD': ItemClassStatic('TOAD', 'toast', 100, testCategory),
         'SAM1': ItemClassStatic('SAM1', 'spam', 2, testCategory)}

categories = {'TESC': testCategory}

invCart.add_item_list(items)
userCart.add_item_list(items)

invCart.set_count_list(100, 120, 2931, 1)

class MainMenu(cmd.Cmd):
    def do_view(self, arg):
        """See everything in shop."""
        for i in items.keys():
            info = invCart.get_information(i)
            print(f"{info['count']}x | {info['name']} | {info['cost']} | {info['id']}")

    def do_start(self, arg):
        for i in categories.values():
            info = i.get_information()
            if info['description']:
                infodesc = info['description']
            else:
                infodesc = ''
            print(f"{info['id']} | {info['longname']} | {infodesc}")


    def do_move(self, arg):
        try:
            target, number = [str(s) for s in arg.split(',')]
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