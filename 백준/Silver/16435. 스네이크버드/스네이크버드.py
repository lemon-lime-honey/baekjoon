import sys
input = sys.stdin.readline

n, l = map(int, input().split())
h = sorted(list(map(int, input().split())))

for height in h:
    if l >= height:
        l += 1
    else:
        break

print(l)