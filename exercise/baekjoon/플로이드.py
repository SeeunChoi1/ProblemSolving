import sys
sys.stdin = open("input.txt", "r")

city_num = int(sys.stdin.readline())
bus_num = int(sys.stdin.readline())
cost_map = [[100000000]*city_num for _ in range(city_num)]
for _ in range(bus_num):
    city_i, city_j, min_cost = map(int, sys.stdin.readline().split())
    cost_map[city_i-1][city_j-1] = min(cost_map[city_i-1][city_j-1],min_cost)

#플로이드–와샬
for c in range(city_num):
    cost_map[c][c] = 0 
    for i in range(city_num):
        for j in range(city_num):
            cost_map[i][j] = min(cost_map[i][j], cost_map[i][c]+cost_map[c][j])    

#i에서 j로 가는 최소비용
for row in cost_map:
    for elem in row:
        if elem == 100000000:
            print(0, end=" ")
        else:
            print(elem, end=" ")
            
    print()
