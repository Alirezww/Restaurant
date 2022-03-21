# TODO : define class Item here
# TODO : write sample classmethod here
import uuid
from datetime import datetime
from khayyam import JalaliDatetime
from constanst import MENU_TYPE


class Item:
    item_count = 0
    Food_list = list()
    Beverage_list = list()
    Starter_list = list()
    item_list = [*Food_list, *Starter_list, *Beverage_list]

    def __init__(self, name, type, price):
        self.item_id = self.get_item_id()
        self.uuid = uuid.uuid4()
        self.datetime = datetime.now()
        self.name = name
        self.type = type
        self.price = price

        if self.type.lower() == MENU_TYPE[1].lower():
            self.Starter_list.append(self)
        elif self.type.lower() == MENU_TYPE[2].lower():
            self.Beverage_list.append(self)
        else:
            self.Food_list.append(self)

    def get_item_id(self):
        self.item_id += 1
        return self.item_count

    @classmethod
    def search(cls, uuid=None, item_id=None):
        item_list = [*cls.Food_list, *cls.Starter_list, *cls.Beverage_list]

        id_temp = uuid
        if id_temp is None:
            id_temp = item_id

        for item in item_list:
            if id_temp in getattr(item, id_temp):
                return item
            return None

    @classmethod
    def sample(cls):
        return cls(price='1200', type='Food', name='pizza')

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime)

    @classmethod
    def prompt(cls):
        name = input("please enter foods'name : ")
        price = input("please enter foods'price : ")
        type = input("please enter foods'type : ")
        result = {
            'name': name,
            'price': price,
            'type': type
        }
        return result

    def serialize(self):
        data = self.__dict__
        return data
