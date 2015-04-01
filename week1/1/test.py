import unittest
from char_histogram import char_histogram


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_char_histogram(self):
        self.assertEqual(char_histogram('Python!'), {'P': 1, 'y': 1, 't': 1,
                                                     'h': 1, 'o': 1, 'n': 1,
                                                     '!': 1})
        self.assertEqual(char_histogram('AAAAaaa!!!'), {'A': 4, 'a': 3, '!': 3})


if __name__ == '__main__':
    unittest.main()
