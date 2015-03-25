import sys


def main():
    file_name = sys.argv[1]
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content

if __name__ == '__main__':
    print(main())
