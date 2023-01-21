mem = {0: 0, 1: 1}

def fibonacci(n):
    if n in mem:
        return mem[n]
    mem[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return mem[n]

n = int(input())
print(fibonacci(n))