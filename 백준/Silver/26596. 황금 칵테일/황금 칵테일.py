from collections import defaultdict
from math import floor

ingredients = defaultdict(int)

m = int(input())

for i in range(m):
    ipt = input().split()
    amount = int(ipt[1])
    name = ipt[0]

    ingredients[name] += amount

target = list(ingredients.keys())
chk = False

for i in range(len(target)):
    for j in range(i + 1, len(target)):
        if (
            floor(ingredients[target[i]] * 1.618) == ingredients[target[j]]
            or floor(ingredients[target[j]] * 1.618) == ingredients[target[i]]
        ):
            chk = True
            break
    if chk:
        break

print("Delicious!" if chk else "Not Delicious...")
