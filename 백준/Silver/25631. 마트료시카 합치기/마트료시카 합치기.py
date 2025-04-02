from collections import defaultdict

n = int(input())
m = list(map(int, input().split()))

m_dict = defaultdict(int)
result = 0

for size in m:
    m_dict[size] += 1
    result = max(result, m_dict[size])

print(result)