from collections import deque
import sys
input = sys.stdin.readline

sieve = [True for i in range(10000)]
sieve[0], sieve[1] = False, False

for i in range(2, 101):
    if sieve[i]:
        for j in range(2 * i, 10000, i):
            sieve[j] = False

digits = [str(i) for i in range(10)]
t = int(input())

for i in range(t):
    a, b = input().rstrip().split()
    chk = [int(1e9) for i in range(10000)]
    chk[int(a)] = 0
    que = deque([(a, 0)])

    while que:
        now, cnt = que.popleft()
        if chk[int(now)] < cnt: continue
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0: continue
                target = now[:i] + digits[j] + now[i+1:]
                conv = int(target)
                if sieve[conv] and chk[conv] > cnt + 1:
                    que.append((target, cnt + 1))
                    chk[conv] = cnt + 1

    result = chk[int(b)]
    print(result if result != int(1e9) else 'Impossible')