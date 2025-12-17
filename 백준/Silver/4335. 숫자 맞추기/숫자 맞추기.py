lo, hi = 0, 11

while True:
    n = int(input())
    
    if n == 0:
        break

    answer = input()
    
    if answer == "right on":
        if lo < n < hi:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        lo, hi = 0, 11
    elif answer == "too high":
        hi = min(hi, n)
    elif answer == "too low":
        lo = max(lo, n)
