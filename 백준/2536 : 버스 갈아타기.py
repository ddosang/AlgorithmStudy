import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    M, N = map(int,readl().split())
    K = int(readl())
    list_bus = [list(map(int,readl().split())) for _ in range(K)]
    sx, sy, dx, dy = map(int,readl().split())
    return M, N, K, list_bus, sx, sy, dx, dy

# 작은거 ~ 큰거로 bus 리스트 가공.
def Arange_Bus(list_bus):
    list_bus = [(id,min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2)) for id,x1,y1,x2,y2 in list_bus]
    return list_bus


# 목적지를 포함하는 버스이면 s_dest 에 True 저장.
    # 근데 이 버스가 시작접에서 바로 탈 수 있는 버스라면?
        # return True, s_rem, s_dest, q
    # 아니라면..
        # s_dest : destination 을 지나가는 버스인가? 를 저장.
        # s_rem : 모든 버스 목록 - 시작점에서 탈 수 있는 버스의 목록.
        # 시작점에서 탈 수 있는 버스는 큐에 넣는다.
def Make_Init():
    q = deque()
    s_rem = set(range(K))
    s_dest = [False]*K
    for i, bus in enumerate(list_bus):
        flag = 0
        _, x1, x2, y1, y2 = bus
        if x1<=dx<=x2 and y1<=dy<=y2: 
            s_dest[i]=True
        if not x1<=sx<=x2: continue
        if not y1<=sy<=y2: continue
        if s_dest[i]: return True, s_rem, s_dest, q 
        s_rem.remove(i)
        q.append((i, 1))
    return False, s_rem, s_dest, q


# 지금 타고 있는거랑 맞물리는 정류장이 있는지?.
def Check(n,nn):
    return ((list_bus[n][1]<=list_bus[nn][1]<=list_bus[n][2]) 
            or (list_bus[nn][1]<=list_bus[n][1]<=list_bus[nn][2])) and \
            ((list_bus[n][3]<=list_bus[nn][3]<=list_bus[n][4]) 
            or (list_bus[nn][3]<=list_bus[n][3]<=list_bus[nn][4]))

def Check2(first, second):
    _, bus1_sx, bus1_ex, bus1_sy, bus1_ey = list_bus[first]
    _, bus2_sx, bus2_ex, bus2_sy, bus2_ey = list_bus[second]

    return ((
        # x 가 갈아탈 수 있는 영역에 있나요?
        ((bus1_sx <= bus2_sx <= bus1_ex) or
        (bus2_sx <= bus1_sx <= bus2_ex)) and \
        # y 가 갈아탈 수 있는 영역에 있나요?
        ((bus1_sy <= bus2_sy <= bus1_ey) or
        (bus2_sy <= bus1_sy <= bus2_ey))
    ))


def BFS():
    arrived, s_rem, s_dest, q = Make_Init()
    if arrived: return 1 # 처음에 목적지로 가는걸 탈 수 있으면 바로 1

    while q:
        n, cnt_bus = q.popleft()
        s_chk = list()
        ncnt_bus = cnt_bus + 1

        # 큐에 안들어간 버스들을 탈건데,
        for nn in s_rem:
            # 갈아탈 수 있는 버스가 아니면 넘기고,
            if not Check(n, nn): continue
            # 해당 버스가 목적지로 감 -> 이거 타면 됨!
            if s_dest[nn]: return ncnt_bus

            s_chk.append(nn)
            q.append((nn, ncnt_bus))

        # 지금 있는 지점에서 탈 수 있는 버스는 큐에 들어갔으니
        # 체크할 수 있는 목록에서 제거.
        for i in s_chk:
            s_rem.remove(i)

    return -1


M, N, K, list_bus, sx, sy, dx, dy = Input_Data()
list_bus = Arange_Bus(list_bus)
sol = BFS()
print(sol)