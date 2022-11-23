import sys
from collections import deque
readl = sys.stdin.readline

def BFS(redx, redy, bluex, bluey):
    global R, C
    ch = [[[[0] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]
    # ch = [[0] * C for _ in range(R)]
    q = deque([(redx, redy, bluex, bluey, 0)])
    ch[redx][redy][bluex][bluey] = 1

    while q:
        redx, redy, bluex, bluey, cnt = q.popleft()

        if (redx, redy) == hole:
            return cnt

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nredx, nredy, nbluex, nbluey, ncnt = redx + dx, redy + dy, bluex + dx, bluey + dy, cnt + 1

            if ncnt > 10:
                return -1
            
            # red 가 움직이기에 앞서서 blue 를 움직이고 체크해본다.
            # blue 움직이는 곳이 벽이면 blue 는 그 자리에 그대로...
            if game[nbluex][nbluey] == '#':
                nbluex, nbluey = bluex, bluey
                
            # blue 가 움직였는데 hole 이면 안됨.
            if (nbluex, nbluey) == hole:
                continue
                
            # red 움직였는데 벽이면 그 자리에 그대로...
            if game[nredx][nredy] == '#':
                nredx, nredy = redx, redy

            # 둘 다 못 움직였다면 그 방향으로 움직이는건 낭비.
            if (nredx, nredy) == (redx, redy) and (nbluex, nbluey) == (bluex, bluey):
                continue
                
            # red 랑 blue 랑 만나면 움직일수가 없음.
            if (nredx, nredy) == (nbluex, nbluey):
                continue

            # red 가 이미 갔던 곳이면 낭비임 움직일 필요 X
            if ch[nredx][nredy][nbluex][nbluey] == 1:
                continue

            # 그렇게 움직인게 구멍에 들어가면 cnt
            if (nredx, nredy) == hole:
                return ncnt
            
            q.append((nredx, nredy, nbluex, nbluey, ncnt))
            ch[nredx][nredy][nbluex][nbluey] = 1

    return -1


# BFS 로 R 이 H 를 찾아가는 횟수를 찾으면 되는데,
# 거기서 B 가 H 에 들어가는 경우가 생기면 안됨.


T = int(readl())
for _ in range(T):
    R, C = map(int, readl().split())
    game = [[c for c in readl().rstrip()] for _ in range(R)]

    red, blue, hole = -1, -1, -1
    for i in range(R):
        if 'R' in game[i]:
            red = (i, game[i].index('R'))
        if 'B' in game[i]:
            blue = (i, game[i].index('B')) 
        if 'H' in game[i]:
            hole = (i, game[i].index('H')) 

        if red != -1 and blue != -1 and hole != -1:
            break
    
    print(BFS(red[0], red[1], blue[0], blue[1]))
    

