import sys

n = int(sys.stdin.readline())
leaves = [int(sys.stdin.readline()) for _ in range(n)]

leaves.sort()

cnt = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        dist1 = leaves[j] - leaves[i]
        for k in range(j + 1, n):
            dist2 = leaves[k] - leaves[j]

            if dist2 >= dist1 and dist2 <= 2*dist1:
                cnt += 1
            elif dist2 > 2 * dist1:
                break

print(cnt)
