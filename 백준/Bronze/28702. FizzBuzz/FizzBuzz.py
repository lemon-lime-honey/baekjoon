strs = [input() for i in range(3)]
target = 0

if strs[0].isdigit(): target = int(strs[0]) + 3
elif strs[1].isdigit(): target = int(strs[1]) + 2
elif strs[2].isdigit(): target = int(strs[2]) + 1

if target % 3 == 0 and target % 5 == 0:
    print("FizzBuzz")
elif target % 3 == 0:
    print("Fizz")
elif target % 5 == 0:
    print("Buzz")
else:
    print(target)