n = int(input())
arr = []
max_sum = 0

for i in range(n):
    arr += [list(map(int, input().split()))]

# for 문 안에서 선언해도 전역변수가 되기 때문에 for문 들어가기 전에 초기화 필수..
# 행
local_sum = 0
for i in range(n):
    local_sum = sum(arr[i])
    if max_sum < local_sum:
        max_sum = local_sum
# 열
local_sum = 0
for i in range(n):
    local_sum = 0
    for j in range(n):
        local_sum += arr[j][i]
    if max_sum < local_sum:
        max_sum = local_sum

# 대각선 좌측 상단 -> 우측 하단\
local_sum = 0
for i in range(n):
    local_sum += arr[i][i]
if max_sum < local_sum:
    max_sum = local_sum

# 대각선 좌측 하단 -> 우측 상단
local_sum = 0
for i in range(n):
    local_sum += arr[i][n-1-i]
if max_sum < local_sum:
    max_sum = local_sum

print(max_sum)
