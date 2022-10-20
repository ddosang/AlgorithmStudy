import sys

def input_data():
    n = int(sys.stdin.readline())
    monies = list(map(int, sys.stdin.readline().split()))
    total = int(sys.stdin.readline())
    return n, monies, total

# 4
# 110 120 140 150
# 485
# 일 때, 작은건 줄 수 있고 넘치는건 큰 애들에서 limit 만 주게 해야함.
# 그러면 485 // 4 = 121 은 4개에 무조건 줄 수 있으니 limit 은 이것보단 크거나 같을 거임.
# 그리고 젤 큰 150 보단 작거나 같을거임.
# avg(total) ~ max(monies) 사이에서 n개에 다 줄 수 있는 가장 큰 limit 을 찾으면 됨.

def limit(n, monies, total):
    max_money = max(monies)
    if sum(monies) <= total:
        return max_money

    ans = 0
    monies.sort()

    start = total // n
    end = max_money

    while start <= end:
        mid = (start + end) // 2

        temp_total = total
        for m in monies:
            if m <= mid:
                temp_total -= m
            else:
                temp_total -= mid

        # 모두에게 줄 수 있다면 그 중 가장 큰 값을 찾아서!!
        if temp_total >= 0:
            start = mid + 1
            ans = mid
        # 모두에게 줄 수 없다면 limit 을 낮춰야함.
        else:
            end = mid - 1

    return ans


n, monies, total = input_data()

print(limit(n, monies,total))
