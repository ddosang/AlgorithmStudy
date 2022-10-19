import sys
import heapq

n = int(sys.stdin.readline())
candies = list(map(int, sys.stdin.readline().split()))

sum = 0

candyheap = []
for i in range(n):
    heapq.heappush(candyheap, candies[i])

for _ in range(n - 1):
    n1 = heapq.heappop(candyheap)
    n2 = heapq.heappop(candyheap)

    sum += (n1 + n2)
    heapq.heappush(candyheap, n1 + n2)

print(sum)
