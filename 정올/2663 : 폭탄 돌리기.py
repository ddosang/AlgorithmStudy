import sys


readl = sys.stdin.readline

people = 8
limit = 210
k = int(readl()) # 처음에 폭탄 가짐
n = int(readl())
quiz = [[int(c) if c.isdigit() else c for c in readl().split()] for _ in range(n)]

time = 0
k -= 1

i = 0
while i < n:
    t, answer = quiz[i]

    # print(k, time)

    time += t

    if time >= limit:
        print(k + 1)
        break

    if answer == "T":
        k = (k + 1) % people
        i += 1
    else:
        i += 1

if time < limit:
    print(k + 1)
