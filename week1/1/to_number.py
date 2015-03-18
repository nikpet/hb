def to_number(digits):
    result = ''
    for i in digits:
        result = result + str(i)
    return int(result)


if __name__ == '__main__':
    print(to_number([1, 2, 3]))
    print(to_number([9, 9, 9, 9, 9]))
    print(to_number([1, 2, 3, 0, 2, 3]))
