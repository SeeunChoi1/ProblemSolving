import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n = int(input())
list = []
today = 0
possible = []
ans = 0

for _ in range(0,n):
    d,w = map(int, input().split())
    list.append((d,w))
list.sort() #남은날짜기준 [(1, 20), (2, 50), (3, 30), (4, 10), (4, 40), (4, 60), (6, 5)]
today = list[-1][0] #6

while True:
    print(">>>", today, possible, ans)
    if today == 0 :
        break
    while list and list[-1][0]==today:
        possible.append(list.pop()[1])
    today -= 1
    possible.sort()
    if possible:
        ans += possible.pop()
    else: 
        ans += 0
        
print(ans)