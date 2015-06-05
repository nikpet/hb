class Histogram:
    def __init__(self):
        self.vault = dict()

    def add(self, item):
        if item not in self.vault:
            self.vault[item] = 1
        else:
            self.vault[item] += 1
        return True

    def count(self, item):
        try:
            item_count = self.vault[item]
        except KeyError:
            return None
        return item_count

    def items(self):
        return self.vault.items()

    def get_dict(self):
        return self.vault


if __name__ == '__main__':
    h = Histogram()
    h.add('aa')
    print(h.count('aa'))
