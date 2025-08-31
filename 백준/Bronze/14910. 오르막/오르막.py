nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    if nums[i - 1] > nums[i]:
        print("Bad")
        break
else:
    print("Good")
