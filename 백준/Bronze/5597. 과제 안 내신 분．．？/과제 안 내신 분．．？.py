student = [x for x in range(1, 31)]

while True:
    temp = int(input())
    student.remove(temp)
    if (len(student) == 2):
        break

student.sort()

for person in student:
    print(person)