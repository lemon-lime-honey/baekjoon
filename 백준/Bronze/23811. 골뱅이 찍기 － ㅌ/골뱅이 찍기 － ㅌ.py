target = ["@@@@@", "@", "@@@@@", "@", "@@@@@"]

n = int(input())

for line in target:
    for i in range(n):
        print(line * n, sep="")
