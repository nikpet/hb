def fibonacci(n):
    result = [1]
    for i in range(n - 1):
        if len(result) > 1:
            result.append(result[i-1] + result[i])
        else:
            result.append(1)
    print(result)
fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(10)
