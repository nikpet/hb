class BankAccount:
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.actions_list = ['Account was created']

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self.actions_list.append('Deposited ' + str(amount) + self.currency)
        self.balance += amount

    def get_balance(self):
        return self.balance

    def withdraw(self, ammount):
        if self.balance - ammount > 0:
            self.balance -= ammount
            return True
        else:
            return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        return self.balance

    def transfer_to(self, account, ammount):
        return account.currency == self.currency
