from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
card = [input().rstrip() for i in range(n)]

print(len(set(("".join(nums) for nums in permutations(card, k)))))
