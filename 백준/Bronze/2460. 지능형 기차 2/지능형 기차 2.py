max = 0
people = 0

for i in range(10):
    o, i = map(int, input().split())
    people += (i - o)
    if max < people:
        max = people

print(max)