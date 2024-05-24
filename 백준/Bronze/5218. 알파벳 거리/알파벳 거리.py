import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = input().split()
    dist = [0 for i in range(len(a))]

    for j in range(len(a)):
        dist[j] = ord(b[j]) - ord(a[j])
        if dist[j] < 0: dist[j] += 26
        
    print('Distances: ', end='')
    print(*dist)