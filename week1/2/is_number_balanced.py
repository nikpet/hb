def is_number_balanced(n):
    string_n = str(n)
    middle = len(string_n) // 2
    if len(string_n) % 2 == 0:
        sum_second_half = sum([int(x) for x in string_n[middle:]])
    else:
        sum_second_half = sum([int(x) for x in string_n[middle + 1:]])
    sum_fist_half = sum([int(x) for x in string_n[:middle]])
    return sum_fist_half == sum_second_half


if __name__ == '__main__':
    print(is_number_balanced(9))
    print(is_number_balanced(11))
    print(is_number_balanced(13))
    print(is_number_balanced(121))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))
