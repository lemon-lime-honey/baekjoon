import re

n = int(input())
target = input()
result = [0, 0]

result[0] = len(re.findall("bigdata", target))
result[1] = len(re.findall("security", target))

if result[0] < result[1]:
    print("security!")
elif result[0] > result[1]:
    print("bigdata?")
else:
    print("bigdata? security!")
