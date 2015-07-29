def sum_of_digits(n):
    if n < 0:
        return 1
    if n < 10:
        return n
    return sum_of_digits(n // 10) + n % 10

print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))
