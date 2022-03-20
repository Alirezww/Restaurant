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
