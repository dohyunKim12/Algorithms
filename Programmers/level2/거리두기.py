def solution(places):
    answer = [1,1,1,1,1]
    
    for idx, place in enumerate(places):
        for j, row in enumerate(place):
            for k, el in enumerate(row):
                if(el == 'P'):
                    isSafe = check(place, j, k)
                    if (not isSafe):
                        answer[idx] = 0
                        break
            if answer[idx] == 0: break
    return answer

def check(place, j, k):
    if((j+2 <= 4 and place[j + 2][k] == 'P' and place[j+1][k] != 'X') or (0 <= j-2 and place[j - 2][k] == 'P' and place[j-1][k] != 'X') or (k+2 <= 4 and place[j][k+2] == 'P' and place[j][k+1] != 'X') or (0 <= k-2 and place[j][k-2] == 'P' and place[j][k-1] != 'X')):
        return 0

    if (j * k == 0 or j == 4 or k == 4): 
        if((j+1 <= 4 and place[j+1][k] == 'P') or (0 <= j-1 and place[j-1][k] == 'P') or (k+1 <= 4 and place[j][k+1] == 'P') or (0 <= k-1 and place[j][k-1] == 'P')):
            return 0
        if ((0 <= j-1 and 0<= k-1 and place[j-1][k-1] == 'P') and (place[j][k-1] != 'X' or place[j-1][k] != 'X')):
            return 0
        if ((j+1 <= 4 and k+1 <= 4 and place[j+1][k+1] == 'P') and (place[j][k+1] != 'X' or place[j+1][k] != 'X')):
            return 0
        if ((0 <= j-1 and k+1 <= 4 and place[j-1][k+1] == 'P') and (place[j-1][k] != 'X' or place[j][k+1] != 'X')):
            return 0    
        if ((j+1 <= 4 and 0 <= k-1 and place[j+1][k-1] == 'P') and (place[j+1][k] != 'X' or place[j][k-1] != 'X')):
            return 0
        else: return 1

    else:
        if(((j+1) * k >= 0 and place[j+1][k] == 'P') or place[j-1][k] == 'P' or place[j][k+1] == 'P' or place[j][k-1] == 'P'):
            return 0
        if (place[j-1][k-1] == 'P' and (place[j][k-1] != 'X' or place[j-1][k] != 'X')):
            return 0
        if (place[j+1][k+1] == 'P' and (place[j][k+1] != 'X' or place[j+1][k] != 'X')):
            return 0
        if (place[j-1][k+1] == 'P' and (place[j-1][k] != 'X' or place[j][k+1] != 'X')):
            return 0    
        if (place[j+1][k-1] == 'P' and (place[j+1][k] != 'X' or place[j][k-1] != 'X')):
            return 0
        else: return 1

    

def valid(x, y):
    if (x< 0 or x > 4 or y < 0 or y> 4) :
        return False
    else: return True


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))