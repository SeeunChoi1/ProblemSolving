import sys
sys.stdin = open("input.txt", "r")

n = int(input())
for _ in range(n):
    m = int(input())
    amount_list = list(map(int, input().split())) #[10, 7, 6]
    income = 0 #수익금
    prev_max = amount_list[-1]

    #거꾸로 for문
    ##등락은 중요하지 않고 최대값나오면 매도가 중요!
    for i in reversed(range(m-1)):
        if amount_list[i] > prev_max:
            prev_max = amount_list[i]
        else:
            income += prev_max - amount_list[i] #어짜피이가격에팔거니까

    print(income)