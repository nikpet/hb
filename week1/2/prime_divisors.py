from sum_of_divisors import divisors
from is_prime import is_prime


def prime_number_of_divisor(n):
    return is_prime(len(divisors(n)))

if __name__ == '__main__':
    print(prime_number_of_divisor(7))
    print(prime_number_of_divisor(8))
    print(prime_number_of_divisor(9))
