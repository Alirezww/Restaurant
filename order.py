# TODO : define class Order here
# TODO : write its sample classmethod here
import uuid
from datetime import datetime
from khayyam import JalaliDatetime
from finance import Bill


class Order:
    def __init__(self, in_out, items_dict, number_table):
        self.uuid = uuid.uuid4()
        self.items_dict = items_dict
        self.in_out = in_out
        self.datetime = datetime.now()
        self.bill = self.create_bill()
        self.table = self.assign_table(number_table)

    @classmethod
    def sample(cls):
        return cls(in_out='out', items_dict={'123-123': 2}, number_table=3)

    def assign_table(self, number):
        pass

    def create_bill(self):
        return Bill(self.total_price)

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime)

    @property
    def total_price(self):
        return 12000  # This is just test
