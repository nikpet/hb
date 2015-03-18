from factorial import factorial


def fact_digits(n):
    result = 0
    string_of_n = str(n)

    for i in range(len(string_of_n)):
        result = result + factorial(int(string_of_n[i]))

    return result

if __name__ == "__main__":
    print(fact_digits(111))
    print(fact_digits(145))
    print(fact_digits(999))
