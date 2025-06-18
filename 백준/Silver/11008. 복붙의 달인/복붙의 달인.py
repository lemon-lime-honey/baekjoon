t = int(input())

for i in range(t):
    s, p = input().split()
    result = 0
    idx = 0

    while idx < len(s):
        result += 1
        if s[idx: idx + len(p)] != p:
            idx += 1
        else:
            idx += len(p)

    print(result)
