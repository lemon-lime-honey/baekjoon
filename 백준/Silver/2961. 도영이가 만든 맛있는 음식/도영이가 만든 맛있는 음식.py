def backtrack(idx, s, b, cnt):
    if idx == n:
        if cnt:
            global result
            result = min(result, abs(s - b))
        return

    backtrack(idx + 1, s * ingredients[idx][0], b + ingredients[idx][1], cnt + 1)
    backtrack(idx + 1, s, b, cnt)


n = int(input())
ingredients = [list(map(int, input().split())) for i in range(n)]
result = int(1e12)

backtrack(0, 1, 0, 0)

print(result)
