import re

s = input()
p = input()

if re.search(p, s):
    print(1)
else:
    print(0)