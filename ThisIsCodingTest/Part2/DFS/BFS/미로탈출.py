from collections import deque
from turtle import distance
n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    dx = [0, 0, 1, -1]  # 동 서 남 북
    dy = [1, -1, 0, 0]
    # 여기서는 x, y 가 x와 y축이라는 생각 버리고, 문제에서 주어진 2차원 행렬의 행과 열 이라는 생각을 해야함!!
    queue = deque()
    queue.append((x, y))
    while True:  # 또는 while queue 해도 됨. (큐가 빌 때까지 반복.)

        pop_node = queue.popleft()  # 하나 pop으로 꺼냄!
        for i in range(4):  # 동, 서, 남, 북 4개의 방향에 대하여 계산.
            nx = pop_node[0] + dx[i]
            ny = pop_node[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:  # map을 벗어나면 continue
                continue
            # 처음 방문(1)이면 큐에 넣고 거리값을 입력.
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[pop_node[0]][pop_node[1]] + 1
        if list(pop_node) == [n-1, m-1]:
            return graph[n-1][m-1]


print(bfs(0, 0))
