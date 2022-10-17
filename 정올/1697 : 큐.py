import sys
readl = sys.stdin.readline

n = int(readl())
buildings = [int(readl()) for _ in range(n)]

stack = []
show = [0] * n

for idx, b in enumerate(buildings):
    if len(stack) == 0:
        stack.append((idx, b))

    while stack and stack[-1][1] < b:
        i, _ = stack.pop()
        show[i] = idx + 1
    stack.append((idx, b))

print(*show, sep='\n')
