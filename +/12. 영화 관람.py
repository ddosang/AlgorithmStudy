import sys

readl = sys.stdin.readline

n = int(readl())
movie = [list(map(int, readl().split())) for _ in range(n)]

movie.sort(key=lambda x:x[1])

cnt = 0
before_end = 0
for start, end in movie:
    # 2시간 이상이면서, 지금 보고 있는 영화보다 늦게 시작하는 영화만 볼 수 있음.
    if (end - start) > 1 and start >= before_end:
        cnt += 1
        before_end = end

print(cnt)

