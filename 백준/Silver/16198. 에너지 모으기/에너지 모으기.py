import sys

input = sys.stdin.readline


def backtrack(total, size):
    global result
    result = max(result, total)

    if size == 2:
        return

    for i in range(1, n - 1):
        if chk[i]:
            chk[i] = False
            temp = 1
            for j in range(i - 1, -1, -1):
                if not chk[j]:
                    continue
                temp *= weights[j]
                break
            for j in range(i + 1, n):
                if not chk[j]:
                    continue
                temp *= weights[j]
                break
            backtrack(total + temp, size - 1)
            chk[i] = True


n = int(input())
weights = list(map(int, input().split()))
chk = [True for i in range(n)]
result = 0
backtrack(0, n)

print(result)
