'''
최대힙
'''

import heapq

hq = []
num = 0

while num != -1:
    num = int(input())

    if num == 0:
        print(-heapq.heappop(hq))
    else:
        heapq.heappush(hq, -num)