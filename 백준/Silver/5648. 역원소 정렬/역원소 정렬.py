import sys
input = sys.stdin.readline

result = list()
start = False
n = 0

while True:
    ipt = list(map(int, input().split()))
    if not start:
        n = ipt[0]
        start = True
        ipt = ipt[1:]
    if not ipt:
        if len(result) == n:
            break
        continue
    for num in ipt:
        temp = 0
        while num:
            temp = temp * 10 + num % 10
            num //= 10
        result.append(temp)

print(*sorted(result), sep='\n')