t = int(input())

for i in range(t):
    n = int(input())
    if n < 5:
        print(0)
    else:
        result = 0
        num = 5

        while num <= n:
            result += n // num
            num *= 5

        print(result)
