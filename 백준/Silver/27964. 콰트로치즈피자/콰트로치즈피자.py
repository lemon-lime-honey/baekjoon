n = int(input())
targets = input().split()
result = set()

for target in targets:
    if len(target) < 6:
        continue
    if target.endswith("Cheese"):
        result.add(target)

print("yummy" if len(result) > 3 else "sad")
