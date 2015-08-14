def cycle(iterable):
    result = ''
    while True:
        for item in iterable:
            result += str(item)
            yield result

if __name__ == '__main__':
    endless = cycle(range(0, 10))
    for item in endless:
        print(item)
