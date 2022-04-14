import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
exp = list(sys.stdin.readline().split())

if int(exp[0]) == 0:
    print('mint chocolate')
    exit(0)
top = int(exp[0]) #분자
bottom = 1 #분모
for i in range(len(exp)):
    if i%2 == 1: #연산자
        if exp[i] == '/':
            bottom = bottom * int(exp[i+1])
        elif exp[i] == '*':
            if int(exp[i+1])==0:
                print('mint chocolate')
                exit(0)
            else:
                top = top * int(exp[i+1])
#정수 -> 민트초코
#유리수 -> 치약
if top%bottom == 0:
    print('mint chocolate')
else:
    print('toothpaste')
