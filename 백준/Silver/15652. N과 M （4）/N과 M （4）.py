from itertools import combinations_with_replacement

n,m = map(int, input().split())

lst = [0]*n
num = 1

for i in range(n):
    lst[i] += num
    num += 1

result = list(combinations_with_replacement(lst, m))

for i in result:
    for j in range(m):
        if j != (m - 1):
            print(i[j], end = " ")
        else:
            print(i[j])
