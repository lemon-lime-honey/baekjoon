import sys
input = sys.stdin.readline

l = int(input())
n = int(input())
cake = [0 for i in range(l + 1)]
guess = [0, 0]
real = [0, 0]

for i in range(1, n + 1):
    p, k = map(int, input().split())
    cnt = 0

    if k - p + 1 > guess[0]:
        guess[0] = k - p + 1
        guess[1] = i

    for j in range(p, k + 1):
        if cake[j] == 0:
            cnt += 1
            cake[j] = i

    if cnt > real[0]:
        real[0] = cnt
        real[1] = i

print(guess[1], real[1], sep='\n')
