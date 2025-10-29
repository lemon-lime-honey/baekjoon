q = int(input())

for i in range(q):
    s = input()
    result = 0

    for j in range(len(s) - 2):
        if s[j : j + 3] == "WOW":
            result += 1

    print(result)
