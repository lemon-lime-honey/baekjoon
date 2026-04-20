from collections import Counter

l = int(input())
s = Counter(input())

print(s["A"] * s["T"] * s["G"] * s["C"] % 1000000007)
