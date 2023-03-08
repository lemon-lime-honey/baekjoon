def exp(n, m):
    if not n: return 0
    if not m: return 1

    result = exp(n, m // 2)
    return (n * result * result) if m % 2 else (result * result)

for i in range(10):
    t = int(input())
    a, b = map(int, input().split())
    answer = exp(a, b)
    print(f'#{t} {answer}')