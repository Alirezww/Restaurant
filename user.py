from menu import Item


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
        if Item.search(item_data['uuid']) is None:
            item = Item(**item_data)
            return item
        return 'It is already satisfied.'

    @classmethod
    def item_data(cls):
        tmp = []
        for item in Item.item_list:
            tmp.append(item.serialize())
        return tmp