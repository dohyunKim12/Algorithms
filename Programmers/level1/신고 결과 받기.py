def solution(id_list, report, k):
    # 먼저, 신고당한 사람이 정지되었는지 여부를 판별한다. 정지되었으면, dictionary로 해당 id의 value를 특정 값으로 만들어 표기하고
    # 마지막에 id_list에 존재하는 순차적으로 2차원 list의 report에서 신고한 id의 dict value를 찾아 그것이 특정 값이면 res_dict에 value를 증가시킨다.

    res_dict = {key: 0 for key in id_list}
    banned_dict = res_dict.copy()

    report = set(report)
    report = list(report)

    for val in report:
        tmp_l = val.split(' ')
        banned_dict[tmp_l[1]] += 1    # 신고횟수 누적.
        if banned_dict[tmp_l[1]] >= k:
            banned_dict[tmp_l[1]] = -999  # 정지횟수 이상이면 음수로 설정.

    for val in report:
        tmp_l = val.split(' ')
        if banned_dict[tmp_l[1]] < 0:
            res_dict[tmp_l[0]] += 1

    print(banned_dict)

    return list(res_dict.values())


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo",
                                                    "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))