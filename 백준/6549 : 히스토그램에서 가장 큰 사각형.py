import sys
from collections import deque

readl = sys.stdin.readline


line = readl()
while line != '0':
    # 입력 받기
    n = 0
    heights = []
    for i, num in enumerate(map(int, line.split())):
        if i == 0:
            n = num
            continue
        heights.append(num)
    heights.append(-1) # 마지막에 스택에 남은 것 전부 프린트하기 위한 while 문 쓰는대신 -1 로 채운다.

    # 스택을 이용해서 풀기.
    stack = []
    max_area = 0

    for i in range(n + 1):
        w = i
        h = heights[i]
        # 새로 들어가는 것의 높이가 크면 해당 높이를 사용할수도 있으니 STACK 에 유지
        # 작으면, 커다란 부분에 대해서는 의미가 없으므로 pop
        while stack and heights[stack[-1]] > heights[i]:
            p = stack.pop()
            h = heights[p]
            # 지금거보다 작거나 같은게 남아있다면, 거기까지만 width 체크
            if stack:
                w = (i - 1 - stack[-1])
            # 스택이 비었다면, 현재 높이가 최소이므로 현재 높이 * i 하면 됨.
            else:
                w = i

            max_area = max(max_area, w * h)

        stack.append(i)
        # print(stack)

    print(max_area)

    line = readl().strip()
