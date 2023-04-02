def visit(n, r, c):
    global result
    if n == 0: return
    area = 2 ** n
    half = area // 2

    if (r // half == 0 and c // half == 0):
        result += half * half * 0
        visit(n - 1, r % half, c % half)
    elif (r // half == 0 and c // half == 1):
        result += half * half * 1
        visit(n - 1, r % half, c % half)
    elif (r // half == 1 and c // half == 0):
        result += half * half * 2
        visit(n - 1, r % half, c % half)
    elif (r // half == 1 and c // half == 1):
        result += half * half * 3
        visit(n - 1, r % half, c % half)

n, r, c = map(int, input().split())
result = 0

visit(n, r, c)
print(result)