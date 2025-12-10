n, m = map(int, input().split())
card = [list(map(int, input().split())) for i in range(m)]
card.sort(reverse=True)
cnt, result = 0, 0

for a, b in card:
    if a >= n:
        cnt += 1
    else:
        if cnt < m - 1:
            cnt += 1
            result += n - a

print(result)
