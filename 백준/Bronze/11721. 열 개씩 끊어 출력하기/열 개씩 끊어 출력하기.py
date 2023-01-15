string = input()
length = len(string)
ref = 0

while True:
    if length >= 10:
        print(string[ref:ref + 10])
        ref += 10
        length -= 10
        if length == 0:
            break
    else:
        print(string[ref:])
        break