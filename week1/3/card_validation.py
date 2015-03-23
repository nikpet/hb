def is_credit_card_valid(number):
    str_num = str(number)
    if len(str_num) % 2 == 0:
        return False
    new_num = str_num[::2]
    for i in str_num[1::2]:
        new_num += str(int(i) * 2)
    sum_of_num = 0
    for i in new_num:
        sum_of_num += int(i)
    if sum_of_num % 10 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_credit_card_valid(79927398713))
    print(is_credit_card_valid(79927398715))
