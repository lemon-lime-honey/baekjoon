def chk(n):
    if n == 1:
        return 0
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return 0
        return 1

m, n = map(int, input().split())

for i in range(m, n+1):
    if chk(i):
        print(i)
