def solution(a, b):
    chkA = a % 2
    chkB = b % 2

    if chkA and chkB: return a**2 + b**2
    if chkA or chkB: return 2 * (a + b)
    return abs(a - b)