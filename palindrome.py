def palindrome(obj):
    str_obj = str(obj)
    first_half = str_obj[:len(str_obj)//2]
    second_half = str_obj[len(str_obj)//2 + 1:]
    reverse_second_half = second_half[::-1]
    return first_half == reverse_second_half
if __name__ == "__main__":
    print(palindrome(121))
    print(palindrome("kapak"))
    print(palindrome("baba"))
