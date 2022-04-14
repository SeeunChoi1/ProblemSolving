import sys
sys.stdin = open("input.txt", "r")

while True:
    try:
        target = int(input())
        start = 1
        # 2<=target<=9 무조건 Baekjoon win
        # 10<=target<=18 무조건(가장 작은 2를 내도) Donghyuk win 
        while True:
            start *= 9 #9
            if target<=start:
                print("Baekjoon wins.")
                break
            start *= 2 #18
            if target<=start:
                print("Donghyuk wins.")
                break
    except EOFError:
        break