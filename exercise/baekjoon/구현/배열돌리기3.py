import sys

sys.stdin = open("input.txt", "r")


row_num, col_num, exe_num = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(row_num)]
# print(*array, sep="\n")
exe_list = list(map(int, input().split()))
# print(exe_list)


# 1번 연산 - 상하반전
def exe1(row_num, col_num, array):
    new_array = [[0] * col_num for _ in range(row_num)]
    # print(*new_array, sep="\n")
    # (i,j) -> (n-1-i,j)
    for i in range(row_num):
        for j in range(col_num):
            new_array[i][j] = array[row_num - 1 - i][j]

    # for num in range(row_num * col_num):
    #     i, j = num / row_num, num % row_num
    #     new_array[i][j] = array[row_num - 1 - i, j]
    return new_array


# 2번 연산 - 좌우반전
def exe2(row_num, col_num, array):
    new_array = [[0] * col_num for _ in range(row_num)]
    # (i,j) -> (i, n-1-j)
    for i in range(row_num):
        for j in range(col_num):
            new_array[i][j] = array[i][col_num - 1 - j]

    return new_array


# 3번 연산 - 오른쪽 90도 회전
def exe3(row_num, col_num, array):
    new_array = [[0] * row_num for _ in range(col_num)]
    # print(*new_array, sep="\n")
    # row_num <-> col_num
    for i in range(row_num):
        for j in range(col_num):
            new_array[j][row_num - 1 - i] = array[i][j]

    return new_array


# 4번 연산 - 왼쪽 90도 회전
def exe4(row_num, col_num, array):
    new_array = [[0] * row_num for _ in range(col_num)]
    # row_num <-> col_num
    for i in range(row_num):
        for j in range(col_num):
            new_array[col_num - 1 - j][i] = array[i][j]

    return new_array


# 5번 연산 - 부분배열 1->2 / 2->3 / 3->4 / 4->1
def exe5(row_num, col_num, array):
    new_array = [[0] * col_num for _ in range(row_num)]
    row_part = row_num // 2
    col_part = col_num // 2

    for i in range(row_num):
        for j in range(col_num):
            if i < row_part and j < col_part:
                new_array[i][j + col_part] = array[i][j]
            elif i < row_part and j >= col_part:
                new_array[i + row_part][j] = array[i][j]
            elif i >= row_part and j >= col_part:
                new_array[i][j - col_part] = array[i][j]
            elif i >= row_part and j < col_part:
                new_array[i - row_part][j] = array[i][j]

    return new_array


# 6번 연산 - 부분배열 1->4 / 4->3 / 3->2 / 2->1
def exe6(row_num, col_num, array):
    new_array = [[0] * col_num for _ in range(row_num)]
    row_part = row_num // 2
    col_part = col_num // 2

    for i in range(row_num):
        for j in range(col_num):
            if i < row_part and j < col_part:
                new_array[i + row_part][j] = array[i][j]
            elif i < row_part and j >= col_part:
                new_array[i][j - col_part] = array[i][j]
            elif i >= row_part and j >= col_part:
                new_array[i - row_part][j] = array[i][j]
            elif i >= row_part and j < col_part:
                new_array[i][j + col_part] = array[i][j]

    return new_array


for exe in exe_list:
    if exe == 1:
        new_array = exe1(row_num, col_num, array)
    elif exe == 2:
        new_array = exe2(row_num, col_num, array)
    elif exe == 3:
        new_array = exe3(row_num, col_num, array)
        row_num, col_num = col_num, row_num
    elif exe == 4:
        new_array = exe4(row_num, col_num, array)
        row_num, col_num = col_num, row_num
    elif exe == 5:
        new_array = exe5(row_num, col_num, array)
    elif exe == 6:
        new_array = exe6(row_num, col_num, array)
    array = new_array

# print(*array, sep="\n")
for a in array:
    print(*a, sep=" ")
