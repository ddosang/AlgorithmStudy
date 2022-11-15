import sys

readl = sys.stdin.readline

def checkBingo():
    cnt = 0
    # 가로
    for i in range(5):
        if bingo[i].count(0) == 5:
            cnt += 1

    # 세로
    for i in range(5):
        local_cnt = 0
        for j in range(5):
            if bingo[j][i] == 0:
                local_cnt += 1
        if local_cnt == 5:
            cnt += 1

    # 대각선 \
    local_cnt = 0
    for i in range(5):
        if bingo[i][i] == 0:
            local_cnt += 1
        if local_cnt == 5:
            cnt += 1

    # 대각선 /
    local_cnt = 0
    for i in range(5):
        if bingo[i][4-i] == 0:
            local_cnt += 1
        if local_cnt == 5:
            cnt += 1

    return cnt

bingo = [list(map(int, readl().split())) for _ in range(5)]
echo = []
for _ in range(5):
    echo += list(map(int,readl().split()))


# 가로 세로 대각선

for idx, e in enumerate(echo):
    breaked = False

    # 빙고판에서 숫자 찾고
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == e:
                breaked = True
                bingo[i][j] = 0
                break
        if breaked:
            break

    # 빙고가 되는지 체크
    # 한번에 4로 넘어가는 경우가 있어서 >= 3
    if checkBingo() >= 3:
        print(idx + 1)
        break
