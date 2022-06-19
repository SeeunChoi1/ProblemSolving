import sys
sys.stdin = open("input.txt", "r")

n,m = map(int,input().split())
graph = [[]for _ in range(n)]
graph_cal = [[0]*m for _ in range(n)]
cnt = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False]*m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,input().split()))

#분리여부확인
def dfs(graph,x,y):
    if graph[x][y] == 0 or visited[x][y]:
        return
    visited[x][y] = True
    for i in range(4):
        dfs(graph,x+dx[i],y+dy[i])

while(cnt==1):
    #1년흐름
    for i in range(n):
        for j in range(m):
            if i-1>=0 and graph[i-1][j] == 0:
                graph_cal[i][j] += 1
            if i+1<n and graph[i+1][j] == 0:
                graph_cal[i][j] += 1
            if j-1>=0 and graph[i][j-1] == 0:
                graph_cal[i][j] += 1
            if j+1<m and graph[i][j+1] == 0:
                graph_cal[i][j] += 1
    #계산
    for i in range(n):
        for j in range(m):
            graph[i][j] -= graph_cal[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
            graph_cal[i][j] = 0   
    #시작점에서부터 나눠졌는지 확인
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(graph,i,j)
                cnt += 1
    print(visited)

print(cnt)
for g in graph:
    print(g)