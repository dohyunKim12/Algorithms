def solution(s):
    if len(s) == 1:
        return 1
    ans_list = []
    for unit in range(1, len(s)//2 + 1):
        res_list = []
        tmp_string = s
        tmp_list = []
        while tmp_string:
            tmp_list.append(tmp_string[:unit])
            tmp_string = tmp_string[unit:]

        cnt = 1
        for i in range(len(tmp_list)-1):
            if tmp_list[i] == tmp_list[i+1]:
                cnt += 1
            else:
                if cnt > 1:
                    res_list.append(str(cnt)+tmp_list[i])
                else:
                    res_list.append(tmp_list[i])
                cnt = 1
            if i == len(tmp_list) - 2:
                if cnt > 1:
                    res_list.append(str(cnt)+tmp_list[i+1])
                else:
                    res_list.append(tmp_list[i+1])

        res_str = ''.join(res_list)
        ans_list.append(res_str)
    for i in range(len(ans_list)):
        ans_list[i] = len(ans_list[i])

    return min(ans_list)


# print(solution('aabbaccc'))
# print(solution('abcabcabcabcdededededede'))
# print(solution('ababcdcdababcdcd'))
# print(solution('aaaaaaaaaaaaaaabbbbbbbbbbc'))
print(solution('a'))
