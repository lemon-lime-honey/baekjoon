numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[0] + numbers[1] + min(numbers[2], numbers[0] + numbers[1] - 1))