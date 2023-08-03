def star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    before = star(n // 2)
    result = list()
    ref = n - 1
    for i in range(n):
        if i < len(before):
            result.append(' ' * (n - i - 1) + before[i].strip() + ' ' * (n - i - 1))
        else:
            result.append(
                ' ' * (n - i - 1) + before[i % len(before)].strip()
                + ' ' * (ref) + before[i % len(before)].strip()
                + ' ' * (n - i - 1)
            )
            ref -= 2
    return result


n = int(input())
result = star(n)
for i in range(n):
    print(*result[i], sep='')