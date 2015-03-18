def count_substrings(heystack, needle):
    return count(heystack, needle)


def count(heystack, needle, count_of_needle=0):
    if needle not in heystack:
        return count_of_needle
    else:
        index = heystack.index(needle)
        count_of_needle += 1
        return count(heystack[index + len(needle):], needle, count_of_needle)

if __name__ == '__main__':
    print(count_substrings("This is a test string", "is"))
    print(count_substrings("babababa", "baba"))
    print(count_substrings("""Python is an awesome language
        to program in!""", "o"))
    print(count_substrings("We have nothing in common!", "really?"))
    print(count_substrings("This is this and that is this", "this"))
