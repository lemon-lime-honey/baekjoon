one = list(map(int, input().split()))
two = list(map(int, input().split()))

dist = ((two[0] - one[0]) ** 2 + (two[1] - one[1]) ** 2) ** 0.5

if dist >= one[2] + two[2]:
    print("NO")
else:
    print("YES")
