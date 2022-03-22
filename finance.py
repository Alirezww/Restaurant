# TODO : define class Bill and Payment here
# TODO : write their sample classmethod here

import uuid
from datetime import datetime
from khayyam import JalaliDatetime


class Bill:
    def __init__(self, total_price):
        self.uuid = uuid.uuid4()
        self.total_price = total_price
        self.payment = self.create_payment()

    @classmethod
    def sample(cls):
        return cls(total_price='1200')

    def create_payment(self):
        payment_data = Payment.prompt()
        payment = Payment(**payment_data, price=self.total_price)
        return payment


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

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime)

    @classmethod
    def prompt(cls):
        payment_type = input('Please enter your payment type : ')
        result = {
            'payment_type': payment_type
        }
        return result
