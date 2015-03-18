def sum_of_digits(n):
    string_of_n = str(n)
    result = 0
    if (n < 0):
        return 1
    for i in range(len(string_of_n)):
        result = result + int(string_of_n[i])
    return result

print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))
