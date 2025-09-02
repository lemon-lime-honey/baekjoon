result = [-1, 2**63]

n, q = map(int, input().split())

for i in range(1, n + 1):
    p, k, c = map(int, input().split())

    chk = (q - 1) // k
    chk = p + chk * (chk + 1) // 2 * c

    if chk < result[1]:
        result[0] = i
        result[1] = chk

print(*result)
