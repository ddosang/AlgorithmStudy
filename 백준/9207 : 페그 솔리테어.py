import sys
import math
from copy import deepcopy
readl = sys.stdin.readline

# 제일 많이 없어져봐야 핀 개수가 하나 남을 때까지.
def DFS(level):
    global pin_cnt, min_move

    flag = False

    # 그냥 전체에서 핀을 찾아서 들어감.
    for r in range(R):
        for c in range(C):
            if board[r][c] != 'o':
                continue

            # 상하좌우
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if not 0 <= r + 2 * dr < R:
                    continue
                if not 0 <= c + 2 * dc < C:
                    continue

                # 해당 방향에 핀이 있고 그 다음 칸이 빈 칸이면
                if board[r + dr][c + dc] == 'o' and board[r + 2 * dr][c + 2 * dc] == '.':
                    # 바뀌는게 있음.
                    flag = True
                    
                    # 뛰어넘어서 바뀌는거 표시.
                    board[r][c] = '.'
                    board[r + dr][c + dc] = '.'
                    board[r + 2 * dr][c + 2 * dc] = 'o'
                    # 거기서 다시 탐색.
                    DFS(level + 1)

                    # DFS 들어갔다 나온 후에 원상복귀
                    board[r][c] = 'o'
                    board[r + dr][c + dc] = 'o'
                    board[r + 2 * dr][c + 2 * dc] = '.'

                    
    # 핀이 더이상 움직일 수 없는 상태라면 갱신.
    if not flag:
        cnt = 0
        for i in range(R):
            cnt += board[i].count('o')

        if cnt < pin_cnt:
            pin_cnt = cnt
            min_move = level
        elif cnt == pin_cnt and min_move > level:
            min_move = level


T = int(readl())
for i in range(T):
    board = []
    str = readl().rstrip()
    while str != '':
        board.append([c for c in str])
        str = readl().rstrip()
    
    R = len(board)
    C = len(board[0])
    
    pin = 0
    pins = []
    
    # o 는 핀, # 은 구멍 없음.
    pin_cnt = math.inf
    min_move = math.inf
    DFS(0)
    print(pin_cnt, min_move)