import sys
readl = sys.stdin.readline
    

# 지금 보드에서 점을 하나로 합칠 수 있는지 체크.
def checkTotal():
    for i, j in xarr:
        BFS(i, j)


# i, j 를 바꿨을 때, 주변 점이 3개가 되는지.
def checkThree(i, j):
    # 위아래로 가능한지?
    if 2 <= i < N - 2:
        # 위 두개
        if fur[i - 2][j] == 'X' and fur[i - 1][j] == 'X':
            return 1

        # 아래 두개
        if fur[i + 1][j] == 'X' and fur[i + 2][j] == 'X':
            return 2

    if 1 <= i < N - 1:
        # 위 하나 아래 하나
        if fur[i - 1][j] == 'X' and fur[i + 1][j] == 'X':
            return 3

    if 2 <= j < M - 2:
        if fur[i][j - 2] == 'X' and fur[i][j - 1] == 'X':
            return 4

        if fur[i][j + 1] == 'X' and fur[i][j + 2] == 'X':
            return 5
    
    if 1 <= j < M - 1:
        if fur[i][j - 1] == 'X' and fur[i][j + 1] == 'X':
            return 6
    
    return 0



def DFS(level):

    for i in range(N):
        for j in range(M):
            if fur[i][j] == '.':
                
                # . 을 X 로 만들었을 때 X 가 될 수 있다면 만들어보기.
                if not checkThree(i, j): 
                    continue

                DFS(level + 1)

    

N, M = map(int, readl().split())
fur = [list(readl().rstrip()) for _ in range(N)]

xarr = []
xcnt = 0

for i in range(N):
    for j in range(M):
        if fur[i][j] == 'X':
            xarr.append((i, j))
            xcnt += 1
