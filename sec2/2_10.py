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
