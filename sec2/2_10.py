# 240417 
# 뭔가 깔끔하게 풀었는데?
N = int(input())
answers = list(map(int, input().split()))

score = 0
cnt = 0 # 연속된 개수 세기
for a in answers:
    if a == 1:
        cnt += 1
        score += cnt # 그 개수가 점수
    else:
        cnt = 0 # 틀린게 나오면 초기화

print(score)



#이전에 푼 것.
n = int(input())
scores = list(map(int, input().split()))

real_scores = [0] * len(scores)

real_scores[0] = scores[0]
for i in range(1, len(scores)):
    if scores[i] == 0:
        real_scores[i] = 0
    elif scores[i] == 1 and scores[i-1] != 0:
        real_scores[i] = real_scores[i - 1] + 1
    elif scores[i] == 1 and scores[i - 1] == 0:
        real_scores[i] = 1


print(sum(real_scores))
