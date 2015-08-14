def chain(iterable_one, iterable_two):
    return list(iterable_one) + list(iterable_two)


if __name__ == '__main__':
    print(list(chain(range(0, 4), range(4, 8))))
