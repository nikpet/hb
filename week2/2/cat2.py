import sys


def main():
    file_names = sys.argv[1:]
    contents = []
    for file in file_names:
        file_handler = open(file, "r")
        contents.append(file_handler.read())
        file_handler.close()
    return "\n".join(contents)

if __name__ == '__main__':
    print(main())
