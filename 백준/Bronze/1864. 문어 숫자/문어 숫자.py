nums = ["-", "\\", "(", "@", "?", ">", "&", "%", "/"]

while True:
    ipt = input()

    if ipt == "#":
        break

    idx = 0
    result = 0

    for i in range(len(ipt) - 1, -1, -1):
        for j in range(8):
            if ipt[i] == nums[j]:
                result += j * 8**idx
                break
        else:
            result -= 8**idx

        idx += 1

    print(result)
