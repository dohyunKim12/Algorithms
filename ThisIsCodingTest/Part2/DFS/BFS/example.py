INF = 999999999
########################################
# # Factorial Iterative vs Recursive
# def factorial_iterative(n):
#     res = 1
#     for i in range(1, n+1):
#         res *= i
#     return res


# def factorial_recursive(n):
#     if n <= 1:
#         return 1
#     return factorial_recursive(n-1) * n


# print(factorial_iterative(4))
# print(factorial_recursive(4))

########################################
# # Adjacency matrix

# graph = [
#     [0, 7, 5],
#     [7, 0, INF],
#     [5, INF, 0],
# ]

# print(graph)

########################################
# # Adjacency List
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))
graph[2].append((1, 5))

print(graph)
