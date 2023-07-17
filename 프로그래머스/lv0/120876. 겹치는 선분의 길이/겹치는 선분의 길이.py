def solution(lines):
    chk = [False for i in range(202)]
    overlap = [False for i in range(202)]
    result = 0
    for start, end in lines:
        for i in range(start + 100, end + 100):
            if chk[i]:
                overlap[i] = True
            else:
                chk[i] = True
    for i in range(202):
        if overlap[i]: result += 1
    return result