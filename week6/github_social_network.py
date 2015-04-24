from github_getter import GithubGetter


class GithubSocialNetwork:
    def __init__(self, user, level):
        self.user = user
        self.network = GithubGetter().build_network(user, level)

    def do_you_follow(self, user):
        return user in self.network.get_neighbors_for(self.user)

    def do_you_follow_indirectly(self, user):
        return self.network.path_between(self.user, user)

    def does_he_she_follows(self, user):
        return self.user in self.network.get_neighbors_for(user)

    def does_he_she_follows_indirectly(self, user):
        return self.network.path_between(user, self.user)

    def who_follows_you_back(self):
        return [x for x in self.network.get_neighbors_for(self.user)
                if self.network.path_between(x, self.user)]


if __name__ == '__main__':
    n = GithubSocialNetwork('presianbg', 1)
    print(n.network.graph)
    # print(n.who_follows_you_back())
