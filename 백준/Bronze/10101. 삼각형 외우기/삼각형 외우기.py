angle = list()
for i in range(3):
    angle.append(int(input()))

if sum(angle) != 180:
    print('Error')
elif angle[0] == angle[1] == angle[2]:
    print('Equilateral')
elif (angle[0] == angle[1]) + (angle[0] == angle[2]) + (angle[1] == angle[2]):
    print('Isosceles')
else:
    print('Scalene')