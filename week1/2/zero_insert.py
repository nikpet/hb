def zero_insert(n):
    string_n = str(n)
    result = ''
    for i in range(len(string_n) - 1):
        same_result = same(string_n[i:i+2])
        modulo_ten_result = modulo_ten(string_n[i:i+2])
        if same_result:
            result += same_result
            continue
        if modulo_ten_result:
            result += modulo_ten_result
            continue
        result += string_n[i:i+1]
    return result + string_n[-1]


def same(string):
    if string[0] == string[1]:
        return string[0] + '0'
    else:
        return False


def modulo_ten(string):
    if (int(string[0]) + int(string[1])) % 10 == 0:
        return string[0] + '0'
    else:
        return False


if __name__ == '__main__':
    print(zero_insert(116457))
    print(zero_insert(55555555))
    print(zero_insert(1))
    print(zero_insert(6446))
