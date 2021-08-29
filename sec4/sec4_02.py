
k, n = map(int, input().split())

lineLengths = []
totalLength = 0

#1 시간 초과 40점
for i in range(k):
    length = int(input())
    lineLengths.append(length)
    totalLength += length

#n개를 전부 잇고 k개로 나누면 나오는 이론적인 최대 길이.
maxLengthMath = totalLength // n

#이론적인 최대 길이부터 하나씩 내리면서
#k개의 전선을 각각 나누어 보고 n개가 만들어지면 break
for i in range(maxLengthMath, 0, -1):
    count = 0
    for j in range(k):
        count += lineLengths[j] // i

    if count == n:
        print(i)
        break


#2. 강의 듣고 짠 것 (이분 검색)
start = 1
end = maxLengthMath #1~이론최대길이 까지 이분 검색을 해서
max = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in range(len(lineLengths)):
        count += lineLengths[i] // mid

    if count >= n:
        if max < mid: #count>=n을 만족하는 것 중 최대 길이 찾아낸다.
            max = mid
        start = mid + 1
    else:
        end = mid - 1
