import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
map = [[0,0,0] for _ in range(n)]
print(map)

for i in range(n):
    a,b,c = sys.stdin.readline().split()
