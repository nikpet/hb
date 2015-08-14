def encrypt(num):
    # Make num between 0 and 26
    num = num % 26

    def encryptor(func):
        def func_wrapper():
            alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            cipher = ''
            for c in func():
                if c in alphabet:
                    cipher += alphabet[(alphabet.index(c) + num) % len(alphabet)]
                elif c == ' ':
                    cipher += ' '
            return cipher
        return func_wrapper
    return encryptor


@encrypt(26)
def get_low():
    return "Get get get low"


if __name__ == '__main__':
    print(get_low())
