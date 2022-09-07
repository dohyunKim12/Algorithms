from re import A


def solution(s):
    print(s)
    list_s = s.split(" ")
    print(list_s)
    for idx, el in enumerate(list_s):
        if(el == ''):
            continue
        if(el[0].isalpha()):
            list_s[idx] = el.capitalize()
        else:
            list_s[idx] = el.lower()

    print(list_s)        
    return ' '.join(list_s)

print(solution(" 3peOple unFollewed   me  "))
