# TODO : define class Order here
# TODO : write its sample classmethod here
import uuid


class Order:
    def __init__(self, in_out, bill, table):
        self.uuid = uuid.uuid4()
        self.items_dict = dict()
        self.in_out = in_out
        self.bill = bill
        self.table = table

    @classmethod
    def sample(cls):
        return cls(in_out='out', bill='bill', table='table')
