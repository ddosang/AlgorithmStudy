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

