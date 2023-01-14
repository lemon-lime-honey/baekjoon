def chk(n):
    if int(n) < 100:
        return 1
    else:
        diff = int(n[0]) - int(n[1])
        for i in range(2, len(n)):
            if (int(n[i - 1]) - int(n[i])) != diff:
                break
        else:
            return 1
        return 0

n = int(input())
result = 0

for i in range(1, n + 1):
    result += chk(str(i))

print(result)