import sys
sys.stdin = open("input.txt", "r")

univ_num, road_num = map(int, sys.stdin.readline().split())
univ_gender = [' '] + list(sys.stdin.readline().split()) #남학교 M, 여학교 W
parent = [i for i in range(univ_num+1)]
edges = []
path_cost = 0
path_sum = 0

for _ in range(road_num):
    u,v,d = map(int, sys.stdin.readline().split())
    edges.append([d,u,v])
edges.sort()

def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parnet(u,v):
    u = find_parent(u)
    v = find_parent(v)
    if u<v:
        parent[v] = u
    else:
        parent[u] = v

#최소신장트리 MST
for edge in edges:
    cost, u, v = edge
    if univ_gender[u] != univ_gender[v] and find_parent(u) != find_parent(v):
        union_parnet(u,v)
        path_cost += cost
        path_sum += 1

if path_sum == univ_num-1: #경로가 n-1개일 경우에만 MST가 완성
    print(path_cost)
else:
    print(-1)