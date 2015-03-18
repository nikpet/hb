def sum_of_divisors(n):
    result = 0
    for i in divisors(n):
        result += i
    return result


def divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    print(sum_of_divisors(8))
    print(sum_of_divisors(7))
    print(sum_of_divisors(1))
    print(sum_of_divisors(1000))
