# TODO : define class Table here
# TODO : write its sample classmethod here

import uuid


class Table:
    table_list = list()

    def __init__(self, capacity, number, reserved):
        self.uuid = uuid.uuid4()
        self.capacity = capacity
        self.number = number
        self.reserved = reserved
        self.is_available = True

    @classmethod
    def sample(cls):
        return cls(capacity=4, number=2, reserved=False)
