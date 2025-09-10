score = {"Kk": 0, "Pp": 1, "Nn": 3, "Bb": 3, "Rr": 5, "Qq": 9}

result = 0

for i in range(8):
    ipt = input()
    for j in range(8):
        for key in score:
            if ipt[j] in key:
                if ipt[j].isupper():
                    result += score[key]
                else:
                    result -= score[key]
                break

print(result)
