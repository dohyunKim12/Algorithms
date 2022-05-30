def solution(new_id):
    # step 1
    new_id = new_id.lower()

    # step 2
    excpt_str = []
    for i in new_id:
        if ((i == '-') or (i == '_') or (i == '.')):
            continue
        elif (i.isnumeric()):
            continue
        elif (i.isalpha()):
            continue
        else:
            excpt_str.append(i)

    for i in range(len(excpt_str)):
        new_id = new_id.replace(excpt_str[i], '')

    # step 3
    for i in range(len(new_id)-1):
        if ((new_id[i] == new_id[i+1]) and (new_id[i] == '.')):
            pre_new_id = new_id[:i]+' '+new_id[i+1:]
            new_id = pre_new_id
    new_id = new_id.replace(' ', '')

    # step 4
    if (len(new_id) == 1 and new_id[0] == '.'):
        new_id = ''
    else:
        if (new_id[0] == '.'):
            new_id = new_id[1:]
        if (new_id[-1] == '.'):
            new_id = new_id[:-1]

    # step 5
    if (not new_id):  # 빈 문자열이면
        new_id = 'a'

    # step 6
    if (len(new_id) >= 16):
        new_id = new_id[:15]
        if (new_id[-1] == '.'):
            new_id = new_id[:-1]

    # step 7
    if (len(new_id) <= 2):
        while (1):
            new_id = new_id+new_id[-1]
            if (len(new_id) == 3):
                break

    return new_id