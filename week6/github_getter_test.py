import unittest
from github_getter import GithubGetter


class GithubGetterTest(unittest.TestCase):
    def setUp(self):
        self.getter = GithubGetter()

    def test_client_and_secret_are_set(self):
        # should be remove in production
        self.assertGreater(len(self.getter.client), 5)
        self.assertGreater(len(self.getter.secret), 5)

if __name__ == '__main__':
    unittest.main()
