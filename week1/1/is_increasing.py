def is_increasing(seq):
    start = seq.pop(0)
    while seq:
        next = seq.pop(0)
        if start >= next:
            return False
        start = next
    return True


if __name__ == '__main__':
    print(is_increasing([1, 2, 3, 4, 5]))
    print(is_increasing([1]))
    print(is_increasing([5, 6, -10]))
    print(is_increasing([1, 1, 1, 1]))
