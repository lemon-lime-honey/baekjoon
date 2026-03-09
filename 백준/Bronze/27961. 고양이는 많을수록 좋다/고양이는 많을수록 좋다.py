n = int(input())

result = 0
cnt = 0

while cnt < n:
    if n - cnt >= cnt and cnt > 0:
        cnt += cnt
        result += 1
    elif n - cnt <= cnt:
        result += 1
        break
    else:
        cnt += 1
        result += 1

print(result)
