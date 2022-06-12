# BFS
Breadth-First Search 너비 우선 탐색

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리함
3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복  
일반적인 경우 실제 수행시간은 DFS보다 좋은 편

## 예시 코드
```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                visited[i] = True
graph = [
    [].
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
bfs(graph, 1, visited)
```
[⬅️ 탐색](/note/algorithm/search.md)
[🏠 목록으로](/README.md)