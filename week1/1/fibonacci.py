def fibonacci(n):
    result = [1, 1]
    for i in range(1, n-1):
        result.append(result[i-1] + result[i])
    return result[:n]
if __name__ == "__main__":
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(10))
