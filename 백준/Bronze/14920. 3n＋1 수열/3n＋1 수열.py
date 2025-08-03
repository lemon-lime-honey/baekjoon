c = int(input())
n = 1

while c != 1:
    if c % 2:
        c = 3 * c + 1
    else:
        c = c // 2
    n += 1

print(n)
