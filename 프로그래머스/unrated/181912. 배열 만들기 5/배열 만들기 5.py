def solution(intStrs, k, s, l):
    answer = list()
    for num in intStrs:
        chk = int(num[s:s + l])
        if chk > k: answer.append(chk)
    return answer