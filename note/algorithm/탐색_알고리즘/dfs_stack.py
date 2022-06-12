def dfs(graph, start, visited):
    stack = []
    stack.append(start)
    #현재 노드와 연결된 다른 노드를 stack에서 pop
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = True # 방문처리
            print(now, end=' ')
            for i in graph[now]:
                if not visited[i]:
                    stack.append(i)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
dfs(graph, 1, visited)