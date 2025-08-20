n = int(input())

origin = [["@", "   ", "@"], ["@@@@@"], ["@", "   ", "@"], ["@@@@@"], ["@", "   ", "@"]]

for line in origin:
    for _ in range(n):
        for element in line:
            for _ in range(n):
                print(element, sep="", end="")
        print()
