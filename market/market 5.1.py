
import csv

class Category:
    def __init__(self, id: str, name: str, longname: str=False):
        self.id = id
        self.name = name
        if longname:
            self.longname = longname
        else:
            self.longname = name
        self.description = None
        self.content = {}

    def get_self_info(self) -> dict:
        return {'id': self.id,
                'name': self.name,
                'longname': self.longname,
                'description': self.description,
                'contentkeys': self.content.keys()}

    def get_content_info(self, target) -> dict:
        return self.content[target].get_self_info()


class ItemData:
    """Contains Shared Data"""
    def __init__(self, id: str, name: str, cost: float, category: Category, longname: str = False):
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
        self.dynamic = {id: content for id, content in zip(itemdata.keys(), itemdata.values.create_dynamic_instance())}

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

def csvimport() -> None:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        print(row)
    return None



