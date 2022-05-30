def solution(s):
    mid_index = len(s)//2
    return s[mid_index] if len(s)%2 else s[mid_index-1]+s[mid_index]