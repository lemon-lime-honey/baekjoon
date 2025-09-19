idx = 1

while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    print(f"Triangle #{idx}")

    if c == -1:
        c = (a**2 + b**2) ** 0.5
        print(f"c = {c:0.3f}")
    elif max(a, b) >= c:
        print("Impossible.")
    elif a == -1:
        a = (c**2 - b**2) ** 0.5
        print(f"a = {a:0.3f}")
    elif b == -1:
        b = (c**2 - a**2) ** 0.5
        print(f"b = {b:0.3f}")

    print()
    idx += 1
