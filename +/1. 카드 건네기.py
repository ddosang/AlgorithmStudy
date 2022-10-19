from collections import deque

n = int(input())

cards = deque([i + 1 for i in range(n)])

for _ in range(n):
    for _ in range(cards[-1] // 2):
        cards.append(cards.popleft())
    print(cards.popleft(), end=' ')
