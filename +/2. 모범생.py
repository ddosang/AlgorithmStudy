import sys

n = int(sys.stdin.readline())
scores = list(enumerate(list(map(int, sys.stdin.readline().split()))))

scores.sort(key=lambda x:x[1], reverse=True)

for id, _ in scores[0:3]:
    print(id + 1, end=' ')
