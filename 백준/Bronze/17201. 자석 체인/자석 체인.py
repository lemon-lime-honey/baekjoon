n = int(input())
nums = input()

for i in range(1, n * 2):
    if nums[i] == nums[i - 1]:
        print("No")
        break
else:
    print("Yes")
