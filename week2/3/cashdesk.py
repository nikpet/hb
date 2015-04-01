class Bill:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amont)


class BillBatch:
    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self, bills)

    def total(self):
        total_sum = 0
        for bill in self.bills:
            total_sum += int(bill)
        return total_sum

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:
    def __init__(self):
        self.bills = {}
        self.values = {}

    def take_money(self, money):
        if isinstance(money, Bill):
            self._add(money)
        else:
            for bill in money:
                self._add(bill)

    def _add(self, money):
        if money in self.bills:
            self.bills[money] += 1
            self.values[int(money)] += 1
        else:
            self.bills[money] = 1
            self.values[int(money)] = 1

    def test(self):
        return self.bills

    def total(self):
        return sum([x * y for x, y in self.values.items()])

    def inspect(self):
        print('We have a total of {}$ in the desk'.format(self.total()))
        print('We have the following count of bills, sorted in ascending order:')
        bills_list = [[x, y] for x, y in self.values.items()]
        for item in sorted(bills_list):
            print("{}$ bills - {}".format(str(item[0]), str(item[1])))

########################################
# values = [10, 20, 50, 100, 100, 100]
# bills = [Bill(value) for value in values]
#
# batch = BillBatch(bills)
#
# desk = CashDesk()
#
# desk.take_money(batch)
# desk.take_money(Bill(10))
# print(desk.total())
# desk.inspect()
########################################
# values = [10, 20, 50, 100]
# bills = [Bill(value) for value in values]
#
# batch = BillBatch(bills)
#
# for bill in batch:
#     print(bill)
########################################
# a = Bill(10)
# b = Bill(5)
# c = Bill(10)
#
# print(int(a) == 10)
# print(str(a) == 'A 10$ bill')
# print(a)
# print(a == b)
# print(a == c)
# money_holder = {}
# money_holder[a] = 1
# if c in money_holder:
#     money_holder[c] += 1
# print(money_holder)
########################################
