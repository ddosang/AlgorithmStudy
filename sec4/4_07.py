n = int(input())
boxes = list(map(int, input().split()))
m = int(input())

boxes.sort()

for i in range(m):
    boxes[n-1] -= 1
    boxes[0] += 1

    boxes.sort()

print(boxes[n-1] - boxes[0])
