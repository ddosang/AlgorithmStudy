'''
마구간 정하기(결정알고리즘)
N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마
구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을
마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대
값을 출력하는 프로그램을 작성하세요.
▣ 입력설명
첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다.
둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩
주어집니다.
▣ 출력설명
첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.
▣ 입력예제 1
5 3
1 2 8 4 9 ▣
출력예제 1
3
'''

def horseCount(minDist): #배치할 수 있는 최대 말의 개수 return
    horsePosition = 0
    horse = 1

    # for i in range(c - 1):
    #
    #     for j in range(horsePosition + 1, n):
    #         if (horseHouse[j] - horseHouse[horsePosition]) >= minDist:
    #             horsePosition = j
    #             horse += 1
    #             break

    for i in range(1, n):
        if (horseHouse[i] - horseHouse[horsePosition]) >= minDist:
            horsePosition = i
            horse += 1


    return horse

#입력 받고 정렬.
n, c = map(int, input().split())
horseHouse =[]
for _ in range(n):
    horseHouse.append(int(input()))
horseHouse.sort()

#이분탐색
start = horseHouse[0]
end = horseHouse[n-1]
maxDistance = 0
while start <= end:
    mid = (start+end) // 2

    if horseCount(mid) >= c:
        maxDistance = mid
        start = mid + 1
    else:
        end = mid - 1

print(maxDistance)