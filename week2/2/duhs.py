import sys
from os import listdir, path


def main():
    metrics = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    directory = sys.argv[1]
    file_list = listdir(directory)
    size = 0
    for file in file_list:
        size += path.getsize(directory + file)
    metric = 0
    print(size)
    while size // 1024 > 0:
        size = size / 1024
        metric += 1
    return directory + 'size is : ' + str(round(size)) + metrics[metric]


if __name__ == '__main__':
    print(main())
