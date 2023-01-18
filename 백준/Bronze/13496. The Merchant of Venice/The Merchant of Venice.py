k = int(input())

for i in range(k):
    n, s, d = map(int, input().split())
    money = 0
    for j in range(n):
        dist, value = map(int, input().split())
        if (dist / s) <= d:
            money += value
    print(f'Data Set {i + 1}:\n{money}\n')