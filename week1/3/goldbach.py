# Copied from solutins.py
def is_prime(n):
    if n <= 1:
        return False

    start = 2

    while start < n:
        if n % start == 0:
            return False

        start += 1

    return True


# Copied from solutions.py
def next_prime(n):
    n += 1

    while not is_prime(n):
        n += 1

    return n


def goldbach(n):
    i = j = 2
    result = []
    while i < n:
        j = i
        while j < n:
            if i + j == n:
                result.append((i, j))
            j = next_prime(j)
        i = next_prime(i)
    return result

if __name__ == '__main__':
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(100))
