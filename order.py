# TODO : define class Order here
# TODO : write its sample classmethod here
import uuid
from datetime import datetime
from khayyam import JalaliDatetime


class Order:
    def __init__(self, in_out, bill, table):
        self.uuid = uuid.uuid4()
        self.items_dict = dict()
        self.in_out = in_out
        self.datetime = datetime.now()
        self.bill = bill
        self.table = table

    @classmethod
    def sample(cls):
        return cls(in_out='out', bill='bill', table='table')

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime)
