import sys

readl = sys.stdin.readline

n = int(readl())
student = [list(map(int, readl().split())) for _ in range(n)]

# 시작 시간 기준으로 정렬.
student.sort()

exist = []

# 시작 시간.
s, e = student[0][0], student[0][1]
for start, end in student:
    # 시작 시간이 이전 것의 끝나는 시간보다 앞쪽이고
    if start <= e:
        # 지금 끝나는 것보다 더 늦게 끝나면 시간 이어 붙인다.
        # 지금 시간보다 늦게 시작하고 일찍 끝나면 이미 포함되어 있으므로 이어붙일 필요 X
        if e < end:
            e = end

    # 시작 시간이 이전 것의 끝나는 것보다 뒷쪽이면
    # 끊어지는 거니까 시간을 구분해서 넣고, 다음 것의 시작 시간 / 끝나는 시간으로 갱신
    else:
        exist.append((s, e))
        s = start
        e = end


exist.append((s, e))

# 학생이 연속적으로 머무르는 시간 중 max
print(max(list(map(lambda x: x[1] - x[0], exist))), end=' ')
# 학생이 없는 시간 중 max
print(max([exist[i][0] - exist[i - 1][1] for i in range(1, len(exist))]))
