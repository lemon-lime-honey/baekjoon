case = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t = int(input())

for i in range(t):
    n = int(input())
    result = dict.fromkeys(case, 0)


    for m in case:
        if n >= m:
            result[m] = n // m
            n -= result[m] * m
    
    print(f'#{i + 1}')
    print(*result.values())