from fibonacci import fibonacci


def fib_number(n):
    result = ''
    for i in fibonacci(n):
        result = result + str(i)
    return int(result)

if __name__ == '__main__':
    print(fib_number(3))
    print(fib_number(10))
