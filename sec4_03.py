

def countDVD(time):
    dvd = 1
    scatterTime = 0 #곡 개수 별로 쪼갠 시간
    maxTime = 0 #쪼갠 시간 중 가장 큰 것을 저장
    i = 0
    while i < n:
        scatterTime += musicTimes[i]

        if scatterTime > time: #순차적으로 더하다가 time보다 커지면
            scatterTime -= musicTimes[i] #그 앞 노래까지 넣을 수 있음.
            i -= 1 #다음에는 시간을 넘긴 그 노래부터 넣어야하니까 줄인다.
            if scatterTime > maxTime:
                maxTime = scatterTime

            dvd += 1
            scatterTime = 0

        if i == n-1: #맨 마지막 dvd 의 시간도 계산
            if scatterTime > maxTime:
                maxTime = scatterTime
        i += 1

    return dvd, maxTime

#입력 받기
n, m = map(int, input().split())
musicTimes = list(map(int, input().split()))

#음악 전체 시간과 평균 시간 계산
totalTime = 0
for i in range(n):
    totalTime += musicTimes[i]

minTime = totalTime
avgMusicTime = totalTime // m

#이분탐색
start = avgMusicTime
end = totalTime
while start <= end:
    mid = (start + end) // 2
    dvdCount, time = countDVD(mid)

    if dvdCount <= m: #dvd 개수가 적으면
        end = mid - 1 #시간을 줄여야 함.
        if minTime > time: #그 중 가장 작은 시간이 필요함.
            minTime = time
    else: #dvd 개수가 많으면 시간을 늘려야함.
        start = mid + 1

print(minTime)