from collections import Counter

num = Counter(map(int, input().split())).most_common(1)
print(num[0][0])