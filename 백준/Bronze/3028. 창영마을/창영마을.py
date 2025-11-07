mix = {"A": (1, 2), "B": (2, 3), "C": (1, 3)}
cup = [False, True, False, False]

ipt = input()

for letter in ipt:
    a, b = mix[letter][0], mix[letter][1]
    cup[a], cup[b] = cup[b], cup[a]

print(cup.index(True))
