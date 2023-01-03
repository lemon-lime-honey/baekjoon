from itertools import permutations

n,m = map(int, input().split())
3
lst = [0]*n
num = 1

for i in range(n):
    lst[i] += num
    num += 1

result = list(permutations(lst, m))

for i in result:
    for j in range(m):
        if j != (m - 1):
            print(i[j], end = " ")
        else:
            print(i[j])
