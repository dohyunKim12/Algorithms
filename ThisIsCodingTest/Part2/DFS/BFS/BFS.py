# bfs 는 너비우선탐색
# dfs, bfs 모두 O(N)이지만, recursion의 dfs는 수행시간이 살짝 느림. --> 코테에서는 bfs가 조금 더 유리!

from collections import deque
from re import I


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:  # 큐가 빌 때 까지 계속 반복.
        pop_node = queue.popleft()
        print(pop_node, end=' ')
        # 꺼낸 node의 인접 노드들에 대하여 방문하지 않았으면, 전부 queue에 넣고 방문처리.
        for node in graph[pop_node]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

# bfs(graph, 1, visited)

val = 256-240
for i in range(257):
    if i % val == 0:
        print('~', i-1)
