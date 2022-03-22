from menu import Item
from saloon import Table


# Todo : define class Supervisor here
# TODO : write their sample classmethod


class Supervisor:
    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number

    @classmethod
    def sample(cls):
        return cls(
            username='alireza', password='1234', phone_number='9131271388'
        )

    @classmethod
    def create_item(cls):
        item_data = Item.prompt()
        if Item.search_by_name(item_data['name']) is None:
            item = Item(**item_data)
            return item
        return 'It is already satisfied.'

    @classmethod
    def item_data(cls):
        tmp = []
        for item in [*Item.Food_list, *Item.Beverage_list, *Item.Starter_list]:
            tmp.append(item.serialize())
        return tmp

    @classmethod
    def table_data(cls):
        tmp = []
        for table in Table.table_list:
            tmp.append(table.serialize())
        return tmp

    @classmethod
    def create_table(cls):
        table_data = Table.prompt()
        if Table.search(table_data['number']) is None:
            table = Table(**table_data)
            return table
        return 'it is already satisfied..'
