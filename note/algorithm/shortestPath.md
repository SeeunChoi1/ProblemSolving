# 최단경로 알고리즘
- 가장 짧은 경로를 찾는 알고리즘 

## 다익스트라 알고리즘

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