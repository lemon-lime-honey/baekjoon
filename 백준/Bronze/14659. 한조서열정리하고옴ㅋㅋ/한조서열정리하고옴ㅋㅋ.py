n = int(input())
hill = list(map(int, input().split()))
before = 0
cnt = 0
result = list()

for index, height in enumerate(hill):
    if (height > before):
        if index != n - 1:
            result.append(cnt)
            cnt = 0
            before = height
    else:
        cnt += 1

result.append(cnt)
print(max(result))