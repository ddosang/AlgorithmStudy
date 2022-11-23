import sys

readl = sys.stdin.readline


def check(d):
    # print('d=', d)
    # 첫번째 구간에서 시작.
    pos = grasses[0][0]
    cow = 1

    for i in range(m):
        start, end = grasses[i]
		
        # 만약에 다음 구간이 d 거리 사이에 있다면 다음 구간부터 체크.
        if pos + d > end:
            continue

        # 다음 구간 시작이 d 이상 떨어져있으면 다음 구간 시작으로 설정.
        if (start - pos) >= d:
            pos = start
            # cow += 1
            # print(pos, cow)

        # 다음 구간 시작이 d 이상 떨어져있지 않으면서
        # 다음 구간이 엄청 작지 않으면 d 더해서 넘어감.
        elif pos + d <= end:
            pos += d
        

        # 예를 들어서
        cow += (end - pos) // d + 1
        pos += ((end - pos) // d) * d
        # print(pos, cow)

    return cow


def check2(d):
    # 첫번째 소 배치
    idx = 0
    last = grasses[0][0]

    # 나머지 n - 1 마리의 소에 대해서
    for _ in range(n - 1):
        # 잔디 구간이 더 작으면 다음 잔디구간으로 넘어감.
        while idx < m and grasses[idx][1] < last + d:
            idx += 1
        
        # 위에서 나왔는데 잔디 구간이 남아있지 않아서 나온거면, 
        # 놓을 수 있는 cow 가 더 적은거니까 더 이상 검사할 필요 X
        if idx == m:
            return False
        
        # + d 한게 다음 잔디 구간 안에 있으면 + d 아니면 다음 잔디 구간 첫번째로 바꿈.
        last = grasses[idx][0] if grasses[idx][0] > last + d else last + d

    return True



n, m = map(int, readl().split())
grasses = [list(map(int, readl().split())) for _ in range(m)]


    # 가장 가까운 두 소 사이의 거리가 최대가 되도록.

left = 0
right = grasses[-1][1] - grasses[0][0]

sol = -1

while left <= right:
    mid = (left + right) // 2

    # 소가 많음 -> 거리를 늘려야 함.
    if check(mid) >= n:
        left = mid + 1
        sol = mid
    else:
        right = mid - 1


print(sol)