def change(number):
    result = 0
    while number:
        result += number % 10
        number //= 10
    return result

while True:
    num = int(input())
    if not num:
        break

    while True:
        result = change(num)
        if result < 10:
            break
        num = result

    print(result)