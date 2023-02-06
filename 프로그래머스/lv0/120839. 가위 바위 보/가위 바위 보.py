rsp_win = {"2": "0", "0": "5", "5": "2"}

def solution(rsp):
    answer = list()
    for num in rsp:
        answer.append(rsp_win[num])
    return (''.join(answer))