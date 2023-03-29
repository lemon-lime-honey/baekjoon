tc = int(input())

for i in range(tc):
    n = int(input())
    income = list(map(int, input().split()))
    mean = sum(income) / n
    result = 0

    for element in income:
        if element <= mean:
            result += 1
    
    print(f'#{i + 1} {result}')