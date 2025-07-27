t = int(input())

for i in range(1, t + 1):
    ipt = input().split()
    parents = [0, 0]

    for j in range(1, 3):
        height = list(map(int, ipt[j].replace('"', "").split("'")))
        parents[j - 1] += height[1] + height[0] * 12

    match ipt[0]:
        case "B":
            result = (sum(parents) + 5) / 2
        case "G":
            result = (sum(parents) - 5) / 2

    if result != int(result):
        lower = int(result - 3.5)
        upper = int(result + 3.5)
    else:
        lower = int(result - 4)
        upper = int(result + 4)

    print(f"Case #{i}: {lower // 12}'{lower % 12}\" to {upper // 12}'{upper % 12}\"")
