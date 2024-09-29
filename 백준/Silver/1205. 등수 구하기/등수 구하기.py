n, s, p = map(int, input().split())

if n == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    if n == p and score[-1] >= s:
        print(-1)
    else:
        result = n + 1
        for i in range(n):
            if score[i] <= s:
                result = i + 1
                break
        print(result)