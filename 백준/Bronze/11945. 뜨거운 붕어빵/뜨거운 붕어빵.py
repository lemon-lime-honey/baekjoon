n, m = map(int, input().split())
for i in range(n):
    temp = input()
    for j in range(len(temp) - 1, -1, -1):
        print(temp[j], end = '')
    print()