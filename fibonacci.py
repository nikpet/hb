def fibonacci(n):
    result = [1]
    for i in range(n - 1):
        if len(result) > 1:
            result.append(result[i-1] + result[i])
        else:
            result.append(1)
    return result
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(10))
