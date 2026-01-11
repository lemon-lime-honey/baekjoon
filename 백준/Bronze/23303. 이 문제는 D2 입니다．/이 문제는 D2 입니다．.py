import re

ipt = input().lower()
pattern = re.compile("d2")

if re.search(pattern, ipt):
    print("D2")
else:
    print("unrated")
