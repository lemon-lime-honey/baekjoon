number = [0]

for i in range(1, 10000):
    flag = True

    if (i % 3):
        temp = i
        while temp:
            if (temp % 10) == 3:
                flag = False
                break
            temp //= 10
    else:
        flag = False

    if flag:
        number.append(i)

def solution(n):
    return number[n]