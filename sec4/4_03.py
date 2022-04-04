import sys

def countDVD(time):
    dvd = 1
    scatterTime = 0
    maxTime = 0
    i = 0

    while i < n:
        # 노래를 넣다가
        scatterTime += times[i]

        # dvd 시간을 초과하면 맨 마지막거 하나 뺴고
        # dvd 녹화 최대 시간 경신, dvd 장수 추가, scatterTime 초기화
        if scatterTime > time:
            scatterTime -= times[i]
            i -= 1

            if maxTime < scatterTime:
                maxTime = scatterTime

            dvd += 1
            scatterTime = 0

        # 맨 마지막 dvd 는 time 보다 길게 녹화되지 않으니가
        # 따로 검사해줘야함.
        if i == n-1:
            if maxTime < scatterTime:
                maxTime = scatterTime

        i += 1

    return dvd, maxTime




# sys.stdin = open("input.txt", "rt")

# 시간이 다 다른 n개의 곡을 m개의 씨디(같은 시간)에 쪼개 넣기.
n, m = map(int, input().split())
times = list(map(int, input().split()))
possible = []


# 평균부터 시작.
start = sum(times) // m
end = sum(times)

minTime = end

while start <= end:
    mid = (start + end) // 2
    # 이분 탐색으로 시간을 넣어서 녹화를 해봄.
    # 해당 시간 안에 dvd 개수가 더 많이 녹화됨 -> 시간을 늘려야 됨.
    # dvd 개수가 더 작거나 같게 녹화됨 -> 시간을 줄여야 됨. (제일 작은 시간을 찾는게 목적이니 개수가 같은 것도 포함)
    # start 와 end 가 교차되면 끝.
    dvd, time = countDVD(mid)

    if mid >= max(times) and dvd <= m:
        minTime = mid
        end = mid - 1
        if minTime > time:
            minTime = time
    else:
        start = mid + 1

print(minTime)

