#  결과적으로 풀이는 맞았으나, 주석 잘 작성 요망.!!
#  전체적인 알고리즘은 같으나, 가독성 떨어진다는 점..
#  맞았으면 -> Refactoring!
#  이러한 방식 말고도, dx, dy를 활용하는 방법으로도 구현해 볼것.

n, m = map(int, input().split())
row, col, direct = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

# Map 초기화, 변수들 선언, 할당.

matrix[row][col] = -1  # Mark -1 for visited (최초 서있는 위치.)
cnt_visited = 1


def manual_2():
    check_val = check()

    turn_left()
    if check_val == 0:  # 왼쪽이 비어있으면, 왼쪽으로 턴하고 전진.
        go_straight()
        return True
    else:               # 그렇지 않으면, 그냥 왼쪽으로 턴만.
        return False


def manual_3():
    cnt = 0
    while(True):
        if manual_2() == True:  # 1회 전진하였으면 바로 True값 return.
            return True
        else:                   # 전진하지 못하고 턴만 하였으면, 아래 절차 진행. 4번동안 돌기만 하면 후진하도록.
            cnt += 1
            if cnt == 4:
                break

    if back_once() == False:    # 후진했는데, False값 (바다) 라면 False를 리턴하고 게임을 종료.
        # end game
        return False


def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3
    return


def check():
    if direct == 0:
        return matrix[row][col-1]  # check left
    elif direct == 1:
        return matrix[row-1][col]  # check upside
    elif direct == 2:
        return matrix[row][col+1]  # check right
    elif direct == 3:
        return matrix[row+1][col]  # check downside


def go_straight():
    global direct, row, col, cnt_visited
    if direct == 0:
        row -= 1
    elif direct == 1:
        col += 1
    elif direct == 2:
        row += 1
    elif direct == 3:
        col -= 1
    matrix[row][col] = -1  # Mark -1 for visited.
    cnt_visited += 1


def back_once():
    global direct, row, col, cnt_visited
    if direct == 0:
        row += 1
    elif direct == 1:
        col -= 1
    elif direct == 2:
        row -= 1
    elif direct == 3:
        col += 1
    if matrix[row][col] == 1:
        return False  # end game
    else:
        return True


while(True):
    resVal = manual_3()

    print(row, col)

    if resVal == False:
        break

print(cnt_visited)
