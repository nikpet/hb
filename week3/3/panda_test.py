import unittest
from panda import Panda


class PandaTest(unittest.TestCase):
    def setUp(self):
        self.panda = Panda("name", "e@mail.com", "male")
        self.female_panda = Panda("name", "e@mail.com", "female")

    def test_init(self):
        self.assertEqual(self.panda.name, "name")
        self.assertEqual(self.panda.email, "e@mail.com")
        self.assertEqual(self.panda.sex, "male")
        with self.assertRaises(ValueError):
            Panda("name", "notEmail", "mail")

    def test_is_male(self):
        self.assertTrue(self.panda.is_male())
        self.assertFalse(self.panda.is_female())
        self.assertTrue(self.female_panda.is_female())
        self.assertFalse(self.female_panda.is_male())

    def test_eq(self):
        other_panda = Panda("name", "e@mail.com", "male")
        self.assertTrue(self.panda == other_panda)

    def test_hash(self):
        self.assertEqual(hash(self.panda),
                        hash((self.panda.name, self.panda.email, self.panda.sex)))


if __name__ == '__main__':
    unittest.main()
