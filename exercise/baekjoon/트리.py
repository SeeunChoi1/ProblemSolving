import sys
sys.stdin = open("input.txt", "r")

case_no = 1
while(True):
    input_case = input()
    if input_case=='0 0': #입력마지막
        exit(0)

    n, m = map(int, input_case.split()) #정점,간선
    num_of_tree = 0
    recursiveYn = False #순환여부

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    isRecursive = [0] * (n+1)

    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
    # print(graph)

    #dfs선언
    def dfs(graph, v, visited, edge, vertax):
        stack = []
        global num_of_tree
        global recursiveYn
        stack.append(v)
        while stack:
            v = stack.pop()
            vertax += 1
            # print(v)
            if not visited[v]:
                visited[v] = True
                for i in graph[v]:
                    stack.append(i)
                    edge += 1
                    if visited[i]: recursiveYn = True #순환체크
        if not recursiveYn and edge == vertax-1: #순환제외 && 정점이 n개, 간선이 n-1개
            num_of_tree += 1 
        recursiveYn = False #초기화
        # print('---',num_of_tree, recursiveYn, edge, vertax)

    for i in range(1,n+1):
        if not visited[i]:
            edge, vertax = 0,0
            dfs(graph, i, visited, edge, vertax)
    
    # print('final visited:',visited)

    #정답출력
    print("Case ", case_no, ":", sep='', end=' ')
    if num_of_tree <= 0:
        print('No trees.')
    elif num_of_tree == 1:
        print('There is one tree.')
    else:
        print('A forest of',num_of_tree,'trees.')
    # print('================')
    case_no += 1