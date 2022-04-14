import sys
sys.stdin = open("input.txt", "r")

n = int(input()) #전체사람수
start, end = map(int, input().split()) #7 3
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

#양방향 그래프
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)

def dfs(start):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = visited[start]+1
            dfs(i)

dfs(start)
ans = visited[end] if visited[end]!=0 else -1
print(ans)