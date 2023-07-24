def solution(arr):
    for i in range(11):
        chk = 2 ** i
        if len(arr) < chk:
            arr.extend([0 for j in range(chk - len(arr))])
            return arr
        elif len(arr) == chk:
            return arr