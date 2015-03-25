import sys
from random import randint


def main():
    numbers = []
    for i in range(int(sys.argv[2])):
        numbers.append(str(randint(1, 1000)))
    file = open(sys.argv[1], "w")
    file.write(" ".join(numbers))
    file.close()


if __name__ == '__main__':
    main()
