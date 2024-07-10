N = int(input())
coins = [int(input()) for _ in range(N)]
min_diff = sum(coins)

def DFS(level, a, b, c):
    global min_diff

    if level == N:
       if a == b or b == c or c == a:
           return
       diff = max(a, b, c) - min(a, b, c)
       min_diff = min(diff, min_diff)
       return

    # 3명에게 분배니까 이 코인이 A, B, C 에게 한번씩 가는 걸로 했는데,
    # 사람이 더밚았으면 level, persons (배열) 로 넘겨서 for 문 돌렸을듯.
    DFS(level + 1, a + coins[level], b, c)
    DFS(level + 1, a, b + coins[level], c)
    DFS(level + 1, a, b, c + coins[level])


DFS(0, 0, 0, 0)
print(min_diff)
