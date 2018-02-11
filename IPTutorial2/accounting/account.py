class Account(object):

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance  # type: float

    def add_transaction(self, income):
        self.balance = self.balance + income

    def get_balance(self):
        return self.balance
