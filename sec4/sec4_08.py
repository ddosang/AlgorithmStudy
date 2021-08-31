'''
침몰하는 타이타닉(그리디)
유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고
있습니다. 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있
으며, 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 프로그램을 작성하세요.
▣ 입력설명
첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다.
각 승객의 몸무게는 M을 넘지는 않습니다. 즉 탈출을 못하는 경우는 없습니다.
▣ 출력설명
첫째 줄에 구명보트의 최소 개수를 출력합니다.
▣ 입력예제 1
5 140
90 50 70 100 60
▣ 출력예제 1
3
'''

n, m = map(int, input().split())
height = list(map(int, input().split()))

height.sort()

cnt = 0
while len(height) > 1: #한명만 남았을 때는 따질 필요가 없음.

    # 젤 가벼운애랑 젤 무거운애 더해서 구명보트 무게 안쪽이면
    if height[0] + height.pop() <= m:
        cnt += 1
        height.pop(0) #둘이 같이 탈출
    else:
        cnt += 1 #더 무거우면 젤 무거운 애만 탈출

if len(height) == 1:
    cnt += 1

print(cnt)