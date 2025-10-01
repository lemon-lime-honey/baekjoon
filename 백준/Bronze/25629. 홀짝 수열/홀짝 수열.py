n = int(input())
original = list(map(int, input().split()))

odd, even = list(), list()

for num in original:
    if num % 2:
        odd.append(num)
    else:
        even.append(num)

if len(odd) in (len(even), len(even) + 1):
    print(1)
else:
    print(0)
