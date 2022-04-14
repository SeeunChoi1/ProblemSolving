import sys
sys.stdin = open("input.txt", "r")

n = int(input())
s_list = []

for _ in range(n):
    s_list.append(input())

#투포인터

# 자리수합이 작은게 먼저(숫자만더함)
# 사전순
for i in range(0,n-1):
    for j in range(i+1,n):
        if len(s_list[i]) > len(s_list[j]): # 짧은게먼저
            s_list[i], s_list[j] = s_list[j], s_list[i]
        elif len(s_list[i]) == len(s_list[j]):
            sum_i = 0
            sum_j = 0
            for x in s_list[i]:
                if x.isdigit(): sum_i += int(x)
            for y in s_list[j]:
                if y.isdigit(): sum_j += int(y)
            if sum_i > sum_j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
            elif sum_i == sum_j:
                for x,y in zip(s_list[i],s_list[j]):
                    if x>y:
                        s_list[i], s_list[j] = s_list[j], s_list[i]
                        break
                    elif x<y:
                        break
for s in s_list:
    print(s)