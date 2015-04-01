import unittest
from cashdesk import BillBatch, Bill


class BillBatchTest(unittest.TestCase):
    def setUp(self):
        self.bills = [Bill(x) for x in range(1, 5)]
        self.bill_batch = BillBatch(self.bills)

    def test_init(self):
        self.assertEqual(self.bill_batch.bills, self.bills)

    def test_len(self):
        self.assertEqual(len(self.bills), len(self.bill_batch))

    def test_total(self):
        self.assertEqual(sum(range(1, 5)), self.bill_batch.total())

    def test_get_item(self):
        self.assertEqual(self.bills[1], self.bill_batch[1])


if __name__ == '__main__':
    unittest.main()
