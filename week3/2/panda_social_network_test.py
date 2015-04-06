import unittest
from panda_social_network import PandaSocialNetwork
from panda import Panda, PandaAlreadyThere


class PandaSocialNetworkTest(unittest.TestCase):
    def setUp(self):
        self.network = PandaSocialNetwork()
        self.panda = Panda('name', 'e@mail.cc', 'male')

    def _new_panda(self, index):
        return Panda('name' + str(index), 'm@ail.cc', 'female')

    def _new_male_panda(self, index):
        return Panda('name' + str(index), 'm@ail.cc', 'male')

    def test_init(self):
        self.assertEqual(self.network.network, {})

    def test_add_panda(self):
        self.network.add_panda(self.panda)
        self.assertEqual(self.network.network, {self.panda: []})
        with(self.assertRaises(PandaAlreadyThere)):
                self.network.add_panda(self.panda)

    def test_has_panda(self):
        panda2 = self._new_panda(1)
        self.network.add_panda(self.panda)
        self.assertTrue(self.network.has_panda(self.panda))
        self.assertFalse(self.network.has_panda(panda2))

    def test_make_friends(self):
        panda2 = self._new_panda(1)
        self.network.add_friends(self.panda, panda2)
        self.assertEqual(self.network.network,
                         {self.panda: [panda2],
                          panda2: [self.panda]})

    def test_are_friends(self):
        panda2 = self._new_panda(1)
        panda3 = self._new_panda(2)
        self.network.add_friends(self.panda, panda2)
        self.assertTrue(self.network.are_friends(self.panda, panda2))
        self.assertFalse(self.network.are_friends(self.panda, panda3))

    def test_friends_of(self):
        panda2 = self._new_panda(1)
        panda3 = self._new_panda(2)
        self.network.add_friends(self.panda, panda2)
        self.assertEqual(self.network.friends_of(self.panda),
                         [panda2])
        self.assertFalse(self.network.friends_of(panda3))

    def test_connection_level(self):
        panda2 = self._new_panda(1)
        panda3 = self._new_panda(2)
        panda4 = self._new_panda(3)
        panda5 = self._new_panda(4)
        self.network.add_friends(self.panda, panda2)
        self.network.add_friends(panda2, panda3)
        self.network.add_friends(panda3, panda4)
        self.network.add_panda(panda5)
        self.assertEqual(self.network.connection_level(self.panda, panda5), 0)
        self.assertEqual(self.network.connection_level(self.panda, panda4), 3)

    def test_are_connected(self):
        panda2 = self._new_panda(1)
        panda3 = self._new_panda(2)
        panda4 = self._new_panda(3)
        panda5 = self._new_panda(4)
        self.network.add_friends(self.panda, panda2)
        self.network.add_friends(panda2, panda3)
        self.network.add_friends(panda3, panda4)
        self.assertTrue(self.network.are_connected(self.panda, panda4))
        self.assertFalse(self.network.are_connected(self.panda, panda5))

    def test_gender_in_level(self):
        panda2 = self._new_panda(1)
        panda3 = self._new_panda(2)
        panda4 = self._new_panda(3)
        panda5 = self._new_panda(4)
        panda6 = self._new_panda(5)
        panda7 = self._new_panda(6)
        panda8 = self._new_male_panda(7)
        panda9 = self._new_male_panda(8)
        self.network.add_friends(self.panda, panda2)
        self.network.add_friends(panda2, panda3)
        self.network.add_friends(panda2, panda6)
        self.network.add_friends(panda2, panda7)
        self.network.add_friends(panda3, panda4)
        self.network.add_friends(panda4, panda5)
        self.network.add_friends(self.panda, panda8)
        self.network.add_friends(panda7, panda9)
        self.assertEqual(self.network.how_many_gender_in_network(1, self.panda, 'female'), 1)
        self.assertEqual(self.network.how_many_gender_in_network(2, self.panda, 'female'), 4)
        self.assertEqual(self.network.how_many_gender_in_network(3, self.panda, 'female'), 5)
        self.assertEqual(self.network.how_many_gender_in_network(1, self.panda, 'male'), 2)
        self.assertEqual(self.network.how_many_gender_in_network(4, self.panda, 'male'), 3)


if __name__ == '__main__':
    unittest.main()
