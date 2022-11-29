import sys
readl = sys.stdin.readline

def checkSudoku():
    for i in range(3):
        for j in range(9):
            for k in range(1, 10):
                if ch[i][j][k] != 1:
                    return False
    return True

def printSudoku():
    for i in range(9):
        print(*sudoku[i])


def DFS(level, idx):
    if level == zero_cnt:
        if checkSudoku():
            printSudoku()
            exit(0)
        return

    for i in range(1, 10):
        # 비어있는 칸에 1~9 중 아무거나 넣을건데,
        ni, nj = zeros[idx]
        # 해당 칸의 범위에 있는 가로 세로 네모 중에 해당 숫자가 들어간게 있으면 검사해볼 필요가 없음.
        if ch[0][ni][i] != 0 or ch[1][nj][i] != 0 or ch[2][3 * (ni // 3) + nj // 3][i] != 0:
            continue

        
        ch[0][ni][i] = 1
        ch[1][nj][i] = 1
        ch[2][3 * (ni // 3) + nj // 3][i] = 1
        sudoku[ni][nj] = i

        DFS(level + 1, idx + 1)

        ch[0][ni][i] = 0
        ch[1][nj][i] = 0
        ch[2][3 * (ni // 3) + nj // 3][i] = 0
        sudoku[ni][nj] = 0




sudoku = [list(map(int, readl().split())) for _ in range(9)]


# 첫번째 인덱스 3개 : 가로 (9개), 세로 (9개), 3*3 정사각형 (9개)
# 두번째 인덱스 9개 : 가로 i, 세로 j, 정사각형 -> 3 * i // 3 + j // 3
# 세번째 인덱스 10개 : 0은 빼고, 1 ~ 9 각 몇개 사용했는지.
# 0 3 6 
# 1 4 7
# 2 5 8
# 1 ~ 9 가 각 하나씩만 있으면 된다.
ch = [[[0] * 10 for _ in range (9)] for _ in range(3)]
# cnts = [[0] * 9 for _ in range(3)]
# sums = [[0] * 9 for _ in range(3)]

zero_cnt = 0
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_cnt += 1
            zeros.append((i, j))
        else:
            # 어떤 범위 (가로 / 세로 / 대각선) 에서 어떤 숫자를 사용했는지 체크.
            ch[0][i][sudoku[i][j]] = 1
            ch[1][j][sudoku[i][j]] = 1
            ch[2][3 * (i // 3) + j // 3][sudoku[i][j]] = 1

DFS(0, 0)