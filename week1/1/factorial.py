def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)
    # result = 1
    # for i in range(1, n + 1):
    #     result = result * i
    # return result
if __name__ == "__main__":
    print(factorial(0))
    print(factorial(1))
    print(factorial(5))
