def chk(num):
    if num <= 9:
        return 1

    for i in range(2, 10):
        for j in range(1, 10):
            if i == num or j == num or i * j == num:
                return 1

    return 0


n = int(input())

print(chk(n))
