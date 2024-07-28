n = int(input())
nums = list(map(int, input().split()))
cnt = [0 for i in range(10)]
result = 0
types = 0
lo = 0

for i in range(n):
    cnt[nums[i]] += 1

    if cnt[nums[i]] == 1:
        types += 1

    while types > 2:
        cnt[nums[lo]] -= 1
        if cnt[nums[lo]] == 0:
            types -= 1
        lo += 1

    result = max(result, i - lo + 1)

print(result)
