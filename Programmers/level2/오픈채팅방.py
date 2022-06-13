def solution(records):
    answer = []
    uid_dict = {}
    for rec in records:
        tmp_list = rec.split()
        if tmp_list[0] == 'Enter' or tmp_list[0] == 'Change':
            uid_dict[tmp_list[1]] = tmp_list[2]

    for rec in records:
        tmp_list = rec.split()
        if tmp_list[0] == 'Enter':
            answer.append(uid_dict[tmp_list[1]] + "님이 들어왔습니다.")
        elif tmp_list[0] == 'Leave':
            answer.append(uid_dict[tmp_list[1]] + "님이 나갔습니다.")

    return answer


records = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]

solution(records)
