import sys
sys.stdin = open("input.txt", "r")

n = int(input())
for _ in range(n):
    m = int(input())
    amount_list = list(map(int, input().split())) #[10, 7, 6]
    stock_cnt = 0 #보유주식수
    income = 0 #수익금
    invest = 0 #투자금
    
    next_max_idx = []
    max = [-1, -1] #idx, amount
    for i in reversed(range(m)):    
        if amount_list[i] > max[1]:
            max[0] = i
            max[1] = amount_list[i]            
            next_max_idx.append(-1)
        else:
            next_max_idx.append(max[0])

    next_max_idx.reverse() #[2,2,-1,4,-1]

    for i in range(m):
        if next_max_idx[i] == -1: #매도
            if stock_cnt == 0:
                continue
            else:                
                income += stock_cnt*amount_list[i]-invest
                stock_cnt = 0
                invest = 0
        else: #매수
            stock_cnt += 1
            invest += amount_list[i]

    print(income)
        