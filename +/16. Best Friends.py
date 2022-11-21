import sys
from collections import deque

readl = sys.stdin.readline

def nC2(n):
    return int(n * (n - 1) / 2)


n, k = map(int, readl().split())
students = [[i, name, len(name)] for i, name in enumerate([readl().rstrip() for _ in range(n)])]

# 큐를 이름 길이별로 운영
queue = [deque() for _ in range(21)] # 2글자부터 20글자
sum = 0

# 처음 K개 넣고 시작.
for i in range(k + 1):
    _, name, length = students[i]
    queue[length].append(name)
# 처음 K 개에 대한 베프 쌍 개수
# 처음에는 k range 안에 있고 이름 길이 같으면 전부 다 친구가 될 수 있음 nC2
for i in range(2, 21):
    if queue[i]:
        sum += nC2(len(queue[i]))

# print(queue, sum)

# 그리고 나서는 맨앞의거 하나 없애고, 맨 뒤에거 하나 넣어주는 식으로
# 대신 이미 큐에 들어간 애들은 베프가 되었으니 새로운 애에 대해서 나머지 친구들과 베프가 되면 됨.
for i in range(k + 1, n):
    _, name, length = students[i]
    queue[students[i - k - 1][2]].popleft()
    queue[length].append(name)

    sum += (len(queue[length]) - 1)

    # print(queue, sum)

print(sum)
