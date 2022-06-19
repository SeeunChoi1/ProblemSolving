import sys
sys.stdin = open("input.txt", "r")

node_num, root = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(node_num+1)]

for _ in range(node_num-1):
    start,end,weight = map(int, sys.stdin.readline().split())
    tree[start].append([end,weight])

#기가노드 구하기 + 기둥길이 구하기
giga = 0
pillar_len = 0
visited = [False]*(node_num+1)
stack = [root]
while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = True
        if len(tree[v]) > 1:
            giga = v
            break
        else:
            pillar_len += tree[v][0][1]
            stack.append(tree[v][0][0])
print(giga)
print(pillar_len, end=' ')

#가장긴가지 구하기
branch_len = []
for branch in tree[giga]:
    tmp = 0
    stack = [branch[0]]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            tmp += branch[1]
    branch_len.append(tmp)
print(branch_len)