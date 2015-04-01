from panda import PandaAlreadyThere


class PandaSocialNetwork:
    def __init__(self):
        self.network = {}

    def add_panda(self, panda):
        if panda in self.network:
            raise PandaAlreadyThere
        self.network[panda] = []

    def has_panda(self, panda):
        return panda in self.network

    def add_friends(self, panda1, panda2):
        if panda1 not in self.network:
            self.add_panda(panda1)
        if panda2 not in self.network:
            self.add_panda(panda2)
        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if not (self.has_panda(panda1) and self.has_panda(panda2)):
            return False
        if panda1 in self.network[panda2]:
            return True
        return False

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self.network[panda]

