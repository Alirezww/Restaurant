# TODO : define class Item here
# TODO : write sample classmethod here
import uuid
from datetime import datetime


class Item:
    item_count = 0
    Food_list = list()
    Beverage_list = list()
    Starter_list = list()

    def __init__(self, name, type, price):
        self.item_id = self.get_item_id()
        self.uuid = uuid.uuid4()
        self.datetime = datetime.now()
        self.name = name
        self.type = type
        self.price = price

        if self.type.lower() == 'starter':
            self.Starter_list.append(self)
        elif self.type.lower() == 'beverage':
            self.Beverage_list.append(self)
        else:
            self.Food_list.append(self)

    def get_item_id(self):
        self.item_id += 1
        return self.item_count

    @classmethod
    def search(cls, uuid):
        item_list = [*cls.Food_list, *cls.Starter_list, *cls.Beverage_list]
        for item in item_list:
            if item.uuid == uuid:
                return item
            return None

    @classmethod
    def sample(cls):
        return cls(price='1200', type='Food', name='pizza')
