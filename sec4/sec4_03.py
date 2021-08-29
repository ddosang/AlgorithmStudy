
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
            dvd += 1
            scatterTime = 0

        i += 1
    return dvd


#입력 받기
n, m = map(int, input().split())
musicTimes = list(map(int, input().split()))

#음악 전체 시간과 평균 시간 계산
totalTime = 0
for i in range(n):
    totalTime += musicTimes[i]

minTime = totalTime
avgMusicTime = totalTime // n
maxMusicTime = max(musicTimes)

#이분탐색
start = avgMusicTime
end = totalTime
while start <= end:
    mid = (start + end) // 2

    if mid >= maxMusicTime and countDVD(mid) <= m: #dvd 개수가 적으면
        minTime = mid
        end = mid - 1 #시간을 줄여야 함.
    else: #dvd 개수가 많으면 시간을 늘려야함.
        start = mid + 1

print(minTime)