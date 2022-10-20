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

def search_front_back(index, arr, find):
    count = 0
    length = len(arr)
    back_index = index + 1
    while index > -1 and arr[index] == find:
        index -= 1
        count += 1

    while back_index < length and arr[back_index] == find:
        back_index += 1
        count += 1

    return count

# 입력 처리
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

find_n = int(sys.stdin.readline())
find_arr = list(map(int, sys.stdin.readline().split()))

for i in range(find_n):
    # 이진 탐색으로 해당 숫자 위치 찾고
    index = binary_search(0, n - 1, find_arr[i], arr)
    # 양 옆에 같은 숫자 탐색
    count = search_front_back(index, arr, find_arr[i])
    print(count, end=' ')
