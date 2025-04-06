N, m, M, T, R = map(int, input().split())

if M - m < T:
    print(-1)
else:
    beat = m
    result = 0

    while N:
        if beat + T <= M:
            beat += T
            N -= 1
        else:
            beat -= R
            if beat < m: beat = m
        result += 1

    print(result)
