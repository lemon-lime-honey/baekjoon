import re

s = input()
pattern = re.compile("driip$")

if re.search(pattern, s):
    print("cute")
else:
    print("not cute")
