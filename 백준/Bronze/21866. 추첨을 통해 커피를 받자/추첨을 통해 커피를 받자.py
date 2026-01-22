nums = list(map(int, input().split()))
maximum = [100, 100, 200, 200, 300, 300, 400, 400, 500]

for i in range(9):
    if nums[i] > maximum[i]:
        print("hacker")
        break
else:
    if sum(nums) >= 100:
        print("draw")
    else:
        print("none")
