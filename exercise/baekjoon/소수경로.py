import sys
from collections import deque
sys.stdin = open("input.txt", "r")

# # 소수판정method
# def isPrimeNumber(num):
#     cnt = 2
#     if num == 1:
#         return False
#     while (cnt<num):
#         if num%cnt == 0:
#             return False
#         cnt += 1
#     return True

# # 소수여부map
# arr = [False for _ in range(10000)]
# for i in range(1000,10000):
#     arr[i] = isPrimeNumber(i)

def bfs(start, end, arr):
    # 조합 가능한 소수를 모두 큐에 넣고
    queue = deque([(start,0)])
    while queue:
        now, cnt = queue.popleft()
        if now == end:
            return cnt
        nowStr = str(now) # 각 자리의 수를 바꾸기 위한 String 형변환
        cnt += 1 
        for i in range(4):
            for j in map(str,range(10)):
                if i == 0 and j == '0': # 천의자리 0
                    continue 
                num = int(nowStr[:i] + j + nowStr[i+1:]) # 만든수
                if arr[num] and not visited[num]: # 만든수가 소수인지 판별
                    visited[num] = True
                    queue.append((num,cnt))


# 소수판정(에라토스테네스의 체)
m = 10000
arr = [False, False] + [True]*(m-1)
for i in range(2, m+1):
    if arr[i]:
        for j in range(2*i, m+1, i):
            arr[j] = False

n = int(input())
for _ in range(n):
    visited = [False] * 10000
    start, end = map(int, input().split())
    print(start, arr[start], end, arr[end])

    #bfs
    print(bfs(start, end, arr))

