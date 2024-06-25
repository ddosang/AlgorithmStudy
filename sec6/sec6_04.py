# 혼자 짠 코드..
# return True 로는 재귀를 탈출할 수가 없다는 것이 문제점.

def DFS(index):
    if index == n+1:
        local_sum = 0
        for i in range(1, n+1):
            if check[i] == 1:
                local_sum += nums[i - 1]

        if local_sum == total - local_sum:
            # print("YES")
            return True

    else:
        check[index] = 1
        DFS(index + 1)
        check[index] = 0
        DFS(index + 1)

    return False

n = int(input())
nums = list(map(int, input().split()))
total = sum(nums)
check = [0] * (n + 1)


if DFS(1):
    print("YES") # YES 가 2번 찍힘..
else:
    print("NO")




# 강의 코드
# check 를 쓰지 않고, sum 을 이용해서!!
import sys

def DFS(index, sum):
    if sum > total // 2:
        return
    
    if index == n: # 0번 index 부터 사용.
        if sum == total - sum:
            print("YES")
            sys.exit(0) # 걍 냅다 종료 시켜버려~

    else:
        DFS(index + 1, sum + nums[index])
        DFS(index + 1, sum)


n = int(input())
nums = list(map(int, input().split()))
total = sum(nums)

if total % 2 == 1:
    print("NO")
    sys.exit(0)

DFS(0, 0)

print("NO") # 종료가 안됐다면 없는거니까 NO


# 240625 복습
import sys
input = sys.stdin.readline

def DFS(level):
    global sum_local
    if level == N:
        if sum_local == total - sum_local:
            print(sum_local, total)
            print("YES")
            exit(0)
        return
    
    sum_local += arr[level]
    DFS(level + 1)
    sum_local -= arr[level]
    DFS(level + 1)


N = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
sum_local = 0

if total % 2 == 1:
    print("NO")
    exit(0)


DFS(0)

print("NO")
