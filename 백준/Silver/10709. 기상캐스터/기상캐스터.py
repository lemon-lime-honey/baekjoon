import sys
input = sys.stdin.readline

h, w = map(int, input().split())
result = [[-1 for i in range(w)] for j in range(h)]

for i in range(h):
    ipt = input().rstrip()
    for j in range(w):
        if ipt[j] == 'c':
            num = 0
            for k in range(j, w):
                result[i][k] = num
                num += 1

for row in result:
    print(*row)