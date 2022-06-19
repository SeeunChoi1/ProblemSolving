import sys
from collections import deque
sys.stdin = open("input.txt", "r")

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
print(graph)

dx, dy, dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1] #상하좌우앞뒤
ans = 0
queue = deque([])

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1: 
                queue.append([k,i,j])

def bfs():
    while queue:
        v = queue.popleft()
        for i in range(6):
            nx = v[1]+dx[i]
            ny = v[2]+dy[i]
            nz = v[0]+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[v[0]][v[1]][v[2]]+1
                queue.append([nz,nx,ny])

bfs() #돌리면서 토마토를 익힘

#다돌았는데 안익은게 있으면 return -1
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                print(-1)
                exit(0)
            ans = max(ans, graph[z][x][y])

# for layer in graph:
#     for row in len(layer):
#         for elem in row:
#             if elem == 0:
#                 print(-1)
#                 exit(0)

print(ans-1)