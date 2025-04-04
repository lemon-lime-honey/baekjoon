from collections import Counter

n = int(input())

for i in range(n):
    ipt = list(map(int, input().split()))
    nums = Counter(ipt[1:]).most_common()
    if ipt[0] // 2 < nums[0][1]:
        print(nums[0][0])
    else:
        print("SYJKGW")
