import sys
sys.stdin = open("input.txt", "r")

n = int(input()) #컴퓨터수
v = int(input()) #edge갯수

graph = [[] for _ in range(n+1)]

for _ in range(v):
    row, val = map(int, input().split())
    graph[row].append(val)
    graph[val].append(row)

visited = [False]* (n+1)
cnt = 0

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v] :
        if not visited[i]:
            cnt += 1
            dfs(graph,i,visited)

dfs(graph,1,visited)
print(cnt)