# TODO : define class Bill and Payment here
# TODO : write their sample classmethod here

import uuid


class Bill:
    def __init__(self, total_price, payment):
        self.uuid = uuid.uuid4()
        self.total_price = total_price
        self.payment = payment

    @classmethod
    def sample(cls):
        return cls(total_price='1200', payment='cash')
