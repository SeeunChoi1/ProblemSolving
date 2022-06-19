import sys
from collections import deque
sys.stdin = open("input.txt", "r")

m, n = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n)]

direction = [[0,1],[0,-1],[1,0],[-1,0]] #상하좌우
ans = 0
queue = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: 
            queue.append([i,j])

def bfs():
    while queue:
        v = queue.popleft()
        for d in direction:
            nx = v[0]+d[0]
            ny = v[1]+d[1]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[v[0]][v[1]]+1
                queue.append([nx,ny])

bfs() #돌리면서 토마토를 익힘

#다돌았는데 안익은게 있으면 return -1
for row in graph:
    for j in row:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(row))

print(ans-1)