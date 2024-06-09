from math import sqrt, gcd
import sys
input = sys.stdin.readline


def get_nums(n1, n2):
    g = gcd(n1, n2)
    for i in range(1, int(sqrt(g)) + 1):
        if g % i == 0:
            nums.add(i)
            nums.add(g // i)


t = int(input())

for i in range(t):
    w, l = map(int, input().split())
    nums = {2}
    get_nums(w - 1, l - 1)
    get_nums(w - 2, l)
    get_nums(w, l - 2)
    print(len(nums), *[num for num in sorted(nums)])