t = int(input())

for i in range(1, t + 1):
    v, e = map(int, input().split())
    print(2 - v + e)