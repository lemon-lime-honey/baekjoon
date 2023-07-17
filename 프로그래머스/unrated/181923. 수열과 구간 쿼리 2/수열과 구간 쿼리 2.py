def solution(arr, queries):
    answer = list()
    for s, e, k in queries:
        chk = int(1e9)
        for i in range(s, e + 1):
            if arr[i] > k:
                chk = min(chk, arr[i])
        if chk != int(1e9): answer.append(chk)
        else: answer.append(-1)
    return answer