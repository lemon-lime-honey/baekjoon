letter = {
    "000000": "A",
    "001111": "B",
    "010011": "C",
    "011100": "D",
    "100110": "E",
    "101001": "F",
    "110101": "G",
    "111010": "H",
}

password = [
    "000000",
    "001111",
    "010011",
    "011100",
    "100110",
    "101001",
    "110101",
    "111010",
]

n = int(input())
ipt = input()

result = list()
idx = 0

while idx < n * 6:
    for i in range(8):
        diff = 0
        for j in range(6):
            if password[i][j] != ipt[idx + j]:
                diff += 1
                if diff > 1:
                    break
        else:
            result.append(letter[password[i]])
            idx += 6
            break
    else:
        print(idx // 6 + 1)
        break

if len(result) == n:
    print("".join(result))
