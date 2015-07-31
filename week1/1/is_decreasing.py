def is_decreasing(seq):
    start = seq.pop(0)
    while seq:
        next = seq.pop(0)
        if start <= next:
            return False
        start = next
    return True


if __name__ == '__main__':
    print(is_decreasing([5, 4, 3, 2, 1]))
    print(is_decreasing([1, 2, 3]))
    print(is_decreasing([100, 50, 20]))
    print(is_decreasing([1, 1, 1, 1]))
