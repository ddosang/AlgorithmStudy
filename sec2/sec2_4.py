

'''
대표값
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
'''


n = int(input())
scores = list(map(int, input().split()))

sum = 0

for i in range(n):
    sum += scores[i]


avg = round(sum / n) #소숫점 첫째 자리에서 반올림

far_from_avg = list(map(lambda x: x-avg, scores)) #편차
far_from_avg_plus = list(map(abs, far_from_avg))  #편차 절댓값

minimum = min(far_from_avg_plus) #편차 절댓값 중 가장 작은 값

for i in range(n):
    if far_from_avg[i] == minimum: #차이가 같으면 점수 높은거, 번호 먼저인거 먼저.
        print(avg, i+1)            #출력하고
        break                      #break

else:                                   #만약에 다 돌았는데 break X
    for i in range(n):                  #==같은 편차인 높은 점수 없음.
        if far_from_avg[i] == -minimum: #편차 절댓값이 최소이면서 마이너스인
            print(avg, i+1)             #값을 번호가 먼저인 것만 출력.
            break


'''
▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연
수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.
▣ 입력예제 1
10
45 73 66 87 92 67 75 79 75 80
▣ 출력예제 1
74 7
예제설명)
평균이 74점으로 평균과 가장 가까운 점수는 73(2번), 75(7번), 75(9번)입니다. 여기서 점수가 높은
75(7번), 75(9번)이 답이 될 수 있고, 75점이 두명이므로 학생번호가 빠른 7번이 답이 됩니다.
'''