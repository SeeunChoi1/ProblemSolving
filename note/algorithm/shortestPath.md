# 최단경로 알고리즘
- 가장 짧은 경로를 찾는 알고리즘 

## 다익스트라 알고리즘
- 여러 개의 노드가 있을 때 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구하는 알고리즘
    - 기본적으로 그리디
    - 매번 **가장 비용이 적은 노드** 선택
    - 각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트(최단 거리 테이블)에 저장하며 리스트를 계속 갱신함
- 음의 간선(0보다 작은 값을 갖는 간선)이 없을 때 정상 작동함
- GPS 소프트웨어의 기본 알고리즘

### 전체 흐름
1. 출발 노드를 선택함
2. 최단 거리 테이블을 초기화함
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택함
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신함 (그리디)
5. 위 과정에서 3번과 4번을 반복함
    - 다음 노드를 고를 때는 방문하지 않은 노드 중에서 최단 거리가 짧은 것 선택
    - 최단 거리가 같으면 번호가 작은 것
- 한 번 선택된 노드는 최단 거리가 감소하지 않는다
- 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것
- 마지막 노드에 대해서는 해당 노드를 거쳐 다른 노드로 가는 경우를 확인할 필요가 없음
    - 나머지 노드에 대한 최단 거리가 확정된 상태이므로 더 이상 테이블이 갱신될 수 없음

### 구현 1(쉽지만 느림)
- o(V^2)의 시간복잡도
    - V는 노드의 갯수
- 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)함
- 노드 개수가 5,000개 이하면 가능
- 노드 개수가 10,000개 넘어가면 불가능
```python
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
# 시작 노드 번호를 인력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b로 가는 비용이 c임
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드(다음에 갈 노드)를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```

### 구현 2(까다롭지만 빠름)
- o(ElogV)의 시간복잡도
    - E : 간선의 개수
    - V : 노드의 개수
- 최단 거리가 가장 짧은 노드를 선형적으로 찾는 것이 아니라면? => [힙 자료구조](../dataStructure/prqueue_heap.md) 사용 
- 최단 거리가 가장 짧은 노드를 선택하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체함

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
# 시작 노드 번호를 인력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b로 가는 비용이 c임
    graph[a].append((b,c))

def dijsktra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

# 다익스트라 알고리즘 수행
dijsktra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```
- while문은 노드의 개수 v 이상의 횟수로는 반복되지 않음

## 플로이드-워셜 알고리즘
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
- 단계마다 거쳐 가는 노드를 기준으로 알고리즘 수행
    - 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없음
- 총 시간 복잡도 O(n^3)
    - 2차원 리스트에 최단 거리 정보를 저장함
    - 모든 노드에 대하여 다른 모든 노드로 가는 최단 거리 정보를 담아야하기 때문
    - n번의 단계에서 매번 O(n^2)의 시간이 소요됨
- 매 단계에서 점화식에 맞는 2차원 리스트 갱신 ← **DP**  
    - $D_{ab} = min(D_{ab}, D_{ak}+D_{kb})$
    - A에서 B로 가는 최소 비용과 A에서 K를 거쳐 B로 가는 비용을 비교하여 더 작은 값으로 갱신

### 예시 코드
```python
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
	for b in range(1, n+1):
		if a==b:
			graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
	# A에서 B로 가는 비용은 C라고 설정
	a, b, c = map(int, input().split())
	graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
	for a in range(1, n+1):
		for b in range(1, n+1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
	for b in range(1, n+1):
		if graph[a][b] == INF: # 도달할 수 없는 경우, "INFINITY" 출력
			print("INFINITY", end = " ")
		else: # 도달할 수 있는 경우 거리를 출력
			print(graph[a][b], end = " ")
	print()
```

## 벨만-포드 알고리즘