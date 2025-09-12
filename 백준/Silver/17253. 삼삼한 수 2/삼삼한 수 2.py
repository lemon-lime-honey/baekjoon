def convert(n):
    if n == 0:
        return False

    result = list()

    while n:
        n, mod = divmod(n, 3)
        result.append(mod)

    return 2 not in result


n = int(input())

print("YES" if convert(n) else "NO")
