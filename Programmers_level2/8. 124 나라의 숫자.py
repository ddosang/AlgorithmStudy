import heapq

def solution(scoville, K):
    count = 0
    scoHeap = []
    
    for sco in scoville:
        heapq.heappush(scoHeap, sco)

#   하나 꺼냈을 때,
    first = heapq.heappop(scoHeap)
#   제일 작은게 K보다 작으면서, heap이 비어있지 않으면 들어간다.
    while first < K and len(scoHeap) > 0:
        second = heapq.heappop(scoHeap)
        heapq.heappush(scoHeap, first + second * 2)
        count += 1
        first = heapq.heappop(scoHeap)
    
#.  다 돌고 나왔는데 K보다 작은게 있으면 -1 return
#   여기를 scoHeap의 원소가 K보다 작으면으로 하면 안먹혔던 이유는
#   scoHeap이 이 시점에 비어있을 수 있기 때문.
    if first < K:
        return -1
    
    return count
