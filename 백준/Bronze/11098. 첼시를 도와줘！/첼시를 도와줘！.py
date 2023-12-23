n = int(input())

for i in range(n):
    p = int(input())
    name = ''
    cost = 0
    for j in range(p):
        ipt = input().split()
        if cost < int(ipt[0]):
            cost = int(ipt[0])
            name = ipt[1]
    print(name)