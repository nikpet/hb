import unittest
from cashdesk import Bill


class BillTest(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(5)

    def test_init(self):
        self.assertEqual(self.bill.amount, 5)

    def test_stringify(self):
        self.assertEqual(str(self.bill), "A 5$ bill")

    def test_int(self):
        self.assertEqual(int(self.bill), 5)

    def test_eq(self):
        second_bill = Bill(5)
        self.assertEqual(self.bill, second_bill)


if __name__ == '__main__':
    unittest.main()
