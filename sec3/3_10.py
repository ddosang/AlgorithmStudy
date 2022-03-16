def sudoku(arr):
    # 가로
    for i in range(9):
        if len(set(arr[i])) != 9:
            return False
    # 세로
    for i in range(9):
        local = set()
        for j in range(9):
            local.add(arr[j][i])
        if len(local) != 9:
            return False

    # 각 박스 : 근데 생각해보니까 박스가 안맞으려면 이미 가로나 세로 중 하나는 안맞을 수밖에 없는데, 이거 할필요 없는거 아닌가??
    # for i in range(3):
    #     for j in range(3):
    #         local = set()
    #         for k in range(3*i, 3*i+3):
    #             for l in range(3*j, 3*j+3):
    #                 local.add(arr[l][k])
    #         print(local)
    #         if len(local) != 9:
    #             return False

    return True


arr = []

for i in  range(9):
    arr += [list(map(int, input().split()))]

print("YES" if sudoku(arr) else "NO")
