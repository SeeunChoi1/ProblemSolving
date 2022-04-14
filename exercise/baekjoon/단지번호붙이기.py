import sys
from typing import Counter
sys.stdin = open("input.txt", "r")

n = int(input())

# map정보 입력받기 (map자체가 literable)
graph = [list(map(int, input())) for _ in range(n)]
#visited = [[False]*n]*n

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0 #아파트 단지
answer = []

# 1. 상하좌우를 살펴본 뒤 주변지점에서 1이고 아직 방문하지 않으면 방문함
# 2. 1을 반복하면서 연결된 모든 아파트에 방문
# 3. 단지번호로 graph값 update하면서 count update
def dfs(x, y):
    if 0<=x<n and 0<=y<n:
        if graph[x][y] == 1:
            global cnt
            cnt += 1
            graph[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
    return False #out of range

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            answer.append(cnt)
            cnt = 0

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])