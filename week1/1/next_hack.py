from palindrome import palindrome as is_palindrome


def is_hack_number(n):
    if is_palindrome(to_bin(n)) and str(to_bin(n)).count('1') % 2 != 0:
        return True
    return False


def next_hack(n):
    n = n + 1
    if is_hack_number(n):
        return n
    return next_hack(n)
    # if is_hack_number(n + 1):
    #     return n + 1
    # return next_hack(n + 1)


def to_bin(n):
    return int(bin(n)[2:])


if __name__ == '__main__':
    print(next_hack(0))
    print(next_hack(10))
    print(next_hack(8031))
