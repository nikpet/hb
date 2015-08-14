def accepts(*args):
    def inner(func):
        def innerer(*func_args):
            for i in range(len(func_args)):
                if type(func_args[i]) is not args[i]:
                    raise TypeError('Argument {} of {} is not {}!'.format(
                        i + 1, func.__name__, args[i].__name__
                    ))
            return func(*func_args)
        return innerer
    return inner


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str)
def say_hello2(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

if __name__ == '__main__':
    print(say_hello("Hacker"))
    print(deposit("RadoRado", 10))
    print(say_hello(4))
