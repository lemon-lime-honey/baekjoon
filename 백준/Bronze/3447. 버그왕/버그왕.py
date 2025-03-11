import re, sys

result = list()
lines = sys.stdin.readlines()

for line in lines:
    while "BUG" in line:
        line = re.sub("BUG", "", line)
    result.append(line)

print(*result, sep="")
