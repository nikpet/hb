def to_digits(n):
    string_n = str(n)
    result = list()
    for i in string_n:
        result.append(int(i))
    return result

if __name__ == '__main__':
    print(to_digits(123))
    print(to_digits(99999))
    print(to_digits(123023))
