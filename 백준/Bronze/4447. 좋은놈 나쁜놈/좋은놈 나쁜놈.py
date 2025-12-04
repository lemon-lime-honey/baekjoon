n = int(input())

for i in range(n):
    ipt = input()
    lower = ipt.lower()
    g, b = lower.count("g"), lower.count("b")

    if g > b:
        print(f"{ipt} is GOOD")
    elif g < b:
        print(f"{ipt} is A BADDY")
    else:
        print(f"{ipt} is NEUTRAL")
