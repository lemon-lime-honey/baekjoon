import sys
input = sys.stdin.readline

n = int(input())
scores = list()

for i in range(n):
    ipt = input().rstrip().split()
    scores.append([ipt[0]] + list(map(int, ipt[1:])))

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
print(*[x[0] for x in scores], sep='\n')