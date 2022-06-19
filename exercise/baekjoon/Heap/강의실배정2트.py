import sys
import heapq
sys.stdin = open("input.txt", "r")

num_classes = int(sys.stdin.readline())
schedule = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(num_classes)])
heap = []

for start, end in schedule:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))