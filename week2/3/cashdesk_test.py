import unittest
from cashdesk import CashDesk, Bill, BillBatch


class CashDeskTest(unittest.TestCase):
    def setUp(self):
        self.cashdesk = CashDesk()
        self.bill = Bill(5)
        self.batch = BillBatch([Bill(20), Bill(10)])

    def test_init(self):
        self.assertEqual(self.cashdesk.bills, {})

    def test_take_money(self):
        self.cashdesk.take_money(self.bill)
        self.cashdesk.take_money(self.batch)
        self.assertEqual(self.cashdesk.bills, {5: 1, 10: 1, 20: 1})

    def test_total(self):
        self.cashdesk.take_money(self.bill)
        self.cashdesk.take_money(self.batch)
        self.assertEqual(self.cashdesk.total(), 35)


if __name__ == '__main__':
    unittest.main()
