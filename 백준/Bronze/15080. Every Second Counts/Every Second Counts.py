start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

if (end[0] == start[0]) * ((end[1] < start[1]) + (end[1] == start[1]) * (end[2] < start[2])):
        hour = 23
        minute = 60 + end[1] - start[1]

else:
    if end[0] < start[0]:
        end[0] += 24

    hour = end[0] - start[0]

    if end[1] < start[1]:
        hour -= 1
        end[1] += 60

    minute = end[1] - start[1]

if end[2] < start[2]:
    minute -= 1
    end[2] += 60

second = end[2] - start[2]

print(hour * 60 * 60 + minute * 60 + second)