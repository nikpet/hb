from factorial import factorial


def fact_digits(n):
    if n < 10:
        return factorial(n)
    return fact_digits(n // 10) + factorial(n % 10)

if __name__ == "__main__":
    print(fact_digits(111))
    print(fact_digits(145))
    print(fact_digits(999))
