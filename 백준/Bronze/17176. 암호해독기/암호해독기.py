from collections import Counter

n = int(input())

nums = list(map(int, input().split()))
letters = Counter(input())
chk = list()

for num in nums:
    if num == 0:
        chk.append(" ")
    elif num < 27:
        chk.append(chr(num + ord("A") - 1))
    else:
        chk.append(chr(num + ord("a") - 27))

if letters == Counter(chk):
    print("y")
else:
    print("n")