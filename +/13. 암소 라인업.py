import sys
import copy

readl = sys.stdin.readline

n = int(readl())
cows = [list(map(int, readl().split())) for _ in range(n)] # x 좌표, 번호
cows.sort()


# 소의 종류를 관리하기 위해서 dictonary 로 관리
dict = {}

for x, num in cows:
    if not num in dict.keys():
        dict[num] = 0
    dict[num] += 1

종류 = len(dict)

copy_dict = copy.deepcopy(dict)



left = 0
right = n - 1

# left 보다 앞쪽에 겹치는 종류의 소가 하나도 없을 때까지 left 땡기고
while left < n - 종류 and dict[cows[left][1]] > 1:
    dict[cows[left][1]] -= 1
    left += 1
# right 보다 뒷쪽에 겹치는 종류의 소가 없을 때까지 right 땡김
while 종류 <= right and dict[cows[right][1]] > 1:
    dict[cows[right][1]] -= 1
    right -= 1


dist = cows[right][0] - cows[left][0]

# print(left, right)

# 근데...! index 차가 거리였다면 위에서 끝내도 되는데,
# 여기서는 x 좌표가 있으므로 left 먼저 땡긴것과 right 먼저 땡긴 것의 결과가 차이나서
# 그 둘을 비교하기 위해 한번 더 돌림.
# 솔직히 이 코드 넘 구린디.........
left = 0
right = n - 1

while 종류 <= right and copy_dict[cows[right][1]] > 1:
    copy_dict[cows[right][1]] -= 1
    right -= 1

while left < n - 종류 and copy_dict[cows[left][1]] > 1:
    copy_dict[cows[left][1]] -= 1
    left += 1

dist = min(dist, cows[right][0] - cows[left][0])
print(dist)
