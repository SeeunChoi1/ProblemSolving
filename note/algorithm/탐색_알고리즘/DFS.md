# DFS
Depth-First Search 깊이 우선 탐색

### 재귀함수
: 자기 자신을 다시 호출하는 함수
> 무한대로 호출하면 RecursionError 발생  

재귀 함수를 문제풀이에서 사용하려면 종료 조건을 명시해야함
```python
def recursive_function(i):
    if i == 100: #100번째 출력하면 종료 조건 명시
        return
    recursive_function(i+1)
recursive_function(1)
```
컴퓨터 내부에서 재귀 함수의 수행은 스택을 이용함  
스택 자료구조를 사용하는 상당수 알고리즘은 재귀 함수로 구현 가능

## Graph 표현 유형
* 인접 행렬 (Adjacency Matrix) : 2차원 배열로 그래프 연결관계 표현
    ```python
    [[0,7,5],
    [7,0,99999999],
    [5,99999999,0]]
    ```
* 인접 리스트 (Adjacency List) : 리스트로 그래프 연결 관계 표현
    ```python
    [[(1,7),(2,5)],
    [(0,7)],
    [(0,5)]]
    ```
인접 행렬 방식은 모든 관계를 저장하므로 노드 갯수가 많을 수록 메모리 낭비
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문처리. 방문하지 않은 노드가 없으면 스택에서 최상단 노드를 꺼낸다
3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복함
> DFS 자체는 순서에 무관하지만 관행적으로 번호가 낮은 것부터 처리함

## 예시코드 - 재귀
```python
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
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
```

## 예시코드 - stack1
list 자료구조 활용
```python
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
```

## 예시코드 - stack2
- deque 자료구조 활용
- list 쓰는 것과 로직은 동일함
    - stack을 deque로 사용
    - 성능면에서 일반 list를 쓰는 것보다 더 뛰어남
```python
from collections import deque

def dfs(graph, start, visited):
    stack = deque()
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
```

[⬅️ 탐색](/note/algorithm/search.md)
[🏠 목록으로](/README.md)