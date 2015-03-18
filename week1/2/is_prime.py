def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in divisors(n):
        if n % i == 0:
            return False
        else:
            return True


def divisors(number):
    if number < 0:
        div_range = range(-2, number, -1)
    else:
        div_range = range(2, number)
    return div_range


if __name__ == '__main__':
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(8))
    print(is_prime(11))
    print(is_prime(-10))
