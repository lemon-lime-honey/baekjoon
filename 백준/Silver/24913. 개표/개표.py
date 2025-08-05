import sys

input = sys.stdin.readline

n, q = map(int, input().split())
score = [0 for i in range(n + 2)]
maximum, total = 0, 0

for i in range(q):
    a, b, c = map(int, input().split())
    match a:
        case 1:
            score[c] += b
            if c != n + 1:
                total += b
                maximum = max(maximum, score[c])
        case 2:
            if score[n + 1] + b > maximum and (score[n + 1] + b - 1) * n >= total + c:
                print("YES")
            else:
                print("NO")
