def count_vowels(string):
    vowels = 'aeiouy'
    count = 0
    for letter in string.lower():
        if letter in vowels:
            count = count + 1
    return count


if __name__ == '__main__':
    print(count_vowels("Python"))
    print(count_vowels("Theistareykjarbunga"))
    print(count_vowels("grrrrgh!"))
    print(count_vowels("""Github is the second best thing that happend
        to programmers, after the keyboard!"""))
    print(count_vowels("A nice day to code!"))
