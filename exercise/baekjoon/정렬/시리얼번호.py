import sys
sys.stdin = open("input.txt", "r")

n = int(input())
s_list = []
#짧은게먼저
#자리수합이 작은게 먼저(숫자만더함)
#사전순
def sum(serial):
    amount = 0
    for i in serial:
        if i.isdigit():
            amount += int(i)
    return amount

for _ in range(n):
    s_list.append(input())

s_list.sort(key = lambda x : (len(x),sum(x),x))

for s in s_list:
    print(s)