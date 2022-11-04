import sys

readl = sys.stdin.readline

def DFS(play):
    global ans
    if play == 15:
        ans = 1
        for r in results:
            if r.count(0) != 3:
                ans = 0
                break
        return

    home, away = 대진표[play]

    # 가능한 경우 3가지
    # 승 패 / 무 무 / 패 승
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if results[home][x] > 0 and results[away][y] > 0:
            results[home][x] -= 1
            results[away][y] -= 1
            DFS(play + 1)
            results[home][x] += 1
            results[away][y] += 1




# 15번의 경기를 진행.
대진표 = []
for i in range(6):
    for j in range(i + 1, 6):
        대진표.append((i, j))


for i in range(4):
    inp = list(map(int, readl().split()))
    results = [inp[3 * i : 3 * (i + 1)] for i in range(6)]

    ans = 0
    DFS(0)
    print(ans, end=' ')
