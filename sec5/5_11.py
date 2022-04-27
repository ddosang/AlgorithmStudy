import heapq

heap = []

n = 0
while n != -1:
    n = int(input())
    if n == 0:
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -n)
