import sys

readl = sys.stdin.readline

def child(num):
    if num > max_fish:
        return False

    # sum 에는 애들이 먹고 남는 것과, 모든 세금을 누적.
    # 앞 -> 뒤 는 이동 가능한 것까지 따져서 세금을 누적하고
    # 뒤 -> 앞 은 모두 누적 해놓고 마지막에 0보다 크거나 같으면 가능, 작으면 불가능.
    sum = 0

    # 앞에서 뒷 마을로 주는것만 생각.
    for i in range(n - 1):
        pos, fish = city[i]
        next_pos, _ = city[i + 1]

        sum += (fish - num) # 일단 애들 먹이고 남거나 필요한만큼 저장.

        # 뒷 마을로 옮길 수 있을 때, 세금을 낼 수 없다면 안옮김.
        if sum >= 0 and (sum - (next_pos - pos)) < 0:
            sum = 0

        # sum < 0 -> 뒷 마을에서 앞 마을로 옮겨야함. 세금을 누적해둠.
        # sum >= 0 인데 세금을 낼 수 있음. -> 앞 마을에서 뒷 마을로 옮김
        else:
            sum -= (next_pos - pos)


    sum += (city[-1][1] - num)

    return (sum >= 0)


def child2(num):
    c = 0  # 이전 마을에서 남는 물고기를 다음 마을로 넘긴다.
    for i in range(n - 1):
        remain = city[i][1] + c - num # 현재 마을의 남는 물고기.
        c = remain - (city[i + 1][0] - city[i][0]) # 세금
        # 남은 물고기는 있지만 세금을 낼 수 없으면 이전 마을로부터 받을 필요가 없음.
        if remain >= 0 and c < 0: 
            c = 0
    
    # 맨 마지막엔 지금까지 남은게 num 보다 큰지.
    return city[-1][1] + c >= num


n = int(readl())
city = [list(map(int, readl().split())) for _ in range(n)] # 위치, 물고기 양

fishes = [x[1] for x in city]

start = 0
max_fish = max(fishes)
end = max_fish

sol = 0

while start <= end:
    mid = (start + end) // 2

    # 해당 명수가 가능하면 더 크게
    if child(mid):
        start = mid + 1
        sol = mid
    else:
        end = mid - 1

print(sol)