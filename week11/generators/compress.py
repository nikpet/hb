def compress(iterable, mask):
    if len(iterable) != len(mask):
        raise ValueError
    for i in range(len(iterable)):
        if mask[i]:
            yield iterable[i]


if __name__ == '__main__':
    print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
