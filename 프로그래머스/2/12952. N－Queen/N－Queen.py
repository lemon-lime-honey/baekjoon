col = set()
diag1 = set()
diag2 = set()
result = 0

def nqueen(row, n):
    if row == n:
        global result
        result += 1
        return
    
    for c in range(n):
        if c in col or row + c in diag1 or row - c in diag2:
            continue
        col.add(c)
        diag1.add(row + c)
        diag2.add(row - c)
        nqueen(row + 1, n)
        col.discard(c)
        diag1.discard(row + c)
        diag2.discard(row - c)

def solution(n):
    nqueen(0, n)
    return result
    