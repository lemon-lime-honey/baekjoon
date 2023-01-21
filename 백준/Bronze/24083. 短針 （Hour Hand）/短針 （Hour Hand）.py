a = int(input())
b = int(input())

if ((a + b) % 12 == 0):
    result = 12
elif a + b > 12:
    result = (a + b) % 12
else:
    result = (a + b)

print(result)