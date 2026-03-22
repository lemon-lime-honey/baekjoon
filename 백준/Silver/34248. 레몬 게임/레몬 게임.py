n = int(input())
lemon = list(map(int, input().split()))

one = lemon.count(1)
two = lemon.count(2)

if one >= two:
    one -= two
    if one % 3:
        print("No")
    else:
        print("Yes")
else:
    print("No")
