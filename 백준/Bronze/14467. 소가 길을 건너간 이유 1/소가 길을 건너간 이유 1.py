n = int(input())
cow = [-1 for i in range(10)]
result = 0

for i in range(n):
    num, loc = map(int, input().split())
    if cow[num - 1] == -1:
        cow[num - 1] = loc
    else:
        if cow[num - 1] != loc:
            result += 1
            cow[num - 1] = loc

print(result)