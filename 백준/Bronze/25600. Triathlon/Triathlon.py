n = int(input())
max = 0

for i in range(n):
    a, d, g = map(int, input().split())
    if a == d + g:
        score = 2 * a * (d + g)
    else:
        score = a * (d + g)
    
    if max < score:
        max = score

print(max)