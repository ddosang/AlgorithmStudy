

import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())

ox = list(map(int, input().split()))

score = 0
connect = 1

for i in ox:
    if i == 1:
        score += connect
        connect += 1
    else:
        connect = 1

print(score)