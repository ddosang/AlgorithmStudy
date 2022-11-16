import sys

readl = sys.stdin.readline

n = int(readl())
words = readl().split()

dict = {}


for idx, w in enumerate(words, 1):
    # 처음 나온 단어면 dict 초기화
    if not w in dict.keys():
        dict[w] = []

    # 해당 단어가 나온 순서 기록
    dict[w].append(idx)


cnt = 0
for key in dict.keys():
    # 두 번 이상 나온 단어 : 단어, 순서를 출력
    if len(dict[key]) > 1:
        print(key, end=' ')
        for idx in dict[key]:
            print(idx, end=' ')
        print()
    # 한 번만 나오면 개수를 세둔다.
    else:
        cnt += 1

# 단어 전체가 한 번씩만 나오면 unique
if cnt == len(words):
    print("unique")
