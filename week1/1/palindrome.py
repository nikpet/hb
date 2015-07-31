def palindrome(obj):
    str_obj = str(obj)
    return str_obj == str_obj[::-1]


if __name__ == "__main__":
    print(palindrome(121))
    print(palindrome("kapak"))
    print(palindrome("baba"))
