result = 0

while True:
    try:
        ipt = input()
        result += 1
    except EOFError:
        break

print(result)
