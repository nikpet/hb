def prepare_meal(number):
    n = 1
    max_num = 0
    while True:
        egg = 3**n
        if number % egg == 0:
            max_num = n
        if number / egg < 1:
            break
        n += 1
    spam = ''
    # print('max ', max_num)
    if number % 5 == 0:
        if max_num == 0:
            spam = 'eggs'
        else:
            spam = 'and eggs'
    else:
        spam = ''
    return 'spam ' * max_num + spam


if __name__ == '__main__':
    print(prepare_meal(3))
    print(prepare_meal(27))
    print(prepare_meal(7))
    print(prepare_meal(5))
    print(prepare_meal(15))
    print(prepare_meal(45))
