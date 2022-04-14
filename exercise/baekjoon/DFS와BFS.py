import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, m, v = map(int, input().split())
# print(n, m, v )

# graph = [[0]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     row, col = map(int, input().split())
#     graph[row][col] = graph[col][row] = 1
graph = [[] for _ in range(n+1)]

for _ in range(m):
    row, val = map(int, input().split())
    graph[row].append(val)
    graph[val].append(row)
for i in range(n+1):
    graph[i].sort()
# print(graph)

dfsVisited = [False] * (n+1)
bfsVisited = [False] * (n+1)

# Depth-First Search 깊이 우선 탐색
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리
#    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
# 3. 더 이상 2번을 수행할 수 없을 때까지 반복함
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        # print(graph[v])
        if not visited[i]:
            dfs(graph, i, visited)

# Breadth-First Search 너비 우선 탐색
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. 더 이상 2번을 수행할 수 없을 때까지 반복함
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# print("dfs : ", end=" ")
dfs(graph, v, dfsVisited)
print("")
# print("bfs : ", end=" ")
bfs(graph, v, bfsVisited) 
