a, b, c, d = map(int, input().split())

shuttle = a + b

if shuttle > d:
    if c > d:
        print("T.T")
    else:
        print("Walk")
else:
    if c > d:
        print("Shuttle")
    else:
        print("~.~")
