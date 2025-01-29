n = int(input())

for i in range(n):
    num = input()
    if (int(num) + 1) % int(num[2:]) == 0:
        print("Good")
    else:
        print("Bye")
