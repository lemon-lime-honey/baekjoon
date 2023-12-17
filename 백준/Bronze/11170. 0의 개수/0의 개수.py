t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    result = 0

    for j in range(n, m + 1):
        result += str(j).count('0')

    print(result)