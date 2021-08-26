'''
주사위 게임
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게
임이 있다.
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된
다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금
으로 받게 된다.
N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램
을 작성하시오
'''

n = int(input())

def computePrice(x, y, z):
    price = 0
    if x == y and y == z:
        price = 10000 + x*1000
    elif x == y:
        price = 1000 + x * 100
    elif y == z:
        price = 1000 + y * 100
    elif z == x:
        price = 1000 + z * 100
    else:
        price = max(x, y, z) * 100

    return price

maxPrice = 0

for i in range(n):
    x, y, z = map(int, input().split())
    price = computePrice(x, y, z)
    if maxPrice < price:
        maxPrice = price

print(maxPrice)

'''
▣ 입력설명
첫째 줄에는 참여하는 사람 수 N(2<=N<=1,000)이 주어지고 그 다음 줄부터 N개의 줄에 사람
들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
▣ 출력설명
첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.
▣ 입력예제 1
3 3
3 6
2 2 2
6 2 5
▣ 출력예제 1
12000
'''