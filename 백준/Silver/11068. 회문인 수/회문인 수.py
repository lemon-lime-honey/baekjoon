t = int(input())

for i in range(t):
    target = int(input())
    for j in range(2, 65):
        num = list()
        n = target

        while n:
            num.append(n % j)
            n //= j
        for k in range(len(num) // 2):
            if num[k] != num[-1-k]:
                break
        else:
            print(1)
            break
    else:
        print(0)
