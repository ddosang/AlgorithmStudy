n = int(input())
entries = []

for i in range(n):
    height, weight = map(int, input().split())
    entries.append((height, weight))


entries.sort(reverse=True)
# 1:1 비교를 해야함.

local_max_weight = 0
count = 1
for i in range(1, n):
    if local_max_weight < entries[i-1][1]:
        local_max_weight = entries[i - 1][1]

    if local_max_weight < entries[i][1]:
        count += 1

print(count)


# 재복습
n = int(input())
entries = [tuple(map(int, input().split())) for _ in range(n)]

entries.sort(key=lambda x:x[0], reverse=True)

count = 1
max_weight = entries[0][1]
for i in range(1, n):

    if entries[i][1] > max_weight:
        max_weight = entries[i][1]
        count += 1

print(count)
