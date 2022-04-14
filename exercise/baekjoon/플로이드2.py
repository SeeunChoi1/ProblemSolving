import sys
sys.stdin = open("input.txt", "r")

city_num = int(sys.stdin.readline())
bus_num = int(sys.stdin.readline())
cost_map = [[100000]*city_num for _ in range(city_num)]
trace = [[[]for _ in range(city_num)] for _ in range(city_num)]

for _ in range(bus_num):
    city_i, city_j, min_cost = map(int, sys.stdin.readline().split())
    if cost_map[city_i-1][city_j-1] > min_cost:
        cost_map[city_i-1][city_j-1] = min_cost
        trace[city_i-1][city_j-1].append(city_i) #경로추가
        trace[city_i-1][city_j-1].append(city_j) #경로추가

#플로이드–와샬
for c in range(city_num):
    cost_map[c][c] = 0 
    trace[c][c] = []
    for i in range(city_num):
        for j in range(city_num):
            if cost_map[i][j] > cost_map[i][c]+cost_map[c][j]:
                cost_map[i][j] = cost_map[i][c]+cost_map[c][j]  
                trace[i][j] = trace[i][c] + trace[c][j][1:] #경로추가    

#i에서 j로 가는 최소비용
for row in cost_map:
    for elem in row:
        if elem<100000:
            print(elem, end=" ")
        else:
            print(0, end=" ")
    print()

#i에서 j로 가는 최소 비용에 포함되어 있는 도시의 개수 k
for row in trace:
    for elem in row:
        print(len(elem),end=" ")
        for e in elem:
            print(e,end=" ")
        print()