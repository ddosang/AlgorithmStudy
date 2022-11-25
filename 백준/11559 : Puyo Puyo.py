import sys
from collections import deque
readl = sys.stdin.readline

def BFS(i, j, ch):
    global pang_cnt

    chk = [[0] * 6 for _ in range(12)]

    q = deque([(i, j)])
    chk[i][j] = 1
    cnt = 1
    pang = [(i, j)]
    

    while q:
        x, y = q.popleft()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy

            if not 0 <= nx < r:
                continue
            if not 0 <= ny < c:
                continue
            
            # 같은 글자를 찾아야하니까 다른 글자 거름
            if puyo[nx][ny] != ch:
                continue

            # 방문 한거 거름
            if chk[nx][ny] == 1:
                continue

            chk[nx][ny] = 1
            q.append((nx, ny))
            pang.append((nx, ny))
            cnt += 1

    
    if cnt >= 4:
        for i, j in pang:
            puyo[i][j] = '.'
        dict[ch] -= cnt
        pang_cnt += 1

    
    return cnt
    

def down():
    for i in range(c):
        arr = []
        for j in range(r):
            arr.append(puyo[j][i])


        # 처음으로 0이 아닌 것의 인덱스를 저장.
        not_dot_idx = -1
        for idx, ch in enumerate(arr):
            if ch != '.':
                not_dot_idx = idx
                break
        
        # 처음으로 0이 아닌거 뒷쪽의 . 을 모두 제거하고,
        # 그만큼 앞에 . 을 더해준다.
        removed_arr = arr[not_dot_idx:]
        removed_cnt = 0
        while '.' in removed_arr:
            removed_arr.remove('.')
            removed_cnt += 1
        
        arr = arr[:not_dot_idx] + ['.'] * removed_cnt + removed_arr

        for j in range(r):
            puyo[j][i] = arr[j]


r, c = 12, 6
puyo = [[c for c in readl().rstrip()] for _ in range(r)]

pang_cnt = 0
dict = {'R':0, 'G':0, 'B':0, 'P':0, 'Y':0}

for i in range(r):
    for j in range(c):
        if puyo[i][j] != '.':
            dict[puyo[i][j]] += 1

before_pang_cnt = -1
while before_pang_cnt != pang_cnt:
    # 1. 한번 전체를 돌고
    before_pang_cnt = pang_cnt
    for i in range(r - 1, -1, -1):
        for j in range(c):
            # 같은 종류의 글자가 4개 이상 있어야 터뜨릴 수 있고,
            if puyo[i][j] != '.' and dict[puyo[i][j]] >= 4:
                BFS(i, j, puyo[i][j])

    # 한번에 여러개가 터져도 팡은 하나만 증가.
    pang_cnt = before_pang_cnt + 1 if pang_cnt != before_pang_cnt else before_pang_cnt
    # 2. down
    down()

print(pang_cnt)