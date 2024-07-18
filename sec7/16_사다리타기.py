# 혼자 푼 것
# 위에부터 타보고 맞는 것 나오면 프로그램 종료
from collections import deque

def DFS(x, y, start):
    if x == 9:
        # print(x, y, start)
        if board[x][y] == 2:
            print(start)
            exit(0)
        return

    for dx, dy in [(0, -1), (0, 1), (1, 0)]:
        newX, newY = x + dx, y + dy

        if 0 <= newX < N and 0 <= newY < N and board[newX][newY] > 0 and not visited[newX][newY]:
            visited[newX][newY] = 1
            DFS(newX, newY, start)
            break # 다른 DFS 처럼 (아래, 오른쪽) / (아래, 왼쪽) 이 같이 있을 떄 튜플 안에 있는걸 각각 탐색하면 안되고 무조건 오른쪽이나 왼쪽으로 뻗어야 해서 break
            # 사다리 특성 상 (아래, 오른쪽, 왼쪽) 으로 다 갈 수 있는 경우는 발생하지 않음.
    

N = 10
board = [list(map(int, input().split())) for _ in range(N)]
res = 0
for start in range(N):
    if board[0][start] == 1:
        visited = [[0] * N for _ in range(N)]
        DFS(0, start, start)


# 수업 코드
# 그냥 2부터 아래에서 위로 탐.. .천재야...
from collections import deque

def DFS(x, y):
    visitied[x][y] = 1
    if x == 0:
        print(y)
        return

    for dx, dy in [(0, -1), (0, 1), (-1, 0)]:
        newX, newY = x + dx, y + dy

        if 0 <= newX < N and 0 <= newY < N and board[newX][newY] > 0 and not visited[newX][newY]:
            visited[newX][newY] = 1
            DFS(newX, newY)
            break
    

N = 10
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
for i in range(10):
    if board[9][i] == 2:
        DFS(9, i)
        break
