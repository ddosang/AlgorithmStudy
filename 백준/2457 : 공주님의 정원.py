import sys
readl = sys.stdin.readline

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
N = int(readl())

always = (sum(days[:3]) + 1, sum(days[:11]) + 31) # 항상 피어있어야 하는 구간.

# 입력 가공. -> 1월 1일 -> 1
# 2월 1일 -> 32 가 될 수 있게.
flower = []
min_start = 400
max_end = 0
for _ in range(N):
    sm, sd, em, ed = map(int, readl().split())
    start = sum(days[:sm]) + sd
    end = sum(days[:em]) + ed
    
    # 공주 기간보다 앞에서 끝나거나 뒤에서 시작하는건 아예 빼고 시작.
    if end < always[0] or always[1] < start:
        continue

    min_start = min(min_start, start)
    max_end = max(max_end, end)

    flower.append((start, end))

# 못만들면 처음부터 끝내고 시작!!
if min_start > always[0] or max_end < always[1]:
    print(0)
    exit(0)

# 시작 날짜 기준 정렬을 하는데,
# 시작 날짜가 같으면 끝나는 시간이 더 긴게 먼저 오도록 가공.
flower.sort(key=lambda x:x[0])

cnt = 0

t = always[0]
i = 0
while t < always[1]:
    max_e = 0

    while i < len(flower) and flower[i][0] <= t:
        max_e = max(max_e, flower[i][1])
        i += 1
    
    if max_e == t:
        cnt = 0
        break
    
    cnt += 1
    t = max_e

print(cnt)
