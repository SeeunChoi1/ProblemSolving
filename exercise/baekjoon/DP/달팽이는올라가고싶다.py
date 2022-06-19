import sys, math
sys.stdin = open("input.txt", "r")

a, b, v = map(int, input().split())
print(a, b, v)

ans = 1
while(True):
    v -= a
    if(v <= 0):
        break
    else:
        v += b
        ans += 1

ans = math.ceil((v-b)/(a-b))
print(ans)