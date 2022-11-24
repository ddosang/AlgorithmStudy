import sys
from collections import deque
import math
readl = sys.stdin.readline


def alphabetToIndex(c):
    if ord(c) >= ord('a'):
        return ord(c) - ord('a') + 26

    return ord(c) - ord('A')

def indexToAlphabet(num):
    if num > 25:
        return chr(num - 26 + ord('a'))
    return chr(num + ord('A'))

def BFS(start):
    q = deque([(start, 0)]) # 시간

    while q:
        x, dist = q.popleft()

        # 다음지점과 거리.
        for nx, d in dict[x]:

            ndist = dist + d

            if visited[nx] <= ndist:
                continue

            visited[nx] = ndist
            q.append((nx, ndist))

    return visited[alphabetToIndex('Z')]
            



P = int(readl())
houses = [readl().rstrip().split() for _ in range(P)]

houses = [[alphabetToIndex(start), alphabetToIndex(end), int(dist)] for start, end, dist in houses] + [[alphabetToIndex(end), alphabetToIndex(start), int(dist)] for start, end, dist in houses]

houses.sort()

dict = {x[0] : [] for x in houses}


for start, end, dist in houses:
    dict[start].append((end, dist))

# 소가 없는 목장은 소문자
# 헛간은 Z
    
visited = [math.inf] * 52

# 0 ~ 24 사이에 있는걸 출발점으로 해서 시작.
# 목적지 Z 가 25
min_b = math.inf
min_start = 0
for start, _, _ in houses:
    if start < alphabetToIndex('Z'):
        b = BFS(start)
        if min_b > b:
            min_b = b
            min_start = start
        # print(start, b)
            
print(indexToAlphabet(min_start), min_b)