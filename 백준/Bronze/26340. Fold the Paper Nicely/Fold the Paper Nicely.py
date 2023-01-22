n = int(input())

for i in range(n):
    side1, side2, fold = map(int, input().split())
    print(f'Data set: {side1} {side2} {fold}')
    
    cnt = 0
    larger = max(side1, side2)
    smaller = min(side1, side2)
    
    while cnt < fold:
        larger = larger // 2
        if larger < smaller:
            larger, smaller = smaller, larger
        cnt += 1
    print(f'{larger} {smaller}\n')