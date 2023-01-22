n = int(input())

for i in range(n):
    c, p = map(int, input().split())
    print(f'{c} {p}')
    
    if c == 1:
        print(p)
    else:
        print(p * c - 2 * (c - 1))