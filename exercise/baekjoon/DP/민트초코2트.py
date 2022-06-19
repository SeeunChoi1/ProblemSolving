import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
exp = list(sys.stdin.readline().split())

# 소수판정(에라토스테네스의 체)
m = 100000
arr = [False, False, False] + [True]*(m-1)
for i in range(2, m+1):
    if arr[i]:
        for j in range(2*i, m+1, i):
            arr[j] = False
def excep(n):
    if n<0: 
        n *= -1
    elif n==0:
        print('mint chocolate')
        exit(0)

#소인수분해
def top(n):
    excep(n)
    for i in range(2,n+1): 
        while not arr[n]: #소수가아니면
            if n%i==0:
                arr[i] += 1
                n = n//i
        print(n)
def bottom(n):
    excep(n)
    for i in range(2,n+1):
        while not arr[n]: #소수가아니면
            if n%i==0:
                arr[i] -= 1
                n = n//i
        print(n)

for i in range(len(exp)):
    if i%2 == 1: #연산자
        if exp[i] == '/': #분모
            bottom(int(exp[i+1]))
        elif exp[i] == '*': #분자
            top(int(exp[i+1]))