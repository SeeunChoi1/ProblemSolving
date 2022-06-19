import sys
from collections import deque
sys.stdin = open("input.txt", "r")

input = input()

# for i in range(0,len(input)-3):
#     if input[i:i+4] == "PPAP":
#         input = input.replace("PPAP","P")
#     if input=="PPAP" or input=="P":
#         print("PPAP")
#         break
# if input != "PPAP" and input != "P":
#     print("NP")

stack = []
ppap = ["P", "P", "A", "P"]

if input == "P" or input == "PPAP":
    print("PPAP")
else:
    for i in input:
        stack.append(i)
        if stack[-4:] == ppap:
            stack.pop()
            stack.pop()
            stack.pop()

    if stack == ppap or stack == ["P"]:
        print("PPAP")
    else:
        print("NP")
