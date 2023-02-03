from itertools import combinations

n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
result = list(combinations(number, m))

for res in result:
    print(*res)