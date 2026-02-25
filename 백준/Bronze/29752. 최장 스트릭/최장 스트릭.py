result = 0
cnt = 0

n = int(input())
solved = list(map(int, input().split()))

for s in solved:
    if s == 0:
        cnt = 0
    else:
        cnt += 1
        result = max(result, cnt)

print(result)
