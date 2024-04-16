n = int(input())
prizes = []

for i in range(n):
    arr = list(map(int, input().split()))
    diff_arr = sorted(list(set(arr)), reverse=True)

    if len(diff_arr) == 1:
        prizes.append(10000 + diff_arr[0] * 1000)
    elif len(diff_arr) == 2:
        prizes.append(1000 + diff_arr[0] * 100)
    else:
        prizes.append(diff_arr[0] * 100)

print(max(prizes))




# 240416 풀이
def checkPrice(dice):
    if len(set(dice)) == 1:
        return 10000 + dice[0] * 1000

    elif len(set(dice)) == 2:
        for c in list(set(dice)):
            dice.remove(c)
        return 1000 + dice[0] * 100

    else:
        return max(dice) * 100
    
def checkPrice2(dice):
    if dice[0] == dice[1] and dice[1] == dice[2]:
        return 10000 + dice[0] * 1000

    elif dice[0] == dice[1]:
        return 1000 + dice[0] * 100

    elif dice[1] == dice[2]:
        return 1000 + dice[1] * 100
    
    elif dice[0] == dice[2]:
        return 1000 + dice[2] * 100
    
    else:
        return max(dice) * 100


N = int(input())

max_price = 0
for _ in range(N):
    dice = list(map(int, input().split()))
    price = checkPrice2(dice)
    if max_price < price:
        max_price = price

print(max_price)
