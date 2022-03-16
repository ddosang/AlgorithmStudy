cards = [i for i in range(21)]

for i in range(10):
    s, e = map(int, input().split())
    count = (e - s + 1) // 2
    for j in range(count):
        cards[s + j], cards[e - j] = cards[e - j], cards[s + j]

for card in cards[1:]:
    print(card, end=' ')
