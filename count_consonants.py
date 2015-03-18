def count_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxz'
    count = 0
    for letter in string.lower():
        if letter in consonants:
            count = count + 1
    return count


if __name__ == '__main__':
    print(count_consonants("Python"))
    print(count_consonants("Theistareykjarbunga"))
    print(count_consonants("grrrrgh!"))
    print(count_consonants("""Github is the second best thing that happend
        to programmers, after the keyboard!"""))
    print(count_consonants("A nice day to code!"))
