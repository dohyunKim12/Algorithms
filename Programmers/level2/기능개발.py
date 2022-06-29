from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    ans = []
    while len(progresses) != 0:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt:
            ans.append(cnt)

    return ans 


progresses = [93,30,55]
speeds = [1, 30, 5]

solution(progresses, speeds)
