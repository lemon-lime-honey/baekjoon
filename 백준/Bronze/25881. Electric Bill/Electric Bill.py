base, extra = map(int, input().split())
n = int(input())

for i in range(n):
    power = int(input())
    charge = 0
    
    if power <= 1000:
        charge += power * base
    else:
        charge += 1000 * base + (power - 1000) * extra
    
    print(f'{power} {charge}')