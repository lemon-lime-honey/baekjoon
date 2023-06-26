def solution(genres, plays):
    genre_cnt = dict()
    answer = list()
    
    for i in range(len(genres)):
        if genres[i] not in genre_cnt:
            genre_cnt[genres[i]] = [-plays[i], [(-plays[i], i)]]
        else:
            genre_cnt[genres[i]][0] -= plays[i]
            genre_cnt[genres[i]][1].append((-plays[i], i))

    genre_cnt_list = sorted(genre_cnt.items(), key=lambda x: x[1][0])

    for data in genre_cnt_list:
        data_sort = sorted(data[1][1])
        if len(data_sort) == 1:
            answer.append(data_sort[0][1])
        else:
            for i in range(2):
                answer.append(data_sort[i][1])

    return answer