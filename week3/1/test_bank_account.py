import unittest
from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.name = 'Name'
        self.balance = 50
        self.currency = '$'
        self.bank_account = BankAccount(self.name, self.balance, self.currency)

    def test_init__(self):
        self.assertTrue(isinstance(self.bank_account, BankAccount))

    def test_init_name(self):
        self.assertEqual(self.bank_account.name, self.name)

    def test_init_balance(self):
        self.assertEqual(self.bank_account.balance, self.balance)

    def test_init_currency(self):
        self.assertEqual(self.bank_account.currency, self.currency)

    def test_deposit_money(self):
        self.bank_account.deposit(self.balance)
        self.assertEqual(self.bank_account.balance, self.balance * 2)

    def test_deposit_negative_money(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-50)

    def test_get_balance(self):
        self.assertEqual(self.bank_account.get_balance(), self.balance)

    def test_withdraw_successfull(self):
        self.assertTrue(self.bank_account.withdraw(20))

    def test_withdraw_fail(self):
        self.assertFalse(self.bank_account.withdraw(100))

    def test_stringify(self):
        bank_account_string = "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)
        self.assertEqual(str(self.bank_account), bank_account_string)

    def test_int(self):
        self.assertEqual(int(self.bank_account), self.balance)

    def test_transfer_money_success(self):
        second_account = BankAccount('second', 100, '$')
        self.assertTrue(self.bank_account.transfer_to(second_account, 50))

    def test_transfer_money_fails(self):
        second_account = BankAccount('second', 100, 'E')
        self.assertFalse(self.bank_account.transfer_to(second_account, 50))

    def test_history_init_message(self):
        self.assertIn('Account was created', self.bank_account.actions_list)

    def test_history_deposited(self):
        deposited_ammount = 100
        self.bank_account.deposit(deposited_ammount)
        self.assertIn('Deposited 100$', self.bank_account.actions_list)

if __name__ == '__main__':
    unittest.main()
