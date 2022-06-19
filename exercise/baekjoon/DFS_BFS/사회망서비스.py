import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
node_list = [i for i in range(1,n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u) #양방향
dp = [[0,0] for _ in range(n+1)] #중복저장(서브트리를 다 얼리어답터로 만드는 최소값)
#[0]: 얼리어답터 O
#[1]: 얼리어답터 X
visited = [False]*(n+1)

def dfs(start):
    visited[start] = True
    dp[start][0] = 1 #내가 얼리어답터니까
    for elem in graph[start]:
        if not visited[elem]:
            dfs(elem)
            dp[start][0] += min(dp[elem][0],dp[elem][1]) #얼리어답터O -> child상관없음
            dp[start][1] += dp[elem][0] #얼리어답터X -> child가얼리어답터
dfs(1)
print(min(dp[1][0],dp[1][1])) #1까지왔음 -> 다 얼리어답터임