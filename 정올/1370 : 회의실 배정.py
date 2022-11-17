import sys

readl = sys.stdin.readline

n = int(readl())
meetings = [list(map(int, readl().split())) for _ in range(n)]

# 끝나는 시간 기준으로 정렬
meetings.sort(key=lambda x:x[2])

doMeet = []
doEnd = 0
for idx, start, end in meetings:
    # 이전 회의의 끝나는 시간보다 다음 회의의 시작 시간이 뒤이면 회의 가능.
    if start >= doEnd:
        doEnd = end
        doMeet.append(idx)
    else:
        continue

print(len(doMeet))
print(*doMeet)
