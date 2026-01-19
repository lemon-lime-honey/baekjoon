result = list()

index = 1
pi = 3.1415927

while True:
    diameter, rotation, time = map(float, input().split())

    if rotation == 0:
        break

    distance = diameter * pi * rotation / 5280 / 12
    speed = distance / time * (60 * 60)

    result.append(f"Trip #{index}: {round(distance, 2):.2f} {round(speed, 2):.2f}")

    index += 1

print(*result, sep="\n")
