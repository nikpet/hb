from palindrome import palindrome


def p_score(n):
    calculate(n, 0)


def calculate(n, score=0):
    if palindrome(n):
        score = score + 1
        print(score)
    else:
        score = score + 1
        reverse_number = str(n)[::-1]
        number = n + int(reverse_number)
        calculate(number, score)


if __name__ == '__main__':
    p_score(121)
    p_score(48)
    p_score(198)
