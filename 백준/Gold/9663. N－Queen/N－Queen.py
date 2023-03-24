n = int(input())

negDiag = set()
posDiag = set()
col = set()
result = 0

def backtrack(row):
    global result
    if row == n:
        result += 1
        return
    
    for c in range(n):
        if c in col or (row + c) in posDiag or (row - c) in negDiag:
            continue

        col.add(c)
        posDiag.add(row + c)
        negDiag.add(row - c)
        backtrack(row + 1)
        col.remove(c)
        posDiag.remove(row + c)
        negDiag.remove(row - c)

backtrack(0)

print(result)