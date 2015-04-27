import unittest
from histogram import Histogram


class HistogramTest(unittest.TestCase):
    def setUp(self):
        self.histogram = Histogram()

    def test_add(self):
        self.histogram.add('apache')
        self.histogram.add('apache')
        self.histogram.add('nginx')
        self.assertEqual(self.histogram.vault['apache'], 2)
        self.assertEqual(self.histogram.vault['nginx'], 1)

    def test_count(self):
        self.histogram.add('apache')
        self.histogram.add('apache')
        self.histogram.add('nginx')
        self.assertEqual(self.histogram.count('apache'), 2)
        self.assertEqual(self.histogram.count('nginx'), 1)
        self.assertIsNone(self.histogram.count('iis'))


if __name__ == '__main__':
    unittest.main()
