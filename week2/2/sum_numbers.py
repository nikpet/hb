import sys


def main():
    filename = sys.argv[1]
    file = open(filename, "r")
    content = file.read()
    file.close()
    content = ''.join(content.split(' '))
    sum = 0
    for i in content:
        sum += int(i)
    return sum


if __name__ == '__main__':
    print(main())
