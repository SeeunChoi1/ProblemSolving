import sys
sys.stdin = open("input.txt", "r")

n = int(input())
scv_list = list(map(int, input().split()))

if len(scv_list)==1:
    scv_list += [0,0]
elif len(scv_list)==2:
    scv_list += [0]
# print(scv_list)

visited = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]

def run(s1, s2, s3):
    if (s1==0 and s2==0 and s3==0): #다죽음
        return visited[s1][s2][s3]

    if s1<0: return run(0,s2,s3)
    if s2<0: return run(s1,0,s3)
    if s3<0: return run(s1,s2,0)

    #똑같은거 제외 
    if visited[s1][s2][s3] != 0: return visited[s1][s2][s3]
    
    visited[s1][s2][s3] = float('inf')
    visited[s1][s2][s3] = min(visited[s1][s2][s3],run(s1-9,s2-3,s3-1)+1)
    visited[s1][s2][s3] = min(visited[s1][s2][s3],run(s1-9,s2-1,s3-3)+1)
    visited[s1][s2][s3] = min(visited[s1][s2][s3],run(s1-1,s2-9,s3-3)+1)
    visited[s1][s2][s3] = min(visited[s1][s2][s3],run(s1-1,s2-3,s3-9)+1)
    visited[s1][s2][s3] = min(visited[s1][s2][s3],run(s1-3,s2-1,s3-9)+1)
    visited[s1][s2][s3] = min(visited[s1][s2][s3],run(s1-3,s2-9,s3-1)+1)

    return visited[s1][s2][s3]

ans = run(scv_list[0],scv_list[1],scv_list[2])
print(ans)