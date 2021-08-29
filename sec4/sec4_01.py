
n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort() #정렬

start = 0
end = n-1
mid = (n-1)//2

while True:
    midInArray = arr[mid] #index가 중간인 값이
    if midInArray < m: #우리가 찾는 m이 중간보다 크면
        start = mid + 1 #mid 뒤쪽 list에서 다시 찾는다.
        mid = (start + end) // 2
    elif midInArray == m: #같으면 해당 index+1을 출력
        print(mid+1)
        break
    else: #우리가 찾는 m이 중간보다 작으면
        end = mid - 1 #mid 앞쪽 list에서 찾는다.
        mid = (start + end) // 2
