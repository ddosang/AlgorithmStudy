import sys
readl = sys.stdin.readline

def BFS():
    # q = deque([(1, 1)])

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # dir + 1 하면 오른쪽으로 틀고 -1 하면 왼쪽으로 틀고.
    dir = 0 # 초기엔 오른쪽.


    head = (1, 1)
    body = [(1, 1)]
    board[1][1] = 2 # 자기 자신은 2
    time = 0
    
    for t, d in move:

        # 오른쪽으로 X 만큼
        for i in range(t):
            x, y = head
            nx, ny = x + direction[dir][0], y + direction[dir][1]
            ntime = time + 1

            # 벽이거나 자기자신이면 return
            if board[nx][ny] == 9 or board[nx][ny] == 2:
                return ntime

            # head, body, time 갱신.
            head = (nx, ny)
            body.append(head)
            time = ntime

            # 사과가 아니면 몸 길이를 줄임.
            if board[nx][ny] != 1:
                tail = body.pop(0)
                board[tail[0]][tail[1]] = 0
            
            board[nx][ny] = 2

            # for i in range(N + 2):
            #     print(board[i])
            # print()

        dir = (dir + 1) % 4 if d == "D" else (dir - 1) % 4



    return -1

N = int(readl())
K = int(readl())

# 벽은 9
board = [[9] + [0] * (N) + [9] if 1 <= i <= N else [9] * (N + 2) for i in range(N + 2)]

# 사과는 1
for _ in range(K):
    r, c = map(int, readl().split())
    board[r][c] = 1

# move
L = int(readl())
moves = [readl().split() for _ in range(L)]

# 처음에 움직인 시점으로부터 몇 초 움직이고 트는건 줄 알았는데,
# 시작 시간으로부터 17초 후에 튼다 이런 식이어서
# 앞에 방향 트는 시간을 빼서 가지고 있어야 내가 원하는 대로 나오는 거였음.
move = []
move.append([int(moves[0][0]), moves[0][1]])

for i in range(1, L):
    move.append([int(moves[i][0]) - int(moves[i - 1][0]), moves[i][1]])

# 만약에 마지막인데 아직 부딪힌 적이 없으면 해당 방향으로 쭉 가서 부딪힐 것임.
move.append([N, 'X'])

print(BFS())