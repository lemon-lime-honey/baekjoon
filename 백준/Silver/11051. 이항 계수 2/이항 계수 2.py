def combination(n, k):
    num1 = n
    num2 = max(k, n - k)
    num3 = min(k, n - k)
    result = 1

    while num1:
        if num1 > num2:
            result *= num1
            num1 -= 1
        elif num1 > num3:
            num1 -=1
        else:
            result //= num3
            num3 -= 1
    
    return result

n, k = map(int, input().split())
print(combination(n, k) % 10007)