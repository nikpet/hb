import unittest
from panda_social_netword import PandaSocialNetwork
from panda import Panda, PandaAlreadyThere


class PandaSocialNetworkTest(unittest.TestCase):
    def setUp(self):
        self.network = PandaSocialNetwork()
        self.panda = Panda('name', 'e@mail.cc', 'male')

    def _female_panda(self):
        return Panda('name', 'm@ail.cc', 'female')

    def test_init(self):
        self.assertEqual(self.network.network, {})

    def test_add_panda(self):
        self.network.add_panda(self.panda)
        self.assertEqual(self.network.network, {self.panda: []})
        with(self.assertRaises(PandaAlreadyThere)):
                self.network.add_panda(self.panda)

    def test_has_panda(self):
        new_panda = self._female_panda()
        self.network.add_panda(self.panda)
        self.assertTrue(self.network.has_panda(self.panda))
        self.assertFalse(self.network.has_panda(new_panda))

    def test_make_friends(self):
        new_panda = self._female_panda()
        self.network.add_friends(self.panda, new_panda)
        self.assertEqual(self.network.network,
                        {self.panda:[new_panda],
                         new_panda:[self.panda]})

    def test_are_friends(self):
        new_panda = self._female_panda()
        panda3 = Panda('n', 's@s.s', 'male')
        self.network.add_friends(self.panda, new_panda)
        self.assertTrue(self.network.are_friends(self.panda, new_panda))
        self.assertFalse(self.network.are_friends(self.panda, panda3))

    def test_friends_of(self):
        new_panda = self._female_panda()
        panda3 = Panda('n', 's@s.s', 'male')
        self.network.add_friends(self.panda, new_panda)
        self.assertEqual(self.network.friends_of(self.panda),
                        [new_panda])
        self.assertFalse(self.network.friends_of(panda3))




if __name__ == '__main__':
    unittest.main()
