from copy import deepcopy

def solution(arr):
    x = 0
    before = deepcopy(arr)
    while True:
        result = list()
        for number in before:
            if number >= 50 and not number % 2:
                result.append(number // 2)
            elif number < 50 and number % 2:
                result.append(number * 2 + 1)
            else: result.append(number)
        if before == result: return x
        else:
            before = result
            x += 1