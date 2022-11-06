import sys
from collections import deque

readl = sys.stdin.readline

n, m = map(int, readl().split())
주차장자리 = [int(readl()) for _ in range(n)]
차의무게 = [int(readl()) for _ in range(m)]
출입순서 = [int(readl()) for _ in range(2 * m)]

ch = [0] * n

q = deque()
total = 0
빈자리 = -1

for 차번호 in 출입순서:
    if 차번호 > 0:
        # 자리가 있으면 자리에 넣고
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 차번호
                break
        # 자리가 없으면 큐에 넣고
        else:
            빈자리 = -1
            q.append(차번호)

    else:
        차번호 = -차번호
        for i in range(n):
            if ch[i] == 차번호:
                ch[i] = 0
                빈자리 = i

                total += 주차장자리[i] * 차의무게[차번호 - 1]

                break
        if q:
            for i in range(n):
                if ch[i] == 0:
                    ch[i] = q.popleft()
                    break


print(total)
