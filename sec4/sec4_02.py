
k, n = map(int, input().split())

lineLengths = []
totalLength = 0

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
