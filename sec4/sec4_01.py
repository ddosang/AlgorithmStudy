'''
이분검색
임의의 N개의 숫자가 입력으로 주어집니다. N개의 수를 오름차순으로 정렬한 다음 N개의 수
중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는
프로그램을 작성하세요. 단 중복값은 존재하지 않습니다.
▣ 입력설명
첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다.
두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.
▣ 출력설명
첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.
▣ 입력예제 1
8 32
23 87 65 12 57 32 99 81
▣ 출력예제 1
3
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort() #정렬

start = 0
end = n-1
mid = (n-1)//2

while start<=end:
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
