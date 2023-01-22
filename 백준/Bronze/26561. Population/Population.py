n = int(input())

for i in range(n):
    p, t = map(int, input().split())
    result = p - (t // 7) + (t // 4)
    print(result)