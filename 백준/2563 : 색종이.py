import sys

readl = sys.stdin.readline

n = int(readl())
색종이 = [list(map(int, readl().split())) for _ in range(n)]
도화지 = [[0] * 100 for _ in range(100)]

for startX, startY in 색종이:
    endX = startX + 10
    endY = startY + 10

    for i in range(startX, endX):
        for j in range(startY, endY):
            도화지[i][j] = 1

sum = 0
for i in range(100):
    sum += 도화지[i].count(1)
print(sum)
