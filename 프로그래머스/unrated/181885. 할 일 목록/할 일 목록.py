def solution(todo_list, finished):
    answer = list()
    for index, todo in enumerate(todo_list):
        if not finished[index]: answer.append(todo)
    return answer