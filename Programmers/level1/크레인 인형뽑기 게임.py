def solution(board, moves):
    l = []
    for i, val in enumerate(moves):
        for j in range(len(board[0])):
            if board[j][val-1] != 0:
                l.append(board[j][val-1])
                board[j][val-1] = 0
                break

    cnt = 0

    while(1):
        prev_cnt = cnt
        for i in range(len(l)-1):
            prev = l[i]
            next = l[i+1]
            if prev == next : 
                l.pop(i)
                l.pop(i)
                cnt += 2
                break
        if prev_cnt == cnt:
            break


    return cnt