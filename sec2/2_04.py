n = int(input())
scores = list(map(int, input().split()))

avg = round(sum(scores) / n)

arr = list(map(lambda x: x-avg, scores))
arr = list(enumerate(arr)) # index 를 뽑아야하니까 enumerate 사용.

# 점수 편차 절댓값 기준 정렬
arr.sort(key=lambda x:abs(x[1]))

# 첫번째 것이 가장 작은 값이니까 해당 값을 기준으로
key = abs(arr[0][1])

# 같은 값이 나오면 출력하면 된다. index 도 오름차순 정렬 되어있으므로!!
# 이렇게 하면 -는 제외됨.
for index, value in arr:
    if value == key:
        print(avg, index + 1)
        break
