def is_an_bn(word):
    if len(word) % 2 != 0:
        return False
    else:
        half_len = len(word) // 2
        if 'a' * half_len != word[:half_len]:
            return False
        elif 'b' * half_len != word[half_len:]:
            return False
        else:
            return True


if __name__ == '__main__':
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))
