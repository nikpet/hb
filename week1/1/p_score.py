from palindrome import palindrome as is_palindrome


def reverse(n):
    return int(str(n)[::-1])


def p_score(n):
    if is_palindrome(n):
        return 1
    else:
        return 1 + p_score(n + reverse(n))


if __name__ == '__main__':
    print(p_score(121))
    print(p_score(48))
    print(p_score(198))
