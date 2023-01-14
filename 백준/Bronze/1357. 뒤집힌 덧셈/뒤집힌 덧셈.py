def rev(n):
    return n[::-1]

x, y = map(str, input().split())

total = int(rev(x)) + int(rev(y))
result = int(rev(str(total)))

print(result)