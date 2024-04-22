# 240422
# 과거의 나는 time check_count 에서 max_time 을 왜 저장하려고 한지 모르겠음.
def check_count(mid):
    local_cd = 0
    cnt = 0
    max_time = 0
    for i in range(len(arr)):
        local_cd -= arr[i]
        if local_cd < 0:
            cnt += 1
            local_cd = mid - arr[i]

    return cnt


N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 한 장의 DVD 당 시간
s = min(arr)
e = sum(arr)

min_time = sum(arr)

while s <= e:
    mid = (s + e) // 2

    # mid 시간짜리 CD 몇 개가 나오지?
    count = check_count(mid)

    # count 가 크다 == DVD 개수가 많다 == DVD 당 시간을 늘린다.
    # 더 작은 숫자에 넣을 수 있는 것도 답임.
    # time 은 arr 최댓값 보다 무조건 커야 함 그거보다 작게 나오면 mid 를 늘려서 다시 수행해봐야함.
    if mid >= max(arr) and count <= M:
        min_time = mid
        e = mid - 1
            
    else:
        s = mid + 1

print(min_time)
