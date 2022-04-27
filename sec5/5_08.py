n = int(input())
words = []

# 입력이 어차피 100까지라 그냥 배열로 했는데,

for i in range(n):
    words.append(input())

# remove 함수가 없는 언어를 썼다면,
# indexes = [i for i in range(n)]
# for i in range(n-1):
#     word = input()
#     for i in range(n):
#         if words[i] == word:
#             indexes[i] = 0
# 
# for i in range(n):
#     if indexes[i] != 0:
#         print(i)

for i in range(n-1):
    words.remove(input())

print(words[0])


# 강의 방법. 배열은 비효율적이니 dictionary 써라 가 핵심이었음.
dict_word = {}
for i in range(n):
    dict_word[input()] = 1

for i in range(n-1):
    dict_word[input()] -= 1

for key, val in dict_word:
    if val == 1:
        print(key)
        break
