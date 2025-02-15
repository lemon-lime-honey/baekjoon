n = input()

if "7" not in n:
    if int(n) % 7: print(0)
    else: print(1)
elif int(n) % 7: print(2)
else: print(3)