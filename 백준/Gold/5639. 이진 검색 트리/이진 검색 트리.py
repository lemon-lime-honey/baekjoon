from itertools import takewhile
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def post(nums):
    if not nums: return list()
    root = nums[0]
    left = list(takewhile(lambda x: x < root, nums[1:]))
    right = nums[len(left) + 1:]
    return post(left) + post(right) + [root]


numbers = list()

while True:
    try: numbers.append(int(input()))
    except: break

result = post(numbers)
print(*result, sep='\n')