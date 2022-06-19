import sys
sys.stdin = open("input.txt", "r")

n = int(input())
graph = []

for _ in range(n):
    #input받기
    dir = list(input().split('\\'))
    #edge표현
    if len(dir) == 1:
        graph.append([dir[0], ' '])
        continue
    for i in range(len(dir)-1):
        graph.append([dir[i], dir[i+1]])

#edge표현 hashmap {'WINNT' : ['DRIVERS', 'SYSTEM32']}
edges = {}
for elem in graph:
    edges[elem[0]] = edges.get(elem[0], []) + [elem[1]] if elem[1] != ' ' else []

#사전순출력
for e in edges:
    edges[e].sort()

print(edges)

#dfs
# stack = [edges.pop()]
# while stack:
#     top = stack.pop()
#     if top not in edges or len(edges[top]) == 0: #디렉토리끝
#         print(top)
#     else: #아직디렉토리남음
#         print(' '+edges[top][-1])
#         stack.append(edges[top][-1])
#         edges[top] = edges[top][:-1] #한번방문한곳은 edges에서 삭제