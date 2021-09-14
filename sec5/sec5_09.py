'''
Anagram(아나그램 : 구글 인터뷰 문제)
Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아
나그램이라고 합니다.
예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면
A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다. 즉 어느 한 단어를 재
배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세
요. 아나그램 판별시 대소문자가 구분됩니다.
▣ 입력설명
첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다.
단어의 길이는 100을 넘지 않습니다.
▣ 출력설명
두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.
▣ 입력예제 1
AbaAeCe
baeeACA
▣ 출력예제 1
YES
'''

firstWord = input()
secondWord = input()
anagram = dict()

#dictionary 초기화를 위해 두 단어에 들어간 알파벳만 뽑은 list를 만들어서
#key는 알파벳 하나하나 value는 0으로 초기화
arr = list(map(str, firstWord)) + list(map(str, secondWord))
arr = list(set(arr))
for c in arr:
    anagram[c] = 0

#첫번째 단어에 있는 각 알파벳에 대한 dict value를 알파벳 개수로 설정
for c in firstWord:
    anagram[c] += 1
    #anagram[c] = anagram.get(c, 0) + 1 #이렇게 하면 초기화 없이 가능.

#두번째 단어에서는 알파벳에 대한 dict value를 기존 값 - (두번째 알파벳 개수)로 설정
for c in secondWord:
    anagram[c] -= 1

#만약 두 단어의 구성이 같았다면 value가 모두 0일 것임.
#for key, value in anagram.items():
for value in anagram.values():
    if value != 0:
        print("NO")
        break
else:
    print("YES")


#강의방법
str1 = dict()
str2 = dict()
for x in firstWord:
    str1[x] = str1.get(x, 0) + 1
for x in secondWord:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

#강의방법 개선은 내 방식과 같음.

#dictionary를 안쓰고 list를 쓴다면?
firstWord = input()
secondWord = input()

str = [0] * 52

for c in firstWord:
    if ord(c) >= 97: #c.islower() 써도 됨.
        str[26 + ord(c) % 97] += 1
    elif ord(c) >= 65: #c.isupper() 써도 됨.
        str[ord(c) % 65] += 1

for c in secondWord:
    if ord(c) >= 97:
        str[26 + ord(c) % 97] -= 1
    elif ord(c) >= 65:
        str[ord(c) % 65] -= 1


for x in str:
    if x != 0:
        print("NO")
        break
else:
    print("YES")