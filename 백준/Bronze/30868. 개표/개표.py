t = int(input())

for i in range(t):
    n = int(input())
    for j in range(n // 5):
        print("++++ ", end="")
    print("|" * (n % 5))