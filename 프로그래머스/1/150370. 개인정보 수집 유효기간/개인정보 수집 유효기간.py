def solution(today, terms, privacies):
    def chk(date):
        if (now[0] > date[0] or
           now [0] == date[0] and (
           now[1] > date[1] or
           now[1] == date[1] and
           now[2] >= date[2])):
            return True
        return False


    answer = list()
    term = [0 for i in range(26)]
    now = list(map(int, today.split(".")))

    for data in terms:
        temp = data.split()
        term[ord(temp[0]) - ord('A')] = int(temp[-1])

    for index, privacy in enumerate(privacies):
        temp = privacy.split()
        start = list(map(int, temp[0].split(".")))
        start[1] += term[ord(temp[-1]) - ord("A")]

        if start[1] > 12:
            while start[1] > 12:
                start[1] -= 12
                start[0] += 1

        if chk(start):
            answer.append(index + 1)

    return answer