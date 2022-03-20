# TODO : define class Order here
# TODO : write its sample classmethod here
import uuid
from datetime import datetime
from khayyam import JalaliDatetime
from saloon import Table
from finance import Bill


class Order:
    def __init__(self, in_out, bill, table, items_dict):
        self.uuid = uuid.uuid4()
        self.items_dict = items_dict
        self.in_out = in_out
        self.datetime = datetime.now()
        self.bill = bill
        self.table = table

    @classmethod
    def sample(cls):
        return cls(in_out='out', bill=Bill.sample(), table=Table.sample(), items_dict={'123-123': 2})

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime)
