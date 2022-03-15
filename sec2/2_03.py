n, k = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

cards_sum = set()

for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for l in range(j + 1, len(cards)):
            cards_sum.add(cards[i] + cards[j] + cards[l])

cards_sum = sorted(list(cards_sum), reverse=True)
print(cards_sum[k-1])
