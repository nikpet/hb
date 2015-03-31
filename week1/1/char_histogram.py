def char_histogram(string):
    histogram = {}
    for letter in string:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram

if __name__ == '__main__':
    print(char_histogram("Python!"))
    print(char_histogram("AAAAaaa!!!"))
