p = int(input())
arr = ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]

for i in range(p):
    result = [0 for i in range(8)]
    ipt = input()

    for j in range(38):
        for k in range(8):
            if ipt[j : j + 3] == arr[k]:
                result[k] += 1
                break

    print(*result)
