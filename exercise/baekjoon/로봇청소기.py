import sys
sys.stdin = open("input.txt", "r")

n,m = map(int, input().split())
r,c,d = map(int, input().split()) #0북,1동,2남,3서
graph = [[] for _ in range(n)]
visited = [[0]*m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))
dir = [[-1,0],[0,1],[1,0],[0,-1]] #북동남서

visited[r][c] = 1
cnt = 1

while(True):
    flag = False
    for _ in range(4):          
        #왼쪽을 확인한다 북->서(0->3), 동->북(1->0), 남->동(2->1), 서->남(3->2)
        nr = r + dir[(d+3)%4][0]
        nc = c + dir[(d+3)%4][1]
        d = (d+3)%4
        if 0<=nr<n and 0<=nc<m and graph[nr][nc]==0: #왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1 #현재 위치를 청소한다
                cnt+=1
                r = nr
                c = nc #한 칸을 전진  
                flag = True
                break  

    if not flag: #네 방향 모두 청소가 이미 되어있거나 벽인 경우
        if graph[r-dir[d][0]][c-dir[d][1]]==1: #뒤쪽 방향이 벽이라 후진도 할 수 없는 경우
            print(cnt)
            break
        else: 
            r = r- dir[d][0]
            c = c- dir[d][1] #바라보는 방향을 유지한 채로 한 칸 후진