import re

ipt = input()
targets = {"social", "history", "language", "literacy"}

for target in targets:
    if re.search(target, ipt):
        print("digital humanities")
        break
else:
    print("public bigdata")
