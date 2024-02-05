import sys
input = sys.stdin.readline

n, h, w = map(int, input().split())
result = ['?' for i in range(n)]

for i in range(h):
    ipt = input().rstrip()
    for j in range(0, n * w, w):
        for k in range(w):
            if ipt[j + k] != '?':
                result[j // w] = ipt[j + k]

print(''.join(result))