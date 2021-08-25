'''
정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
'''


n, m = map(int, input().split())
sum = []

for i in range(1, n+1):
    for j in range(1, m+1):
        sum.append(i+j)

sum.sort()

frequency = [1] * len(sum)
max = 0

#최빈값 알고리즘
for i in range(len(sum)):
    for j in range(i+1, len(sum)):
        if sum[i] == sum[j]:
            frequency[i] += 1

        if frequency[i]>max:
            max = frequency[i]

# #강의 풀이 : data를 새로운 배열의 index로 보고 진행.
# freq2 = [0]*(n+m+3) #약간 여유를 두고.
#
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         freq2[i+j] += 1
#
# for i in range(n+m+1):
#     if freq[i] > max:
#         max = freq[i]



for i in range(len(sum)):
    if max == frequency[i]:
        print(sum[i], end=' ')




'''
▣ 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
▣ 출력설명
첫 번째 줄에 답을 출력합니다.
▣ 입력예제 1
4 6
▣ 출력예제 1
5 6 7
'''