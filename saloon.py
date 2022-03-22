# TODO : define class Table here
# TODO : write its sample classmethod here

import uuid


class Table:
    table_list = list()

    def __init__(self, number, capacity, reserved, is_available):
        self.uuid = uuid.uuid4()
        self.capacity = capacity
        self.number = number
        self.reserved = reserved
        self.is_available = is_available
        self.table_list.append(self)

    @classmethod
    def sample(cls):
        return cls(number=2, capacity=4)

    def serialize(self):
        data = self.__dict__
        data.pop('uuid')
        return data

    @classmethod
    def prompt(cls):
        number = int(input('PLease enter table number : '))
        capacity = input('PLease enter table capacity : ')
        result = {
            'number': number,
            'capacity': capacity
        }
        return result

    @classmethod
    def search(cls, number):
        for table in cls.table_list:
            if number == int(table.number):
                return table
            return None

    @classmethod
    def search_assigning(cls, number):
        table = Table.search(number)
        if table and table.reserved == False and table.is_available == True:
            table.reserved = True
            table.is_available = False
            return table
        return False
