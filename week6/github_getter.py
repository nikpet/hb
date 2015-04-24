import requests
from directed_graph import DirectedGraph
import pprint
# import gzip
# import json


class GithubGetter:

    def __init__(self):
        with open('credential.txt', 'r') as fd:
            self.client, self.secret = [l.rstrip() for l in fd]
        self.uri = "https://api.github.com/users/{}/{}"
        self.uri += "?client_id=" + self.client
        self.uri += "&client_secret=" + self.secret
        self.headers = {'Accept': 'application/json',
                        'Accept-encoding': 'utf-8'}
        self.graph = DirectedGraph()

    def get(self, action, user):
        if action not in ['followers', 'following']:
            raise ValueError
        json_data = requests.get(self.uri.format(user, action),
                                 headers=self.headers).json()
        # json_data = json_data.json()
        users_doing_action = []
        for actionist in json_data:
            users_doing_action.append(actionist['login'])
        return users_doing_action

    def build_network(self, starting_user, level):
        visited = {starting_user}
        queue = [(0, starting_user)]
        while len(queue) > 0:
            current_level, current_user = queue.pop(0)
            if current_level >= level:
                break
            for user in self.get('following', current_user):
                self.graph.add_edge(current_user, user)
                if user not in visited:
                    visited.add(user)
                    queue.append((current_level + 1, user))
        visited = {starting_user}
        queue = [(0, starting_user)]
        while len(queue) > 0:
            current_level, current_user = queue.pop(0)
            if current_level >= level:
                break
            for user in self.get('followers', current_user):
                self.graph.add_edge(user, current_user)
                if user not in visited:
                    visited.add(user)
                    queue.append((current_level + 1, user))
        return self.graph

if __name__ == '__main__':
    f = GithubGetter()
    p = pprint.PrettyPrinter(indent=2)
    p.pprint(f.build_network('nikpet', 2).graph)
