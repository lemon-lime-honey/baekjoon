from collections import defaultdict


def solution(id_list, report, k):
    record = defaultdict(set)
    email = [0 for i in range(len(id_list))]

    for data in report:
        temp = data.split()
        record[temp[1]].add(temp[0])

    for names in record.values():
        if len(names) >= k:
            for name in names:
                email[id_list.index(name)] += 1

    return email