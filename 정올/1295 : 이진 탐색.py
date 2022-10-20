import sys

def binary_search(start, end, find, arr):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == find:
        return mid
    elif arr[mid] < find:
        return binary_search(mid + 1, end, find, arr)
    else:
        return binary_search(start, mid - 1, find, arr)


# 입력 처리
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

find_n = int(sys.stdin.readline())
find_arr = list(map(int, sys.stdin.readline().split()))

for i in range(find_n):
    print(binary_search(0, n - 1, find_arr[i], arr) + 1)
