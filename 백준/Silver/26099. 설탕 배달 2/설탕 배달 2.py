n = int(input())

three, five = n // 3, n // 5
result = [int(1e9), int(1e9)]

while three:
    if (n - three * 3) % 5 == 0:
        result[0] = three + (n - three * 3) // 5
        break
    three -= 1

while five:
    if (n - five * 5) % 3 == 0:
        result[1] = five + (n - five * 5) // 3
        break
    five -= 1

answer = min(result)

print(answer if answer != int(1e9) else -1)
