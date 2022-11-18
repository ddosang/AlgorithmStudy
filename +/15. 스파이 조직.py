import sys

readl = sys.stdin.readline

n, spy = readl().split()
n = int(n)
spy = list(spy)

조직도 = {}

balance = 0


level = 0
i = 0

while i < len(spy):
    s = spy[i]

    if s.isdigit():
        # 한자리 숫자가 아닐수도 있으니 숫자는 계속 더해봐야함.
        num = ''
        while spy[i].isdigit():
            num += spy[i]
            i += 1

        # 조직도[level] 에 스파이를 넣는다.
        if not level in 조직도.keys():
            조직도[level] = []
        조직도[level].append(int(num))

    # < 이 나오면 트리에서 자식으로 내려간 것.
    elif s == "<":
        level += 1
        i += 1

    # > 이 나오면 해당 레벨이 끝난 것.
    else:
        level -= 1
        i += 1

print(*조직도[n])
