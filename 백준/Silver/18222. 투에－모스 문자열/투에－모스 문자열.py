def get_number(n):
    if n == 0: return 0
    if n == 1: return 1

    if not n % 2: return get_number(n // 2)
    return 1 - get_number(n // 2)


k = int(input())
print(get_number(k - 1))