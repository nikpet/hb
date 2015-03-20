def unique_words_count(arr):
    words_seen = []
    unique_words = 0
    for word in arr:
        if word not in words_seen:
            words_seen.append(word)
            unique_words += 1
    return unique_words


if __name__ == '__main__':
    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))
    print(unique_words_count(["HELLO!"] * 10))
