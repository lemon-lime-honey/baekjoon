n, b, h, w = map(int, input().split())
minimum = b

for i in range(h):
    p = int(input())
    a = list(map(int, input().split()))
    if (p * n < b):
        for i in a:
            if (i >= n) * (p * n < minimum):
                minimum = p * n

if minimum == b:
    print('stay home')
else:
    print(minimum)