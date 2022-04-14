import sys
from collections import deque
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline().strip()

n = int(input())
list = sys.stdin.readline().split(" ") #9 5 4 8
stack = [] # 5 8
ans = []

for i in reversed(range(n)):
    while stack: 
        if stack[-1] > int(list[i]): #오큰수
            break
        else:
            stack.pop()
    if stack:
        ans.append(stack[-1])
        stack.append(int(list[i]))
    if not stack:
        ans.append(-1)
        stack.append(int(list[i]))

ans.reverse()
for a in ans:
    print(a, end=" ")
