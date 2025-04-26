n = int(input())

for i in range(1, n + 1):
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[-1] ** 2 == nums[0] ** 2 + nums[1] ** 2:
        print(f"Scenario #{i}:\nyes")
    else:
        print(f"Scenario #{i}:\nno")
    print()
