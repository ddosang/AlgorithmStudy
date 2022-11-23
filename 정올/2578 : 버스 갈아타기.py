import sys
from collections import deque
readl = sys.stdin.readline

import sys
from collections import deque
readl = sys.stdin.readline

def BFS():
    q = deque([(startr, startc)])
    bmap[startr][startc] = 0

    while q:
        x, y = q.popleft()
        # print(x, y)
            
        # 모든 버스 중에 탈 수 있는 버스를 찾아야할듯...
        for num, start, end in bus:
            stops = []
            temp = sorted([start, end])
            start, end = temp
            
            # 해당 버스의 구간에 내가 들어감.
            # 버스 구간이 가로임.
            if start[0] == end[0]:
                # for i in range(start[1], end[1] + 1):
                #     if (start[0], i) == (x, y):
                #         # 이거 탈 수 있음.
                #         stops = [(start[0], i) for i in range(start[1], end[1] + 1)]
                #         break
                if start[0] == x and start[1] <= y <= end[1]:
                    stops = [(start[0], i) for i in range(start[1], end[1] + 1)]
                else:
                    continue

            # 해당 버스의 구간에 내가 들어감.
            # 버스 구간이 세로임
            elif start[1] == end[1]:
                if start[0] <= x <= end[0] and start[1] == y:
                    stops = [(i, start[1]) for i in range(start[0], end[0] + 1)]
                else:
                    continue

            # print(x, y, stops)
            
            # 해당 버스를 타고 모든 지점에서 내려봄.
            for er, ec in stops:

                # 탄 지점에선 안내려도 됨.
                if (er, ec) == (x, y):
                    continue

                # 환승을 더 많이하면 거름.
                if bmap[x][y] + 1 >= bmap[er][ec]:
                    continue
                
                # 목표 지점이면 return
                if (er, ec) == (endr, endc):
                    return bmap[x][y] + 1

                bmap[er][ec] = bmap[x][y] + 1
                q.append((er, ec))

    return -1



c, r = map(int, readl().split())
k = int(readl())
bus = [list(map(int, readl().split())) for _ in range(k)]
bus = sorted([[num, (sr, sc), (er, ec)] for num, sc, sr, ec, er in bus])
startc, startr, endc, endr = map(int, readl().split())


bmap = [[0] + [10000000] * c + [0] if 1 <= i <= r else [0] * (c + 2) for i in range(r + 2)]


print(BFS())

# for i in range(r + 2):
#     print(bmap[i])