n, k = map(int, input().split())

queue = [i + 1 for i in range(n)]

count = 0
while len(queue) > 1:
    prince = queue.pop(0)
    count += 1

    if count == k:
        count = 0
        continue

    queue.append(prince)

print(queue[0])
