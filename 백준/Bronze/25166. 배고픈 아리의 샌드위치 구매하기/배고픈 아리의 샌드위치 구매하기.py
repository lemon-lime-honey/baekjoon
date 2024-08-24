s, m = map(int, input().split())
a = 1 << 10 - 1

if s < 1024:
    print("No thanks")
elif (s - 1023) & m == s - 1023:
    print("Thanks")
else:
    print("Impossible")
