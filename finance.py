# TODO : define class Bill and Payment here
# TODO : write their sample classmethod here

import uuid
from datetime import datetime


class Bill:
    def __init__(self, total_price, payment):
        self.uuid = uuid.uuid4()
        self.total_price = total_price
        self.payment = payment

    @classmethod
    def sample(cls):
        return cls(total_price='1200', payment='cash')


class Payment:
    def __init__(self, payment_type, price):
        self.uuid = uuid.uuid4()
        self.datetime = datetime.now()
        self.is_paid = False
        self.payment_type = payment_type
        self.price = price

    @classmethod
    def sample(cls):
        return cls(payment_type='cash', price='12000')
