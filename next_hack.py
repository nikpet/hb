from palindrome import palindrome


def is_hack_number(n):
    if palindrome(to_bin(n)) and str(to_bin(n)).count('1') % 2 != 0:
        return True
    return False


def next_hack(n):
    if is_hack_number(n):
        print(n)
    else:
        n = n + 1
        next_hack(n)


def to_bin(n):
    return int(bin(n)[2:])


if __name__ == '__main__':
    # print(is_hack_number(21))
    next_hack(0)
    next_hack(10)
    # 8031 is hack number
    # 8032 gives 8191
    next_hack(8032)
