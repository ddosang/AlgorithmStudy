n, m  = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

left = 0
right = len(nums) - 1
m_index = nums.index(m)
while left <= right:
    mid = (left + right) // 2
    if m_index == mid:
        print(m_index + 1)
        break
    elif m_index < mid:
        right = mid - 1
    else:
        left = mid + 1
