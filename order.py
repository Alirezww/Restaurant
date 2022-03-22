# TODO : define class Order here
# TODO : write its sample classmethod here
import uuid
from datetime import datetime
from khayyam import JalaliDatetime
from finance import Bill
from utils import calculate
from saloon import Table


class Order:
    order_list = []

    def __init__(self, in_out, items_dict, number_table):
        self.uuid = uuid.uuid4()
        self.items_dict = items_dict
        self.in_out = in_out
        self.datetime = datetime.now()
        self.bill = self.create_bill()
        self.table = self.assign_table(number_table)
        self.order_list.append(self)

    @classmethod
    def sample(cls):
        return cls(in_out='out', items_dict={'123-123': 2}, number_table=3)

    def assign_table(self, number):
        table = Table.search_assigning(number)
        return table

    def create_bill(self):
        return Bill(self.total_price)

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime)

    @property
    def total_price(self):
        return calculate(self.items_dict)

    @classmethod
    def create_order(cls, items_dict):
        order_date = cls.prompt()
        order = Order(**order_date, items_dict=items_dict)
        return order

    @classmethod
    def prompt(cls):
        in_out = input('Do you want to eat here or no ? (Enter in/out)')
        number_table = int(input('Please enter table number : '))
        result = {
            'in_out': in_out,
            'number_table': number_table
        }
        return result
