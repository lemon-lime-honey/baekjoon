def execute(idx, total, route):
    if total == 100 and len(route) == 7:
        print(*route, sep='\n')
        return

    for i in range(idx, 9):
        route.append(nums[i])
        execute(i + 1, total + nums[i], route)
        route.pop()


nums = [int(input()) for i in range(9)]
execute(0, 0, list())