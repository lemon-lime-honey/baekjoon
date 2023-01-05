original = input()
if original[1] == '0':
    print(int(original[0:2]) + int(original[2:]))
else:
    print(int(original[0]) + int(original[1:]))