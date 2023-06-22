def solution(players, callings):
    order = dict()
    names = dict()

    for idx, name in enumerate(players):
        order[name] = idx
        names[idx] = name

    for name in callings:
        target = order[name]
        names[target], names[target - 1] = names[target - 1], names[target]
        order[name], order[names[target]] = order[names[target]], order[name]

    raw_answer = sorted(order.items(), key=lambda x:x[1])
    answer = list()
    
    for data in raw_answer:
        answer.append(data[0])

    return answer