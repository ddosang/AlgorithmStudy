'''
카드 역배치(정올 기출)
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓
여있다. 각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다.

이제 여러분은 다음과 같은 규칙으로 카드의 위치를 바꾼다: 구간 [a, b] (단, 1 ≤ a ≤ b ≤
20)가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
예를 들어, 현재 카드가 놓인 순서가 위의 그림과 같고 구간이 [5, 10]으로 주어진다면, 위치
5부터 위치 10까지의 카드 5, 6, 7, 8, 9, 10을 역순으로 하여 10, 9, 8, 7, 6, 5로 놓는다.
'''

cards = []
#list(range(21)) # 이렇게 하면 0~20까지 list 생김....
#대신 마지막에 cards.pop(0)해서 0은 날려야함.

for i in range(20):
    cards.append(i+1)

#1 reversedCards에 뒤집어서 넣고 해당 부분 교체
for i in range(10):
    a, b = map(int, input().split())

    reversedCards = []
    for j in range(b-1,a-2,-1):
        reversedCards.append(cards[i])

    cards[a-1:b] = reversedCards

for card in cards:
    print(card, end=' ')



#2 a번째와 b번째 바꾸고 a+1번째와 b-1번째 바꾸고...
for i in range(10):
    a, b = map(int, input().split())
    mid = (a+b-2) // 2 #중간 지점 파악.
    for j in range(a-1,mid+1): #시작지점부터 중간지점까지 바꿔치기
        temp = cards[i]
        cards[i] = cards[b-1-i + a-1]
        cards[b - 1 - i + a - 1] = temp


for card in cards:
    print(card, end=' ')

'''
▣ 입력설명
총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다. i번째 줄에는 i번째 구간의 시
작 위치 ai와 끝 위치 bi가 차례대로 주어진다. 이때 두 값의 범위는 1 ≤ ai ≤ bi ≤ 20이다.
▣ 출력설명
1부터 20까지 오름차순으로 놓인 카드들에 대해, 입력으로 주어진 10개의 구간 순서대로 뒤집
는 작업을 했을 때 마지막 카드들의 배치를 한 줄에 출력한다.
▣ 입력예제 1
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20
▣ 출력예제 1
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
'''