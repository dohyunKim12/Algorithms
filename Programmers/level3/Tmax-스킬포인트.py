def solution(total_sp, skills):
    skills_dict = {}
    skills_rvs = []
    tmp_list = []
    for skill in skills:
        tmp_list.append(skill[0])
        tmp_list.append(skill[1])

        skills_rvs.append(skill[1])

    for skill_nu in tmp_list:
        skills_dict[skill_nu] = tmp_list.count(skill_nu)

    skills_list = sorted(skills_dict.items(), key=lambda item: item[1])

    if skills_list[0][0] in skills_rvs:
        start_skill = skills_list[0][0]
    else:
        start_skill = skills_list[1][0]
    print(skills_rvs)
    print(skills_list)
    print(start_skill)

    # use bfs
    first_sp = 1
    while True:
        for i in range(0, len(skills)+1):
            skills[i].append(skills[i])

        first_sp += 1

    return sp_ary


total_sp = 13
skills = [
    [2, 3],
    [3, 1],
    [4, 2],
]

solution(total_sp, skills)
