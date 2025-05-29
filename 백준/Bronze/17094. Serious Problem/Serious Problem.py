length = int(input())
s = input()

two = s.count('2')

if 2 * two > length:
    print(2)
elif 2 * two < length:
    print("e")
else:
    print("yee")