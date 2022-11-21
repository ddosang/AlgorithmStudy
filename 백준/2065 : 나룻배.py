import sys
from collections import deque

readl = sys.stdin.readline

m, t, n = map(int, readl().split())
order = [readl().split() for _ in range(n)]
order = [[i, int(o[0]), o[1]] for i, o in enumerate(order)]


stop = [deque(), deque()] # leftq, rightq
ship = deque()
ship_side = 0 # left 에서 시작.
i = 0
current = 0
res = [0] * n
cnt = 0 # 내린 사람 카운트

while cnt < n:

    # 현재 시간보다 작은 것을 대기열에 넣음.
    while i < n and current >= order[i][1]:
        side = (order[i][2] == "right")
        stop[side].append(order[i][0])
        i += 1

    # 현재 배가 있는 곳의 대기열을 배에 태움.
    while len(ship) < m and stop[ship_side]:
        ship.append(stop[ship_side].popleft())

    if len(ship) == 0 and len(stop[0]) == 0 and len(stop[1]) == 0 and i < n:
        # 만약 해당 시간에 손님이 계속 없으면 다음 손님이 올때까지 기다림
        current = order[i][1]

        # 동시에 여러게 올 수도 있으니까.
        # 현재 시간과 같은 것을 대기열에 넣음.
        while i < n and current >= order[i][1]:
            side = (order[i][2] == "right")
            stop[side].append(order[i][0])
            i += 1

        # 현재 배가 있는 곳의 대기열을 배에 태움.
        while len(ship) < m and stop[ship_side]:
            ship.append(stop[ship_side].popleft())

    ship_side = 0 if ship_side else 1
    current += t

    while ship:
        res[ship.popleft()] = current
        cnt += 1

print(*res, sep='\n')
