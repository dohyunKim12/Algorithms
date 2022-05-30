def solution(citations):
    ans = 0
    j = 0
    for k in range(max(citations)):
        cnt = 0
        for i in citations:
            if i >= j:
                cnt += 1

        if j == cnt :
            ans = j
            break
        elif j <= cnt:
            ans = j
        j += 1

    return ans