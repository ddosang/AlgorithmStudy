n = int(input())

for i in range(n):
    word = input().lower()

    for i in range(n // 2):
        if word[i] != word[len(word)-1-i]:
            print("NO")
            break
    else:
        print("YES")
