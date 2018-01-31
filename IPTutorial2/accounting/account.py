class Account(object):
    name = ""
    balance = None

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def income(self, income):
        self.balance = self.balance + income

    def expenses(self, expenses):
        self.balance = self.balance - expenses

    def get_balance(self):
        return self.balance
