def prime_factorization(n):
    global primes
    primes = []
    # list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
    #                   47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    result = calculate(n)
    while True:
        if result == 1:
            break
        result = calculate(result)
    # return dict_to_list(times_to_powers(primes))
    return list(times_to_powers(primes).items())


def calculate(n):
    global primes
    list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                      47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    for i in list_of_primes:
        if is_factor(n, i):
            primes.append(i)
            return n // i


def is_factor(n, prime):
    return n % prime == 0


def times_to_powers(arr):
    times = {}
    for i in arr:
        if i in times:
            times[i] += 1
        else:
            times[i] = 1
    return times


if __name__ == '__main__':
    print(prime_factorization(10))
    print(prime_factorization(14))
    print(prime_factorization(356))
    print(prime_factorization(89))
    print(prime_factorization(1000))
