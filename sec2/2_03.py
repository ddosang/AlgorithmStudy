from itertools import combinations

n, k = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

cards_sum = set()

for arr in list(combinations(cards, 3)):
    cards_sum.add(sum(arr))

print(sorted(list(cards_sum), reverse=True)[k-1])
