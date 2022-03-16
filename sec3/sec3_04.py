
'''
두 리스트 합치기
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
▣ 출력설명
오름차순으로 정렬된 리스트를 출력합니다.
▣ 입력예제 1
3 1
3 5
5 2
3 6 7 9
▣ 출력예제 1
1 2 3 3 5 6 7 9
'''

n = int(input())
arrayN = list(map(int, input().split()))

m = int(input())
arrayM = list(map(int, input().split()))

#1 파이썬이라 가능한 방법.
# array = arrayN + arrayM
#
# array.sort()


#2 정석
indexN = 0
indexM = 0
array = []
for i in range(n+m):
    if indexN < n and indexM < m: #index를 벗어나지 않는 선에서
        if arrayN[indexN] < arrayM[indexM]: #작은거 먼저 넣는다.
            array.append(arrayN[indexN])
            indexN += 1
        else:
            array.append(arrayM[indexM])
            indexM += 1
    else: #index를 벗어남 -> 한 list가 바닥났음.
        if n > m: #큰쪽이 남은 list 이므로
            while indexN < n: #남은거 고대로 넣으면 됨.
                array.append(arrayN[indexN])
                indexN += 1
        elif n == m: #같으면
            if indexN > indexM: #어느 쪽이 남았는지(넣은 index가 작은쪽) 판별 후
                array.append(arrayM[indexM]) #남은 쪽을 넣어줌.
                indexM += 1
            else:
                array.append(arrayN[indexN])
                indexN += 1
        else: #역시 큰쪽.
            while indexM < m:
                array.append(arrayM[indexM])
                indexM += 1


for value in array:
    print(value, end=' ')
