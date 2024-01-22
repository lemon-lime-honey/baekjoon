from functools import cmp_to_key
import sys
input = sys.stdin.readline


def compare(x, y):
    if x[0].isdigit() and y[0].isalpha():
        return -1
    if x[0].isalpha() and y[0].isdigit():
        return 1

    xList = list()
    yList = list()

    for letter in x:
        if not xList or letter.isalpha():
            xList.append(letter)
        elif xList[-1].isalpha():
            xList.append(letter)
        else:
            xList[-1] += letter

    for letter in y:
        if not yList or letter.isalpha():
            yList.append(letter)
        elif yList[-1].isalpha():
            yList.append(letter)
        else:
            yList[-1] += letter

    i, j = 0, 0
    
    while i < len(xList) and j < len(yList):
        if xList[i].isdigit() and yList[j].isalpha():
            return -1
        if xList[i].isalpha() and yList[j].isdigit():
            return 1
        if xList[i].isdigit() and yList[j].isdigit():
            xVal = int(xList[i])
            yVal = int(yList[j])
            if xVal < yVal:
                return -1
            elif xVal > yVal:
                return 1
            elif len(xList[i]) < len(yList[j]):
                return -1
            elif len(xList[i]) > len(yList[j]):
                return 1
        if xList[i].isalpha() and yList[j].isalpha():
            if xList[i].lower() == yList[j].lower():
                if xList[i].isupper() and yList[j].islower():
                    return -1
                elif xList[i].islower() and yList[j].isupper():
                    return 1
            elif xList[i].lower() < yList[j].lower():
                return -1
            elif xList[i].lower() > yList[j].lower():
                return 1
        i += 1
        j += 1
  
    if i == len(xList):
        return -1
    if j == len(yList):
        return 1
    
    return 0


n = int(input())
strs = [input().rstrip() for i in range(n)]
print(*sorted(strs, key=cmp_to_key(compare)), sep='\n')
