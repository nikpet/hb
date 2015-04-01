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
        self.actions_list.append('Balance check -> ' + str(self.balance) + self.currency)
        return self.balance

    def withdraw(self, ammount):
        if self.balance - ammount > 0:
            self.balance -= ammount
            self.actions_list.append(str(ammount) + self.currency + ' was withdrawed')
            return True
        else:
            self.actions_list.append('Withdraw for {}$ failed.'.format(ammount))
            return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        self.actions_list.append('__int__ check -> ' + str(self.balance) + self.currency)
        return self.balance

    def transfer_to(self, account, ammount):
        result = account.currency == self.currency
        if result:
            self.actions_list.append('Transfer to {} for {}{}'.format(account.name, ammount, self.currency))
            account.actions_list.append('Transfer from {} for {}{}'.format(self.name, ammount, self.currency))
        return result

    def history(self):
       return self.actions_list 
