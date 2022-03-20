# TODO : define class Table here
# TODO : write its sample classmethod here

import uuid


class Table:
    table_list = list()

    def __init__(self, capacity, number):
        self.uuid = uuid.uuid4()
        self.capacity = capacity
        self.number = number
        self.reserved = False
        self.is_available = True
        self.table_list.append(self)

    @classmethod
    def sample(cls):
        return cls(capacity=4, number=2)
