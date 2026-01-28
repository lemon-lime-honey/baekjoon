t = int(input())

for i in range(t):
    time = int(input()) % 25

    if time < 17:
        print("ONLINE")
    else:
        print("OFFLINE")
