ab = [1, 0]

def button(n):
    if n == 1:
        ab[0] = 0
        ab[1] = 1
        return ab
    for i in range(n):
        temp = ab[0]
        ab[0] = ab[1]
        ab[1] += temp
    return ab

k = int(input())
ab = button(k)
print(f'{ab[0]} {ab[1]}')