def split_tree(height):
    total = 0
    for t in trees:
        if t - height > 0:
            total += (t - height)
    return total

# 다 해봐야하나..? 싶었는데 너무 많을거같음 -> 이진탐색

N, M = map(int, input().split())
trees = list(map(int, input().split()))

s = 0
e = max(trees)
ans = 0

while s <= e:
    # 설정할 수 있는 높이
    mid = (s + e) // 2

    # 잘린 나무가 크다는건 높이가 너무 낮다는 것.
    # 하지만 잘린 나무가 커도 답이 될 수 있음.
    if split_tree(mid) >= M:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)
