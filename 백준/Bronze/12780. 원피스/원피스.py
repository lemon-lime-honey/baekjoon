h = input()
n = input()

idx, result = 0, 0

while idx <= len(h) - len(n):
    if h[idx : idx + len(n)] == n:
        result += 1
        idx += len(n)
    else:
        idx += 1

print(result)
