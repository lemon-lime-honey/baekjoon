n = int(input())
ipt = input()
nums = list()
temp = list()

for letter in ipt:
    if letter.isalpha():
        if not temp:
            continue
        nums.append(int("".join(temp)))
        temp.clear()
    else:
        temp.append(letter)

if temp:
    nums.append(int("".join(temp)))

print(sum(nums))
