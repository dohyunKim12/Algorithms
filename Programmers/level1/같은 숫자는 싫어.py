def solution(arr):
    ans = []
    tmp = -1
    for i in arr:
        if i != tmp:
            ans.append(i)
        tmp = i
    return ans