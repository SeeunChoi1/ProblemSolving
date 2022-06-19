import sys
sys.stdin = open("input.txt", "r")

start = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()
print(start,target)

# 문자열의 뒤에 A를 추가한다.
# 문자열을 뒤집고 뒤에 B를 추가한다.
while(True):
    if len(start) == len(target):
        if start == target:
            print(1)
            break
        else:
            print(0)
            break
    if target[-1] == 'A':
        target = target[:-1]
    elif target[-1] == 'B':
        target = target[:-1]
        target = target[::-1]