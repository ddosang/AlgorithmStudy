import sys

readl = sys.stdin.readline

def leftToRight(row, start, end):
    global num, sol
    for i in range(start, end + 1):
        seat[row][i] = num
        if num == k:
            sol = (row + 1, i + 1)
        num += 1

def upToDown(col, start, end):
    global num, sol
    for i in range(start, end + 1):
        seat[i][col] = num
        if num == k:
            sol = (i + 1, col + 1)
        num += 1

def rightToLeft(row, end, start):
    global num, sol
    for i in range(end, start - 1, - 1):
        seat[row][i] = num
        if num == k:
            sol = (row + 1, i + 1)
        num += 1


def downToUp(col, end, start):
    global num
    for i in range(end, start - 1, - 1):
        seat[i][col] = num
        if num == k:
            sol = (i + 1, col + 1)
        num += 1


h, w = map(int, readl().split())
k = int(readl())

seat = [[0] * w for _ in range(h)]
num = 1

startCol = 0
endCol = w - 1
startRow = 1
endRow = h - 1

sol = (0, 0)


for i in range(min(w, h) // 2 + 1):
    leftToRight(i, startCol, endCol)
    if num == w * h + 1:
        break
        
    upToDown((w - 1) - i, startRow, endRow)
    if num == w * h + 1:
        break
        
    rightToLeft((h - 1) - i, endCol - 1, startCol)
    if num == w * h + 1:
        break
        
    downToUp(i, endRow - 1, startRow)
    if num == w * h + 1:
        break


    startCol += 1
    endCol -= 1
    startRow += 1
    endRow -= 1

for i in range(h):
    for j in range(w):
        if seat[i][j] == k:
            sol = (i + 1, j + 1)

# for i in range(h):
#     print(seat[i])

if sol == (0, 0):
    print(0)
else:
    print(*sol)


