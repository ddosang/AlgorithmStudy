n, c = map(int, input().split())

# c마리의 말을 n개의 마굿간에 배치할 때 가장 가까운 두말의 거리가 되는 최대값.
horses = []
for i in range(n):
    horses.append(int(input()))

horses.sort()

# 최소 시간을 가정하고, 그 시간대로 했을 때 말이 몇 마리 들어가는지?
def horseCount(minDist):
    i = 0
    count = 1
    j = 0
    while i < n - 1:
        if horses[i + 1] - horses[j] >= minDist:
            count += 1
            j = i + 1
        i += 1

    return count

left = horses[0]
right = horses[-1]
maxDist = 0

while left <= right:
    mid = (left + right) // 2

    count = horseCount(mid)
    # 왜 같아도 계속 탐색??
    # 테스트 케이스의 경우도 최소 거리가 2일때, 3일때가 모두 정답이라
    # 그 중 최대 거리를 찾아야하기 때문.
    if count >= c:
        maxDist = mid
        left = mid + 1
    else:
        right = mid - 1

print(maxDist)


# 240414
def count_horse(dist):
    present = houses[0] # 첫번째 말을 골라야 다른 말을 고를 때 거리가 최대가 되게 할 수 있음.
    cnt = 1
    for h in houses:
        # dist 보다 먼 말을 선택해서 마릿수 카운트
        if h - present >= dist:
            present = h
            cnt += 1

    return cnt


N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()


s = 1
e = houses[N-1] - houses[0]
ans = 0

while s <= e:
    mid = (s + e) // 2

    # 말이 더 많이 들어갈 수 있는건 정답일 수 있는 상황
    # 근데 말이 많다 == 거리가 짧다 == 거리를 늘려서 그 중 가장 먼 거리를 구하자.
    if count_horse(mid) >= C:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1


print(ans)
