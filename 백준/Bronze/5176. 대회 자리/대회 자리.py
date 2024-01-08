k = int(input())

for i in range(k):
    p, m = map(int, input().split())
    seat = [False for i in range(m + 1)]
    result = 0
    for j in range(p):
        target = int(input())
        if not seat[target]:
            seat[target] = True
        else:
            result += 1
    print(result)