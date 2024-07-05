import sys
input = sys.stdin.readline

t = int(input())
result = list()

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    k = int(input())
    c = list(map(int, input().split()))

    nums = set()

    for j in range(n):
        for l in range(m):
            for o in range(k):
                num = a[j] + b[l] + c[o]
                flag = True
                while num:
                    if num % 10 not in (5, 8):
                        flag = False
                        break
                    num //= 10
                if flag: nums.add(a[j] + b[l] + c[o])

    result.append(len(nums))

print(*result, sep='\n')
