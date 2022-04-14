import sys
import heapq
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
ans = []
heap = [] #min_heap

for _ in range(n):
    s,t = map(int, sys.stdin.readline().split())
    ans.append([s,t])
ans.sort(key=lambda x: x[0])
heapq.heappush(heap,ans[0][1]) #끝나는시간

for i in range(1,n):
    if heap[0]<= ans[i][0]: #안겹침
        heapq.heappop(heap)
        heapq.heappush(heap,ans[i][1])  
    else: #겹침
        heapq.heappush(heap,ans[i][1])
        
print(len(heap))