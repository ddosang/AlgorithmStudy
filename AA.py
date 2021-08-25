# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import sys
# sys.stdin = open("input.txt", "rt")
#
# n, k = map(int, input().split())
#
# cards = list(map(int, input().split()))
# cards.sort()

n = 5
cards = [1,2,3,4,5]

sum = 0
cards_sums = []
for i in range(n):
    sum = 0
    sum += cards[i]
    for j in range(n):
        if i!=j:
            sum += cards[j]
            for kk in range(n):
                if i != j and j != kk and i != kk:
                    sum+= cards[kk]
                    cards_sums.append(sum)
print(cards_sums)