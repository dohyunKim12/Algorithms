import enum


def solution(s):

    length = len(s)
    str = s
    cnt = 0

    for i in range(length):
        str = s[i:length] + s[:i]
        cnt += check(str)
    return cnt

def check(str):
    str = list(str)
    stack = []
    for el in str:
        if el in ['(','{','['] :
            stack.append(el)
        else:
            if (not stack): return False
            x = stack.pop()
            if x == '(' and el != ')':
                return 0
            if x == '{' and el != '}':
                return 0
            if x == '[' and el != ']':
                return 0
    return 1

print(solution("[](){}"))
print(solution("(){()}"))
print(solution("}}}"))
print(solution('{{{{{{{{{{{{{{){{{{{{{{{{{{{{([[[((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]}}}}}}}}}}}}}}}}}}}}}}}}}}}}'))