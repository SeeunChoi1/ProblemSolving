import sys
from collections import deque
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline().strip()

try:
    while input():
        n = int(input())
        print(n)
        list  = list(map(int,input().split()))

        hist = []
        stack = []

        for i in range(0,n):
            insert = list[i]
            if stack: #stack이 비어있지않을때
                if insert <= stack[-1]: #오름세가 아님
                    hist.append(len(stack))
                    stack = []
                elif insert > stack[-1]: #오름세Hist에 insert
                    stack.append(list[i])
            else: #stack이 비었음
                stack.append(list[i])
        #계속오름세이기만하면stack초기화를안함
        hist.append(len(stack))

        print(max(hist))
except: exit()