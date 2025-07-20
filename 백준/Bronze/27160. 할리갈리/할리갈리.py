from collections import defaultdict

n = int(input())
fruits = defaultdict(int)

for i in range(n):
    ipt = input().split()
    fruits[ipt[0]] += int(ipt[1])

for value in fruits.values():
    if value == 5:
        print("YES")
        break
else:
    print("NO")
