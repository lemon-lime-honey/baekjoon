n = int(input())
s = input()

nums = list()
start = 0

for i in range(n):
    if s[i] in ".|:#":
        nums.append(int(s[start:i]))
        start = i + 1
    elif i == n - 1:
        nums.append(int(s[start:]))

print(sum(nums))
