import sys
from collections import deque
readl = sys.stdin.readline

# a -> b
def Move(ca, cb, a, b):
    nb = (b + a) if a <= (cb - b) else cb
    na = a - (nb - b)

    return (na, nb)


def BFS():
    visited = set((0, 0))
    q = deque()
    q.append((0, 0, 0))

    # 이거 처음에 안걸러서 틀린거였음!!!
    if ea == 0 and eb == 0:
        return 0
    

    # Fill / Empty / Move
    # 1 은 Fill -1 은 Empty 
    # -2 2 는 주고 받기.
    
    while q:
        a, b, cnt = q.popleft()

        x, y = Move(cb, ca, b, a)
        move = [(ca, b), (a, cb), (0, b), (a, 0), Move(ca, cb, a, b), (y, x)]

        for na, nb in move:
            if (na, nb) == (ea, eb):
                return cnt + 1

            if (na, nb) in visited:
                continue

            visited.add((na, nb))
            q.append((na, nb, cnt + 1))

    return -1


ca, cb, ea, eb = map(int, readl().split())

print(BFS())