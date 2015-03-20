def groupby(func, seq):
    result = {}
    for i in seq:
        if func(i) in result:
            result[func(i)].append(i)
        else:
            result[func(i)] = [i]
    return result


if __name__ == '__main__':
    print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
    print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
    print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
