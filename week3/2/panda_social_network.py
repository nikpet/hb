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
        pass
