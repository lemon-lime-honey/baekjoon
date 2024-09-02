def calculate(num):
    result = 6
    for i in range(11, num + 1):
        result *= i
    return result


n = int(input())
print(calculate(n))
