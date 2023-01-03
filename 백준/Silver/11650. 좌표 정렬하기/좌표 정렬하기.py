import sys

n = int(input())
loc = [[0]*2 for i in range(n)]

for i in range(n):
    loc[i][0], loc[i][1] = map(int, sys.stdin.readline().split())
    
loc.sort(key = lambda x: (x[0],x[1]))

for i in range(n):
    print(*loc[i])
