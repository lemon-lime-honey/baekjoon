n = int(input())
paper = [[False for i in range(100)] for j in range(100)]
area = 0

for i in range(n):
    left, under = map(int, input().split())
    for j in range(under, under + 10):
        for k in range(left, left + 10):
            paper[k][j] = True

for i in range(100):
    for j in range(100):
        if paper[i][j] == True:
            area += 1

print(area)