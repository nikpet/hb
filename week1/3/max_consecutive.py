from group import group


def max_consecutive(items):
    max_len = 0
    for i in group(items):
        if max_len < len(i):
            max_len = len(i)
    return max_len


if __name__ == '__main__':
    print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
    print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
