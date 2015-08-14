def chain(iterable_one, iterable_two):
    for item in iterable_one:
        yield item
    for item in iterable_two:
        yield item


if __name__ == '__main__':
    print(list(chain(range(0, 4), range(4, 8))))
