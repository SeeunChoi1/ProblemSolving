def solution(lottos, win_nums):
    answer = [0,0]
    zero_num = 0
    count = 0
    
    for lotto in lottos:
        if lotto == 0:
            zero_num += 1
    
    for i in range(6):
        for j in range(6):
            if lottos[i] == win_nums[j]:
                count += 1
    
    if zero_num == 6:
        answer[0] = 1
        answer[1] = 6
    elif zero_num == 0 and count == 0:
        answer[0] = 6
        answer[1] = 6
    else:
        answer[0] = 7-(count+zero_num)
        answer[1] = 7-count
    
    return answer