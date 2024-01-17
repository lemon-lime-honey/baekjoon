from collections import Counter, defaultdict
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    w = input().rstrip()
    k = int(input())

    if k == 1:
        print(1, 1)
        continue

    cnt = Counter(w)
    letterDict = defaultdict(list)

    for idx, letter in enumerate(w):
        if cnt[letter] >= k:
            letterDict[letter].append(idx)

    if len(letterDict) == 0:
        print(-1)
        continue

    short, long = int(1e9), 0

    for nums in letterDict.values():
        for j in range(len(nums) - k + 1):        
            short = min(short, nums[j + k - 1] - nums[j] + 1)
            long = max(long, nums[j + k - 1] - nums[j] + 1)
   
    print(short, long)