from panda import PandaAlreadyThere
from panda import Panda
import json


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
        if panda1 not in self.network[panda2]:
            self.network[panda2].append(panda1)
        if panda2 not in self.network[panda1]:
            self.network[panda1].append(panda2)

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

    # def _find_shortest_path(self, panda1, panda2, path=[]):
    #     path = path + [panda1]
    #     if panda1 == panda2:
    #         return path
    #     if panda1 not in self.network:
    #         return None
    #     shortest = None
    #     for node in self.network[panda1]:
    #         if node not in path:
    #             newpath = self._find_shortest_path(node, panda2, path)
    #             if newpath:
    #                 if not shortest or len(newpath) < len(shortest):
    #                     shortest = newpath
    #     return shortest

    def connection_level(self, panda1, panda2):
        path = {}
        path[panda1] = None
        queue = [panda1]
        visited = {panda1}
        found = False
        level = 0

        while len(queue) > 0:
            current = queue.pop(0)
            visited.add(current)
            if current == panda2:
                found = True
                break
            for item in self.network[current]:
                if item not in visited:
                    path[item] = current
                    visited.add(item)
                    queue.append(item)
        if found:
            while path[panda2] is not None:
                panda2 = path[panda2]
                level += 1
        return level

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) > 0:
            return True
        else:
            return False

    def how_many_gender_in_network(self, level, panda, gender):
        queue = [panda]
        visited = {panda}
        lvl = 0
        while len(queue) > 0:
            lvl += 1
            current = queue.pop(0)
            for friend in self.network[current]:
                if friend not in visited:
                    visited.add(friend)
                    if lvl < level:
                        queue.append(friend)
        count = 0
        for item in visited:
            if item.sex == gender:
                count += 1
        return count

    def serialize(self):
        serizlized = {}
        for item in self.network:
            serizlized[str(item)] = [str(x) for x in self.network[item]]

        return serizlized

    def save(self, filename):
        f = open(filename, "w")
        json.dump(self.serialize(), f)
        f.close()

    def load(self, filename):
        self.network = {}
        f = open(filename, "r")
        data = json.load(f)
        f.close()
        for item in data:
            for friend in data[item]:
                self.add_friends(item, friend)

    def _new_panda(self, index):
        return Panda('name' + str(index), 'm@ail.cc', 'female')

    def _new_male_panda(self, index):
        return Panda('name' + str(index), 'm@ail.cc', 'male')

if __name__ == '__main__':
    nn = PandaSocialNetwork()
    panda = nn._new_male_panda(0)
    panda2 = nn._new_panda(1)
    panda3 = nn._new_panda(2)
    panda4 = nn._new_panda(3)
    panda5 = nn._new_panda(4)
    panda6 = nn._new_panda(5)
    panda7 = nn._new_panda(6)
    panda8 = nn._new_male_panda(7)
    panda9 = nn._new_male_panda(8)
    nn.add_friends(panda, panda2)
    nn.add_friends(panda2, panda3)
    nn.add_friends(panda2, panda6)
    nn.add_friends(panda2, panda7)
    nn.add_friends(panda3, panda4)
    nn.add_friends(panda4, panda5)
    nn.add_friends(panda, panda8)
    nn.add_friends(panda7, panda9)
    nn.save("jjj.json")
    nn.load("jjj.json")
