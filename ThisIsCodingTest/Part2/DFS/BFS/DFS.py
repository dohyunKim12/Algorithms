# dfs 는 깊이우선탐색(가장 먼 곳의 노드부터 탐색) -> 재귀적으로 구현하면 쉽다!!! ( 재귀적 함수는 깊은 곳 까지 가서 return, return 해 오기 때문에..)
# recursion 을 이용한 방식은 간결하나, stack을 이용한 방식보다 시간복잡도가 더 안좋음.

##########################################
# WAY 1. Implement dfs using recursion
# Original (book)
# Recursion의 원리를 이용.
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리.
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문.
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)


##########################################
# WAY 2. Implement dfs using Stack

def dfs_with_stack(graph, v, visited):
    stack = []
    print(v, end=' ')
    stack.append(v)
    visited[v] = True

    while(True):
        for idx, node in enumerate(graph[v]):
            # 방문하지 않은 놈을 stack에 넣고, break문을 통해 다시 새로운 v를 이용하여 for문으로 들어오도록 만들기.
            if not visited[node]:
                v = node
                stack.append(v)
                print(v, end=' ')
                visited[v] = True
                break
            if idx == len(graph[v]) - 1:  # last node, but all visitied
                # stack에서 맨 위 요소 제거하고, 그 바로 밑에 애를 v 로 다시 잡음.
                stack.pop()
                if stack:   # empty stack에서 -1번째 element를 참조하는 오류 방지.
                    v = stack[-1]

        # stack 이 비었으면, 종료.
        if not stack:
            break


# graph 를 Adjacency List (연결 리스트) 로 표현.
graph = [
    [],         # 0번 vertex
    [2, 3, 8],  # 1번 vertex 의 adjacent node
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9  # (0번부터 9개의 vertex가 있다고 가정.)

# dfs_with_stack(graph, 1, visited)
