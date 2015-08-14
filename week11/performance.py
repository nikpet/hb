from datetime import datetime
from time import sleep


def log(filename):
    def logger(func):

        def wrapper():
            start = datetime.now()
            result = func()
            end = datetime.now()
            timed = end - start
            fd = open(filename, 'a')
            fd.write(func.__name__ +
                     ' was called and took ' +
                     str(timed.seconds) +
                     '.' +
                     str(timed.microseconds) +
                     ' seconds to complete' +
                     '\n')
            fd.close()
            return result
        return wrapper
    return logger


@log('log.txt')
def something_heavy():
    sleep(2)
    return "I am done"


if __name__ == '__main__':
    print(something_heavy())
